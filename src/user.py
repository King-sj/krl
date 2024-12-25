from interpreter import Interpreter
from uuid import UUID,uuid4
from threading import Thread
class User:
  '''
  A user is a person who is using the KRL language.
  '''
  def __init__(self, interpreter:Interpreter):
    self.interpreter = interpreter
    self.id:UUID = User.gen_user_id()
    self.thread:None|Thread = None
  @staticmethod
  def gen_user_id():
    return uuid4()