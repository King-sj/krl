from symbols import *
from node import *
from dataclasses import dataclass


@dataclass
class GlobalInfo:
  entry_point: Node
  # more info maybe need in future


def init_global_symbols(st: StackListSymbolTable, root: Node):
  st.openScope()
  s_program(root, st)


def s_program(cur: Node, st: StackListSymbolTable):
  s_program_part_list(cur.children[0], st)


def s_program_part_list(cur: Node, st: StackListSymbolTable):
  s_program_part(cur.children[0], st)
  if (len(cur.children) > 1):
    s_program_part_list(cur.children[1], st)


def s_program_part(cur: Node, st: StackListSymbolTable):
  if cur.children[0].name == 'function':
    s_function(cur.children[0], st)
  elif cur.children[0].name == 'event':
    s_event(cur.children[0], st)


def s_event(cur: Node, st: StackListSymbolTable):
  value = GlobalInfo(cur.children[1])
  name = str(cur.children[0].value).strip('"')

  rec = Record(Type(TypeKind.EVENT), value)
  symbol = Symbol(name, rec)
  st.insert(symbol)


def s_function(cur: Node, st: StackListSymbolTable):
  name = str(cur.children[0].value)
  value = GlobalInfo(cur.children[2])
  params = []
  if cur.children[1].name != 'NULL':
    params = s_var_list(cur.children[1])
  func = Function(Type(TypeKind.UNKNOWN), params)
  rec = Record(Type(TypeKind.FUNCTION, func), value)
  symbol = Symbol(name, rec)
  st.insert(symbol)


def s_var_list(cur: Node):
  var_list: List[Tuple[Type, str]] = []
  type_name = str(cur.children[0].value)
  id_name = str(cur.children[1].value)
  var_list.append((Type.str2type(type_name),id_name))
  if (len(cur.children) > 2):
    var_list += s_var_list(cur.children[2])
  return var_list
