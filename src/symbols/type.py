from enum import Enum
from dataclasses import dataclass
from typing import List, Union, Tuple,Any


class TypeKind(Enum):
  ERROR = -1
  VOID = 0
  INT = 1
  FLOAT = 2
  STRING = 3
  JSON = 4
  FUNCTION = 5
  EVENT = 6
  UNKNOWN = 7
  ANY = 8


@dataclass
class Function:
  returnType: 'Type'
  params: List[Tuple['Type', str]]


class Type:
  """
  A class to represent a type in the system.
  Attributes:
  ----------
  kind : TypeKind
    The kind of the type (e.g., INT, FLOAT, STRING, JSON).
  function : Union[None, 'Function']
    An optional function associated with the type.
  Methods:
  -------
  str2type(typename: str) -> 'Type':
    Converts a string representation of a type to a Type object.
  trans_to(value: Any, type: 'Type') -> Any:
    Transforms a value to the specified type.
  """
  def __init__(self,
               kind: TypeKind,
               function: Union[None, 'Function'] = None) -> None:
    self.kind = kind
    self.function = function
  @staticmethod
  def str2type(typename:str):
    if typename == 'int':
      return Type(TypeKind.INT)
    elif typename == 'float':
      return Type(TypeKind.FLOAT)
    elif typename == 'string':
      return Type(TypeKind.STRING)
    elif typename == 'json':
      return Type(TypeKind.JSON)
    else:
      raise RuntimeError(f"Unknown Type {typename}")
  @staticmethod
  def trans_to(value:Any, type:'Type') -> Any:
    if type.kind == TypeKind.INT:
      return int(value)
    elif type.kind == TypeKind.FLOAT:
      return float(value)
    elif type.kind == TypeKind.STRING:
      return str(value)
    elif type.kind == TypeKind.JSON:
      return value
    else:
      raise RuntimeError(f"Unknown Type {type.kind}")