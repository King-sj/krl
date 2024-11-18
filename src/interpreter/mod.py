from node import Node
from symbols import *
from .global_symbols_utils import init_global_symbols
class Interpreter:
  def __init__(self, ast_root:Node) -> None:
    self.root = ast_root
    # 存储所有 event, function 的必要信息（重入点
    self.global_symbols_table = StackListSymbolTable()
    # 运行时所用的符号表
    self.running_symbol_table = StackListSymbolTable()

    init_global_symbols(self.global_symbols_table,ast_root)
