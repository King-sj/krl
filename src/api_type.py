from typing import TypedDict
class Response(TypedDict):
  """
  Response TypedDict

  Attributes:
    res (str): The response message.
    code (int): The error code.
    msg (str): The error message.
  """
  res: str # 返回信息
  code: int # 错误码
  msg: str # 错误信息

class UserInput(TypedDict):
  user_id: str # 用户ID
  input: str # 用户输入数据
