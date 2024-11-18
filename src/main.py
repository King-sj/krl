from lex import lexer
from parser import parser

with open(r"C:\Users\21756\Desktop\krl\examples\eq.krl", "r") as f:
  data = f.read()
  parser.parse(data)

from parser import root
root.print_ast()
