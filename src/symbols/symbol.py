from dataclasses import dataclass
from .record import Record
from typing import Optional
@dataclass
class Symbol:
  name: str
  record: 'Record'
  next: int = -1
