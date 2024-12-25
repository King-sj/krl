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
  """
  A class representing a node in an abstract syntax tree (AST).
  Attributes:
    type (NodeType): The type of the node.
    name (str | None): The name of the node. Defaults to None.
    value: The value of the node. Defaults to None.
    children (List['Node']): The children of the node. Defaults to an empty list.
    lineno (int): The line number of the node in the source code. Defaults to -1.
    lexpos (int): The position of the node in the source code. Defaults to -1.
  Methods:
    set_pos(pos: tuple[int, int]):
      Sets the position of the node in the source code.
    print_ast(indent=0):
      Prints the abstract syntax tree starting from this node.
    create_none() -> 'Node':
      Creates a node representing a 'None' value.
  """

  def __init__(self,
               type: NodeType,
               name: str | None = None,
               value=None,
               children: List['Node'] = []):
    self.type = type
    self.name = name
    self.value = value
    self.children = children
    self.lineno = -1
    self.lexpos = -1

  def set_pos(self, pos: tuple[int, int]):
    l, c = pos
    self.lineno = l
    self.lexpos = c

  def print_ast(self, indent=0):
    print(' ' * indent + (self.name if self.name is not None else '') +
          (f':{self.value}' if self.value else '') + f' [{self.lineno}]')
    for child in self.children:
      if child is None:
        print(' ' * (indent + 2) + 'None')
        continue
      if isinstance(child, Node):
        child.print_ast(indent + 2)
      else:
        print(' ' * (indent + 2) + f'{type(child)} {child}')
  @staticmethod
  def create_none():
    obj = Node(NodeType.VOID, 'NULL')
    return obj