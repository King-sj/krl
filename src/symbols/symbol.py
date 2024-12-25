from dataclasses import dataclass
from .record import Record
from typing import Optional
@dataclass
class Symbol:
  """
A class used to represent a Symbol.

Attributes
----------
name : str
  The name of the symbol.
record : Record
  The record associated with the symbol.
next : int, optional
  The index of the next symbol (default is -1).
"""
  name: str
  record: 'Record'
  next: int = -1
