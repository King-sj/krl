from node import Node
from symbols import *
from .global_symbols_utils import init_global_symbols, GlobalInfo
from enum import Enum
from warnings import warn
from dataclasses import dataclass
from typing import Any
from node import Node, NodeType
import requests
from urllib import request
from typing import Dict
import json


class RunState(Enum):
  START = 0
  WAIT = 1
  RUNNING = 2
  END = 3


@dataclass
class StmtVal:
  type: Type
  value: Any


class Interpreter:

  def __init__(self, ast_root: Node) -> None:
    self.root = ast_root
    # ast_root.print_ast()
    # 存储所有 event, function 的必要信息（重入点
    self.global_symbols_table = StackListSymbolTable()
    # 运行时所用的符号表
    self.running_symbol_table = StackListSymbolTable()

    init_global_symbols(self.global_symbols_table, ast_root)
    self.state = RunState.START
    self.is_end = False

  def run(self):
    '''
    脚本执行的入口
    '''
    while not self.is_end:
      if self.state == RunState.START:
        self.start()
      elif self.state == RunState.WAIT:
        self.wait()
      elif self.state == RunState.RUNNING:
        raise RuntimeError("program is already running")
      elif self.state == RunState.END:
        warn("program already closed")
        break
    self.state = RunState.END

  def start(self):
    self.run_event('start')
  def generate_text(self, text: str) -> str:
    '''
    通过NLP生成用户请求文本
    '''
    return text
  def wait(self):
    query = input()
    query = self.generate_text(query)
    try:
      self.run_event(query)
    except Exception as e:
      self.other(query)

  def end(self):
    if self.global_symbols_table.find('end') != -1:
      self.run_event('end')
    self.is_end = True
    self.state = RunState.END
    exit(0)

  def other(self, query):
    # TODO:find most like query
    self.run_event('other')

  def s_statement_list(self, cur: Node) -> StmtVal:
    if len(cur.children) > 1:
      res = self.s_statement_list(cur.children[1])
      if res.type.kind != TypeKind.UNKNOWN:
        return res
    return self.s_statement(cur.children[0])

  def s_statement(self, cur: Node) -> StmtVal:
    name = str(cur.children[0].name)
    unknown = StmtVal(Type(TypeKind.UNKNOWN), None)
    if name == 'if_statement':
      return self.s_if_statement(cur.children[0])
    elif name == 'while_statement':
      return self.s_while_statement(cur.children[0])
    elif name == 'return_statement':
      return self.s_expression(cur.children[0].children[0])
    elif name == 'comp_statement':
      res = self.s_comp_statement(cur.children[0])
      return res

    elif name == 'expression':
      self.s_expression(cur.children[0])
      return unknown
    elif name == 'empty':
      return unknown
    else:
      raise RuntimeError("Unknown statement")
    raise RuntimeError("Unreached code")

  def s_if_statement(self, cur: Node) -> StmtVal:
    cond = self.s_expression(cur.children[0])
    if cond.type.kind != TypeKind.INT:
      raise RuntimeError(f"[{cur.lineno}]only int could be condition")
    else:
      cond = int(cond.value)
      if cond != 0:
        return self.s_statement(cur.children[1])
      elif len(cur.children) > 2:
        return self.s_statement(cur.children[2])
    return StmtVal(Type(TypeKind.UNKNOWN), None)

  def s_while_statement(self, cur: Node) -> StmtVal:
    cond = self.s_expression(cur.children[0])
    if cond.type.kind != TypeKind.INT:
      raise RuntimeError(f"[{cur.lineno}]only int could be condition")
    else:
      cond = int(cond.value)
      if cond == 0:
        return StmtVal(Type(TypeKind.UNKNOWN), None)
      else:
        self.s_statement(cur.children[1])
        # 需要重新计算condition
        return self.s_while_statement(cur)
    raise RuntimeError("Unreached code")

  def s_comp_statement(self, cur: Node) -> StmtVal:
    self.running_symbol_table.openScope()
    res = self.s_statement_list(cur.children[0])
    self.running_symbol_table.closeScope()
    return res

  def comp_exp(self, children: List[Node], grammar: str):
    exp_list = grammar.split(' ')
    if len(children) != len(exp_list):
      return False
    for i in range(len(children)):
      # TODO: 更改lex.py 从而可以确保类型是Node, 从而可以去除下面这行
      if isinstance(children[i], str) and children[i] != exp_list[i]:
        return False
      if isinstance(children[i], Node) and children[i].name != exp_list[i]:
        return False
    return True

  def s_expression(self, cur: Node) -> StmtVal:
    if self.comp_exp(cur.children, 'TYPE ID = expression'):
      t = Type.str2type(str(cur.children[0].value))
      id = str(cur.children[1].value)
      val = self.s_expression(cur.children[3])
      if val.type.kind == TypeKind.UNKNOWN or val.type.kind == TypeKind.ANY:
        # transfer type
        val.type = t
        val.value = Type.trans_to(val.value, t)
      elif t.kind != val.type.kind:
        raise RuntimeError(f"[{cur.lineno}]type mismatch")
      syb = Symbol(id, Record(t, val.value))
      self.running_symbol_table.insert(syb)
      return val
    elif self.comp_exp(cur.children, 'ID = expression'):
      syb = self.running_symbol_table.get_symbol(str(cur.children[0].value))
      val = self.s_expression(cur.children[2])
      if syb.record.value.type.kind != val.type.kind:
        raise RuntimeError(f"[{cur.lineno}]type mismatch")
      syb.record.value = val.value
      return val
    elif self.comp_exp(cur.children, 'expression + expression') or \
        self.comp_exp(cur.children, 'expression - expression') or \
        self.comp_exp(cur.children, 'expression * expression') or \
        self.comp_exp(cur.children, 'expression / expression') :
      left = self.s_expression(cur.children[0])
      right = self.s_expression(cur.children[2])
      if left.type.kind != right.type.kind:
        raise RuntimeError(f"[{cur.lineno}]type mismatch")
      if left.type.kind != TypeKind.INT and left.type.kind != TypeKind.FLOAT:
        raise RuntimeError(
            f"[{cur.lineno}]only int or float could be calculated")
      lval = 0
      rval = 0
      if left.type.kind == TypeKind.INT:
        lval = int(left.value)
        rval = int(right.value)
      else:
        lval = float(left.value)
        rval = float(right.value)
      op = ''
      # TODO: 更改lex.py 从而可以确保类型是Node, 从而可以去除下面这行
      if isinstance(cur.children[1], Node):
        op = str(cur.children[1].value)
      else:
        op = str(cur.children[1])
      res = 0
      if op == '+':
        res = lval + rval
      elif op == '-':
        res = lval - rval
      elif op == '*':
        res = lval * rval
      elif op == '/':
        res = lval / rval
      if isinstance(res, bool):
        return StmtVal(Type(TypeKind.INT), int(res))
      elif left.type.kind == TypeKind.INT:
        return StmtVal(left.type, int(res))
      elif left.type.kind == TypeKind.FLOAT:
        return StmtVal(left.type, float(res))
    elif self.comp_exp(cur.children, 'expression RELOP expression'):
      op = ''
      # TODO: 更改lex.py 从而可以确保类型是Node, 从而可以去除下面这行
      if isinstance(cur.children[1], Node):
        op = str(cur.children[1].value)
      else:
        op = str(cur.children[1])
      left = self.s_expression(cur.children[0])
      right = self.s_expression(cur.children[2])
      res = 0
      lval = left.value
      rval = right.value
      if op == '>':
        res = lval > rval
      elif op == '<':
        res = lval < rval
      elif op == '>=':
        res = lval >= rval
      elif op == '<=':
        res = lval <= rval
      elif op == '==':
        res = lval == rval
      elif op == '!=':
        res = lval != rval
      return StmtVal(Type(TypeKind.INT), int(res))
    elif self.comp_exp(cur.children, 'expression && expression') or \
        self.comp_exp(cur.children, 'expression || expression'):
      left = self.s_expression(cur.children[0])
      right = self.s_expression(cur.children[2])
      if left.type.kind != right.type.kind:
        raise RuntimeError(f"[{cur.lineno}]type mismatch")
      if left.type.kind != TypeKind.INT:
        raise RuntimeError(f"[{cur.lineno}]only int could be condition")
      lval = int(left.value)
      rval = int(right.value)
      op = ''
      # TODO: 更改lex.py 从而可以确保类型是Node, 从而可以去除下面这行
      if isinstance(cur.children[1], Node):
        op = str(cur.children[1].value)
      else:
        op = str(cur.children[1])

      res = 0
      if op == '&&':
        res = lval and rval
      elif op == '||':
        res = lval or rval
      return StmtVal(Type(TypeKind.INT), int(res))
    elif self.comp_exp(cur.children, 'expression = expression'):
      # most used to json
      id = self.is_left_val(cur.children[0])
      if len(id) == 0:
        raise RuntimeError(f"[{cur.lineno}]type mismatch")
      val1 = self.s_expression(cur.children[0])
      val2 = self.s_expression(cur.children[2])
      if val1.type.kind != TypeKind.ANY and val1.type.kind != val2.type.kind:
        raise RuntimeError(f"[{cur.lineno}]type mismatch")
      syb = self.running_symbol_table.get_symbol(id[0])
      # set syb.record.value.id[1].id[2]...id[-1] = val2.value
      value = syb.record.value
      for i in range(1, len(id) - 1):
        value = value.get(id[i])
      value[id[-1]] = val2.value
      return val2
    elif self.comp_exp(cur.children, '( expression )'):
      return self.s_expression(cur.children[1])
    elif self.comp_exp(cur.children, '! expression'):
      val = self.s_expression(cur.children[1])
      if val.type.kind != TypeKind.INT:
        raise RuntimeError(f"[{cur.lineno}]only int could be condition")
      return StmtVal(Type(TypeKind.INT), int(not val.value))
    elif self.comp_exp(cur.children, '- expression'):
      val = self.s_expression(cur.children[1])
      if val.type.kind != TypeKind.INT and val.type.kind != TypeKind.FLOAT:
        raise RuntimeError(
            f"[{cur.lineno}]only int or float could be calculated")
      if val.type.kind == TypeKind.INT:
        return StmtVal(val.type, -int(val.value))
      elif val.type.kind == TypeKind.FLOAT:
        return StmtVal(val.type, -float(val.value))
    elif self.comp_exp(cur.children, 'ID ( )') or \
      self.comp_exp(cur.children, 'ID ( args )'):
      id = str(cur.children[0].value)
      args = []
      if len(cur.children) > 3:
        args = self.s_args(cur.children[2])
      return self.exec_func(id, args)
    elif self.comp_exp(cur.children, 'expression . ID'):
      # now only for json
      data = self.s_expression(cur.children[0])
      if data.type.kind != TypeKind.JSON:
        raise RuntimeError("only json could be accessed by .")
      id = str(cur.children[2].value)
      value = data.value.get(id)
      return StmtVal(Type(TypeKind.ANY), value)
    elif self.comp_exp(cur.children, 'ID'):
      syb = self.running_symbol_table.get_symbol(str(cur.children[0].value))
      return StmtVal(syb.record.type, syb.record.value)
    elif self.comp_exp(cur.children, 'INT'):
      if cur.children[0].value is None:
        raise RuntimeError(f"[{cur.lineno}]int value is None")
      return StmtVal(Type(TypeKind.INT), int(cur.children[0].value))
    elif self.comp_exp(cur.children, 'FLOAT'):
      if cur.children[0].value is None:
        raise RuntimeError(f"[{cur.lineno}]float value is None")
      return StmtVal(Type(TypeKind.FLOAT), float(cur.children[0].value))
    elif self.comp_exp(cur.children, 'STRING'):
      if cur.children[0].value is None:
        raise RuntimeError(f"[{cur.lineno}]string value is None")
      res = str(cur.children[0].value)
      res = self.format_string(res)
      return StmtVal(Type(TypeKind.STRING), res)
    elif self.comp_exp(cur.children, 'json'):
      return self.s_json(cur.children[0])
    raise RuntimeError("Unreached code")

  def s_json(self, cur: Node) -> StmtVal:
    data = dict()
    self.s_json_list(cur.children[0], data)
    return StmtVal(Type(TypeKind.JSON), data)

  def s_json_list(self, cur: Node, data: Dict):
    self.s_json_pair(cur.children[0], data)
    if len(cur.children) > 1:
      self.s_json_list(cur.children[1], data)

  def s_json_pair(self, cur: Node, data: Dict):
    k: str = str(cur.children[0].value)
    val = self.s_expression(cur.children[1])
    data[k] = val.value

  def s_args(self, cur: Node) -> List[StmtVal]:
    res = list()
    if len(cur.children) > 1:
      res += self.s_args(cur.children[1])
    res.append(self.s_expression(cur.children[0]))
    return res

  def get_entry_point(self, id: str):
    syb = self.global_symbols_table.get_symbol(id)
    info: GlobalInfo = syb.record.value
    return info.entry_point

  def run_event(self, id):
    cur = self.get_entry_point(id)
    self.running_symbol_table.openScope()
    self.state = RunState.RUNNING
    try:
      self.s_statement_list(cur)
    except Exception as e:
      print(f"Error: {e} when running event {id}")
    self.state = RunState.WAIT
    self.running_symbol_table.closeScope()

  def is_left_val(self, cur: Node) -> List[str]:
    '''
    return id
    '''
    res = []
    if cur.name == 'ID':
      res.append(str(cur.value))
      return res
    if cur.children[0].value == 'ID':
      res.append(str(cur.children[0].value))
      return res
    if cur.type == NodeType.NOT_TOKEN:
      if len(cur.children) == 1:
        return self.is_left_val(cur.children[0])
      # if cur.children[0].value == 'expression':
      # TODO: 支持更多左值类型
      elif len(cur.children) == 3:
        if cur.children[1] == '.':
          l = self.is_left_val(cur.children[0])
          r = self.is_left_val(cur.children[2])
          if len(r) != 1:
            raise RuntimeError("Unknow left value")
          return l + r
    return res

  def exec_func(self, func_name: str, args: List[StmtVal]) -> StmtVal:
    if self.is_builtin_func(func_name):
      return self.run_builtin_func(func_name, args)
    syb = self.global_symbols_table.get_symbol(func_name)
    if syb.record.type.kind != TypeKind.FUNCTION:
      raise RuntimeError(f"{func_name} is not callable")
    if syb.record.type.function is None:
      raise RuntimeError(f"function{func_name} is not defined")
    # comp args
    params = syb.record.type.function.params
    info: GlobalInfo = syb.record.value
    entry_point = info.entry_point
    if len(args) != len(params):
      raise RuntimeError(f"args is not right in {func_name} call produce")
    self.running_symbol_table.openScope()
    for i in range(len(args)):
      t, name = params[i]
      if args[i].type.kind != t.kind:
        raise RuntimeError(f"args type is not matched in func {func_name}")
      rec = Record(args[i].type, args[i].value)
      arg_syb = Symbol(name, rec)
      self.running_symbol_table.insert(arg_syb)
    res = self.s_comp_statement(entry_point)
    self.running_symbol_table.closeScope()
    return res

  def is_builtin_func(self, func_name: str) -> bool:
    return func_name in ["print", "get", "hget", "hpost", "exit", "quit"]

  def run_builtin_func(self, func_name: str, args: List[StmtVal]) -> StmtVal:
    if func_name == 'print':
      output = ""
      for arg in args:
        output += str(arg.value)
      print(output)
      return StmtVal(Type(TypeKind.VOID), None)
    elif func_name == 'get':
      txt = ""
      if len(args) == 1:
        txt = args[0].value
      else:
        raise RuntimeError("get func just need no more than 1 param")
      query = input(txt)
      return StmtVal(Type(TypeKind.UNKNOWN), query)
    elif func_name == 'hget':
      if len(args) != 1:
        raise RuntimeError("hget need 1 param")
      try:
        res = request.urlopen(args[0].value)
        data = res.read()
        data = data.decode('utf-8')
        # convert to dict(json)
        data = json.loads(data)
        return StmtVal(Type(TypeKind.JSON), data)
      except Exception as e:
        print(f"HTTP GET ERROR {e}")
        return StmtVal(Type(TypeKind.ERROR), None)
    elif func_name == 'hpost':
      if len(args) != 2:
        raise RuntimeError("hpost func need 2 params")
      url: str = args[0].value
      data = args[1].value
      if not isinstance(data, Dict):
        raise RuntimeError("hpost data must be json")
      try:
        res = requests.post(url, json=data)
        data = res.json()
        return StmtVal(Type(TypeKind.JSON), data)
      except Exception as e:
        print(f"HTTP POST ERROR {e}")
        return StmtVal(Type(TypeKind.ERROR), None)
    elif func_name in ["exit", "quit"]:
      self.end()
      raise RuntimeError("Unreached code")
    raise RuntimeError("Unreached code")

  def format_string(self, val: str) -> str:
    import re
    res = val
    # 处理转义字符
    res = res.replace(r'\n', '\n')
    res = res.replace(r'\t', '\t')
    res = res.replace(r'\r', '\r')
    res = res.replace(r'\b', '\b')
    res = res.replace(r'\f', '\f')
    res = res.replace(r'\\', '\\')
    res = res.replace(r'\"', '\"')
    res = res.replace(r'\'', '\'')

    # 将 ${id} 替换为 id 的值
    def replacer(match):
      var_name = match.group(1)
      return str(self.running_symbol_table.get_symbol(var_name).record.value)

    pattern = re.compile(r'\$\{([a-zA-Z_][a-zA-Z_0-9]*)\}')
    res = pattern.sub(replacer, res)
    return res
