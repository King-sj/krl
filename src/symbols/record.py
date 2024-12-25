from .type import Type
from dataclasses import dataclass
from typing import Any

@dataclass
class Record:
  """
A data class representing a record with a type and an optional value.

Attributes:
  type (Type): The type of the record.
  value (Any, optional): The value of the record. Defaults to None.
"""
  type: Type
  value: Any = None
  # lineno: int = 0