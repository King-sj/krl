from typing import List,Dict
from .symbol import Symbol
from .error import *
from utils import *
from .record import Record
from .type import Type, TypeKind
import warnings
class StackListSymbolTable:
  """
  A symbol table that supports nested scopes using a stack-based approach.
  Attributes:
    blockIndexTable (List[int]): A list to keep track of the starting index of each scope.
    symbolTable (List[Symbol]): A list to store symbols.
    top (int): The current top index of the symbol table.
    hashTable (Dict[int, int]): A dictionary to map symbol names to their indices in the symbol table.
    blockIndex (int): The current scope level.
  Methods:
    openScope():
      Opens a new scope by incrementing the block index and storing the current top index.
    closeScope():
      Closes the current scope by popping symbols until the scope's starting index is reached.
    find(name: str) -> int:
      Finds the index of a symbol in the nearest scope by its name.
    insert(symbol: Symbol) -> int:
      Inserts a new symbol into the symbol table and returns its index.
    get(idx: int) -> Symbol:
      Retrieves a symbol from the symbol table by its index.
    pop() -> int:
      Removes the top symbol from the symbol table and returns the new top index.
    get_symbol(name: str) -> Symbol:
      Retrieves a symbol from the symbol table by its name.
  """
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
      raise SymbolNotFoundError(f'Not Found Symbol {name}')
    return self.symbolTable[idx]