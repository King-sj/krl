from typing import List,Dict
from .symbol import Symbol
from .error import *
from utils import *
from .record import Record
from .type import Type, TypeKind
import warnings
class StackListSymbolTable:

  def __init__(self):
    self.blockIndexTable: List[int] = []
    self.symbolTable: List[Symbol] = []
    self.top = 0
    self.hashTable: Dict[int, int] = {}
    self.blockIndex = -1
    # add watch dog
    # self.symbolTable.append(Symbol("^^watch_dog$$", Record(Type(TypeKind.VOID), None)))
  def openScope(self):
    self.blockIndex += 1
    self.blockIndexTable.append(self.top)

  def closeScope(self):
    if self.blockIndex < 0:
      raise RuntimeError("Unreached Code")
    while self.top > self.blockIndexTable[self.blockIndex]:
      if -1 == self.pop():
        break
    self.blockIndex -= 1
    self.blockIndexTable.pop()


  def find(self, name: str) -> int:
    """
    Find the symbol idx at symbolTable in the nearest scope.
    """
    idx = hash(name)
    if idx not in self.hashTable:
      return -1
    pos = self.hashTable[idx]
    while pos != -1:
      if self.symbolTable[pos].name == name:
        return pos
      pos = self.symbolTable[pos].next
    return -1

  def insert(self, symbol: Symbol):
    idx = hash(symbol.name)
    if idx in self.hashTable:
      pos = self.find(symbol.name)
      if pos >= self.blockIndexTable[self.blockIndex]:
        raise SymbolInvalidError(symbol.name)
    else:
      self.hashTable[idx] = -1
    symbol.next = self.hashTable[idx]
    self.hashTable[idx] = self.top
    self.symbolTable.append(symbol) # self.symbolTable[self.top] = symbol
    self.top += 1
    return self.top - 1

  def get(self, idx: int) -> Symbol:
    return self.symbolTable[idx]

  def pop(self):
    if self.top == 0:
      warnings.warn("Unreached Code")
      return -1
    symbol = self.get(self.top-1)
    idx = hash(symbol.name)
    self.hashTable[idx] = symbol.next
    self.symbolTable.pop()
    self.top -= 1
    return self.top
  def get_symbol(self, name:str):
    idx = self.find(name)
    if idx == -1:
      raise SymbolNotFoundError(f'Not Found Symbol f{name}')
    return self.symbolTable[idx]