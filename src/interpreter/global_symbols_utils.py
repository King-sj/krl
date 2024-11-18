from symbols import *
from node import *
from dataclasses import dataclass
@dataclass
class GlobalInfo:
  entry_point:Node
  # more info maybe need in future


def init_global_symbols(st: StackListSymbolTable, root: Node):
  st.openScope()
  s_program(root,st)


def s_program(cur: Node,st: StackListSymbolTable):
  s_program_part_list(cur.children[0],st)


def s_program_part_list(cur: Node,st: StackListSymbolTable):
  s_program_part(cur.children[0],st)
  if (len(cur.children)>1):
    s_program_part_list(cur.children[1],st)

def s_program_part(cur: Node,st: StackListSymbolTable):
  if cur.children[0].name == 'function_list':
    s_function_list(cur.children[0],st)
  elif cur.children[0].name == 'event_list':
    s_event(cur.children[0],st)

def s_event_list(cur: Node,st: StackListSymbolTable):
  s_event(cur.children[0],st)
  if len(cur.children)>1:
    s_event_list(cur.children[1],st)

def s_event(cur: Node,st: StackListSymbolTable):
  value = GlobalInfo(cur.children[1])
  name = str(cur.children[0].value)
  rec = Record(Type(TypeKind.EVENT),value)
  symbol = Symbol(name,rec)
  st.insert(symbol)

def s_function_list(cur: Node,st: StackListSymbolTable):
  pass