# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
from config.lex_config import *
from node import Node,NodeType

def t_COMMENT(t):
  r'\#.*'
  pass

def t_TYPE(t):
  r'(int|float|string|json)'
  t.value = Node(NodeType.TOKEN,'TYPE',t.value)
  t.value.set_pos((t.lexer.lineno, t.lexer.lexpos))
  return t
def t_RELOP(t):
  r'==|!=|<=|>=|<|>'
  t.value = Node(NodeType.TOKEN,'RELOP',t.value)
  t.value.set_pos((t.lexer.lineno, t.lexer.lexpos))
  return t
@lex.TOKEN(identifier)
def t_ID(t):
  # r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'ID')
  t.value = Node(NodeType.TOKEN,'ID',t.value)
  t.value.set_pos((t.lexer.lineno, t.lexer.lexpos))
  return t


# A regular expression rule with some action code
def t_INT(t):
  r'\d+'
  t.value = int(t.value)
  t.value = Node(NodeType.INT,'INT',t.value)
  t.value.set_pos((t.lexer.lineno, t.lexer.lexpos))
  return t
def t_FLOAT(t):
  r'\d+\.\d+'
  t.value = float(t.value)
  t.value = Node(NodeType.FLOAT,'FLOAT',t.value)
  t.value.set_pos((t.lexer.lineno, t.lexer.lexpos))
  return t
def t_STRING(t):
  r'".*"'
  t.value = t.value[1:-1]
  t.value = Node(NodeType.STRING,'STRING',t.value)
  t.value.set_pos((t.lexer.lineno, t.lexer.lexpos))
  return t

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  # t.lexer.lexpos = 0
  t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
  print(f"{t.lexer.lineno} : Illegal character {t.value[0]}")
  t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
