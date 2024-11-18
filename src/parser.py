# Yacc example

import ply.yacc as yacc
from lex import tokens
from node import Node, NodeType

precedence = (
    # ('nonassoc', 'LESSTHAN', 'GREATERTHAN'),  # Nonassociative operators
    ('right', 'ASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'RELOP'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
    ('left', 'DOT'),
    ('left', 'LPAREN', 'RPAREN'),
    ('nonassoc', 'ELSE'),
)

root = None


def p_program(p):
  'program : program_part_list'
  p[0] = Node(NodeType.NOT_TOKEN, "program", None, [p[1]])
  global root
  root = p[0]

def p_empty(p):
  'empty :'
  p[0] = Node(NodeType.NOT_TOKEN, "empty", None, [])

def p_program_part_list(p):
  '''program_part_list : program_part
                       | program_part program_part_list'''
  if len(p) == 2:
    p[0] = Node(NodeType.NOT_TOKEN, "program_part_list", None, [p[1]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "program_part_list", None, [p[1], p[2]])


def p_program_part(p):
  '''program_part : event_list
                  | function_list'''
  p[0] = Node(NodeType.NOT_TOKEN, "program_part", None, [p[1]])


def p_event_list(p):
  '''event_list : event
                | event_list event'''
  if len(p) == 2:
    p[0] = Node(NodeType.NOT_TOKEN, "event_list", None, [p[1]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "event_list", None, [p[1], p[2]])


def p_event(p):
  '''event : EVENT STRING LBRACE statement_list RBRACE'''
  p[0] = Node(NodeType.NOT_TOKEN, "event", None, [p[2], p[4]])


def p_statement_list(p):
  '''statement_list : statement
                    | statement_list statement'''
  if len(p) == 2:
    p[0] = Node(NodeType.NOT_TOKEN, "statement_list", None, [p[1]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "statement_list", None, [p[1], p[2]])


def p_statement(p):
  '''statement : if_statement
               | while_statement
               | return_statement
               | comp_statement
               | expression SEMI
               | empty
  '''
  if len(p) == 2:
    p[0] = Node(NodeType.NOT_TOKEN, "statement", None, [p[1]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "statement", None, [p[1], p[2]])

def p_if_statement(p):
  '''if_statement : IF LPAREN expression RPAREN statement
                  | IF LPAREN expression RPAREN statement ELSE statement
  '''
  if len(p) == 6:
    p[0] = Node(NodeType.NOT_TOKEN, "if_statement", None, [p[3], p[5]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "if_statement", None, [p[3], p[5], p[7]])


def p_while_statement(p):
  '''while_statement : WHILE LPAREN expression RPAREN statement'''
  p[0] = Node(NodeType.NOT_TOKEN, "while_statement", None, [p[3], p[5]])


def p_return_statement(p):
  '''return_statement : RETURN expression SEMI'''
  p[0] = Node(NodeType.NOT_TOKEN, "return_statement", None, [p[2]])


def p_comp_statement(p):
  '''comp_statement : LBRACE statement_list RBRACE'''
  p[0] = Node(NodeType.NOT_TOKEN, "comp_statement", None, [p[2]])


def p_expression(p):
  '''expression : TYPE ID ASSIGN expression
                | ID ASSIGN expression
                | expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression
                | expression RELOP expression
                | expression AND expression
                | expression OR expression
                | expression ASSIGN expression
                | LPAREN expression RPAREN
                | NOT expression
                | MINUS expression
                | ID LPAREN RPAREN
                | ID LPAREN args RPAREN
                | expression DOT ID
                | ID
                | INT
                | FLOAT
                | STRING
                | json
  '''
  if len(p) == 2:
    p[0] = Node(NodeType.NOT_TOKEN, "expression", None, [p[1]])
  elif len(p) == 3:
    p[0] = Node(NodeType.NOT_TOKEN, "expression", None, [p[1], p[2]])
  elif len(p) == 4:
    p[0] = Node(NodeType.NOT_TOKEN, "expression", None, [p[2]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "expression", None, [p[1], p[3], p[2]])


def p_args(p):
  '''args : expression
          | args COMMA expression'''
  if len(p) == 2:
    p[0] = Node(NodeType.NOT_TOKEN, "args", None, [p[1]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "args", None, [p[1], p[3]])


def p_json(p):
  '''json : LBRACE json_list RBRACE'''
  p[0] = Node(NodeType.NOT_TOKEN, "json", None, [p[2]])


def p_json_list(p):
  '''json_list : json_pair
               | json_pair COMMA json_list'''
  if len(p) == 2:
    p[0] = Node(NodeType.NOT_TOKEN, "json_list", None, [p[1]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "json_list", None, [p[1], p[3]])


def p_json_pair(p):
  '''json_pair : STRING COLON expression'''
  p[0] = Node(NodeType.NOT_TOKEN, "json_pair", None, [p[1], p[3]])


def p_function_list(p):
  '''function_list : ID LPAREN RPAREN comp_statement
                   | ID LPAREN var_list RPAREN comp_statement
  '''
  if len(p) == 5:
    p[0] = Node(NodeType.NOT_TOKEN, "function_list", None, [p[1], p[4]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "function_list", None, [p[1], p[3], p[5]])


def p_var_list(p):
  '''var_list : TYPE ID
              | var_list COMMA TYPE ID
  '''
  if len(p) == 3:
    p[0] = Node(NodeType.NOT_TOKEN, "var_list", None, [p[1], p[2]])
  else:
    p[0] = Node(NodeType.NOT_TOKEN, "var_list", None, [p[1], p[3], p[4]])


# Error rule for syntax errors
# def p_error(p):
#   print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
