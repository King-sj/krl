from typing import TypedDict
class Response(TypedDict):
  res: str # 返回信息
  code: int # 错误码
  msg: str # 错误信息

class UserInput(TypedDict):
  user_id: str # 用户ID
  input: str # 用户输入数据
