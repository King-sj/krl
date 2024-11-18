reserved = {
    'event': 'EVENT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
}
tokens = [
    'TYPE',
    'ID',
    "AND",
    "OR",
    "NOT",
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMI',
    'RELOP',
    'ASSIGN',
    'COMMA',
    'COLON',
    # 'MOD',
    'DOT',
    'STRING',
    'INT',
    'FLOAT'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_ASSIGN = r'='
# t_PIPE = r'\|'
t_COMMA = r','
# t_LBRACKET = r'\['
# t_RBRACKET = r'\]'
t_COLON = r':'
# t_MOD = r'%'
t_DOT = r'\.'

digit = r'([0-9])'
nondigit = r'([_A-Za-z])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

# Regular expression rules for simple tokens

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_RELOP = r'==|!=|<=|>=|<|>'

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
