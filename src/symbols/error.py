import inspect

# 自定义错误类型
class SymbolError(Exception):

  def __init__(self, message: str):
    super().__init__(message)
    self.message = message

  def __str__(self):
    frame = inspect.currentframe()
    if frame:
        frame = frame.f_back
    lineno = frame.f_lineno if frame else 'unknown'
    filename = frame.f_code.co_filename if frame else 'unknown'
    return f"[{filename}][{lineno}] SymbolError: {self.message}"


# 特殊化错误类型
class SymbolNotFoundError(SymbolError):

  def __init__(self, symbol: str):
    super().__init__(f"Symbol '{symbol}' not found.")
    self.symbol = symbol


class SymbolInvalidError(SymbolError):

  def __init__(self, symbol: str):
    super().__init__(f"Symbol '{symbol}' is invalid.")
    self.symbol = symbol


class SymbolAccessError(SymbolError):

  def __init__(self, symbol: str):
    super().__init__(f"Access to symbol '{symbol}' is denied.")
    self.symbol = symbol

class SymbolTypeError(SymbolError):

  def __init__(self, message: str):
    super().__init__(message)
    self.message = message