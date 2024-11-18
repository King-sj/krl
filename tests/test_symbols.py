from src.symbols import *

def test_base():
  table = StackListSymbolTable()
  table.openScope()
  table.closeScope()

  table.openScope()
  table.openScope()
  table.closeScope()
  table.closeScope()

def test_symboltable():
  table = StackListSymbolTable()
  #
  table.openScope()
  rec1 = Record(Type(TypeKind.INT), 1)
  symb1 = Symbol("a", rec1)
  table.insert(symb1)
  assert table.find("a") == 0
  rec2 = Record(Type(TypeKind.FLOAT), 2.0)
  symb2 = Symbol("b", rec2)
  table.insert(symb2)
  assert table.find("b") == 1
  ##
  table.openScope()
  rec3 = Record(Type(TypeKind.STRING), "fsd")
  symb3 = Symbol("a", rec3)
  table.insert(symb3)
  assert table.find("a") == 2
  #
  table.closeScope()
  assert table.find("a") == 0

  table.closeScope()
  assert table.find("a") == -1
