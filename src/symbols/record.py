from .type import Type
from dataclasses import dataclass
from typing import Any

@dataclass
class Record:
  type: Type
  value: Any = None
  # lineno: int = 0