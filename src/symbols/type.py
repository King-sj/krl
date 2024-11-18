from enum import Enum
from dataclasses import dataclass
from typing import List, Union, Tuple
class TypeKind(Enum):
  ERROR = -1
  VOID = 0
  INT = 1
  FLOAT = 2
  STRING = 3
  JSON = 4
  FUNCTION = 5
  EVENT = 6

@dataclass
class Function:
  returnType: 'Type'
  params: List[Tuple['Type', str]]

@dataclass
class Type:
  kind: TypeKind
  function: Union[None, 'Function'] = None

