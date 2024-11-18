from enum import Enum
from typing import List


class NodeType(Enum):
  ERROR = -1
  VOID = 0
  INT = 1
  FLOAT = 2
  STRING = 3
  JSON = 4
  TOKEN = 5  # normal token, 终结符
  NOT_TOKEN = 6  # 非终结符


class Node:

  def __init__(self,
               type: NodeType,
               name: str | None = None,
               value=None,
               children: List['Node'] = []):
    self.type = type
    self.name = name
    self.value = value
    self.children = children

  def print_ast(self, indent=0):
    print(' ' * indent + (self.name if self.name is not None else '') +
          (f':{self.value}' if self.value else ''))
    for child in self.children:
      if child is None:
        print(' ' * indent + 'None')
        continue
      if isinstance(child, Node):
        child.print_ast(indent + 2)
      else:
        print(' ' * indent + f'type:{type(child)} {child}')
