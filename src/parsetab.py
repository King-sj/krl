
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocTOKENrightASSIGNleftORleftANDnonassocRELOPleftPLUSMINUSleftTIMESDIVIDErightNOTrightUMINUSleftDOTleftLPARENRPARENnonassocELSEAND ASSIGN COLON COMMA DIVIDE DOT ELSE EVENT FLOAT ID IF INT LBRACE LPAREN MINUS NOT OR PLUS RBRACE RELOP RETURN RPAREN SEMI STRING TIMES TYPE WHILEprogram : program_part_listempty :program_part_list : program_part\n                       | program_part program_part_listprogram_part : event_list\n                  | function_listevent_list : event\n                | event_list eventevent : EVENT STRING LBRACE statement_list RBRACEstatement_list : statement\n                    | statement_list statementstatement : if_statement\n               | while_statement\n               | return_statement\n               | comp_statement\n               | expression SEMI\n               | empty\n  if_statement : IF LPAREN expression RPAREN statement\n                  | IF LPAREN expression RPAREN statement ELSE statement\n  while_statement : WHILE LPAREN expression RPAREN statementreturn_statement : RETURN expression SEMIcomp_statement : LBRACE statement_list RBRACEexpression : TYPE ID ASSIGN expression\n                | ID ASSIGN expression\n                | expression PLUS expression\n                | expression MINUS expression\n                | expression TIMES expression\n                | expression DIVIDE expression\n                | expression RELOP expression\n                | expression AND expression\n                | expression OR expression\n                | expression ASSIGN expression\n                | LPAREN expression RPAREN\n                | NOT expression\n                | MINUS expression %prec UMINUS\n                | ID LPAREN RPAREN\n                | ID LPAREN args RPAREN\n                | expression DOT ID\n                | ID %prec TOKEN\n                | INT\n                | FLOAT\n                | STRING\n                | json\n  args : expression\n          | args COMMA expressionjson : LBRACE json_list RBRACEjson_list : json_pair\n               | json_pair COMMA json_listjson_pair : STRING COLON expressionfunction_list : ID LPAREN RPAREN comp_statement\n                   | ID LPAREN var_list RPAREN comp_statement\n  var_list : TYPE ID\n              | var_list COMMA TYPE ID\n  '
    
_lr_action_items = {'ID':([0,3,4,5,6,10,15,16,17,18,23,24,25,26,27,28,29,31,33,35,36,38,39,43,44,45,49,50,51,52,53,54,55,56,57,58,59,60,61,64,67,68,71,75,89,90,97,98,101,102,103,105,106,],[7,7,-5,-6,-7,-8,21,37,-50,37,37,37,-10,-12,-13,-14,-15,-17,37,37,66,37,37,37,-51,72,-9,-11,-16,37,37,37,37,37,37,37,37,84,37,37,37,37,-22,37,-21,37,37,37,37,-18,-20,37,-19,]),'EVENT':([0,3,4,5,6,10,17,44,49,71,],[8,8,8,-6,-7,-8,-50,-51,-9,-22,]),'$end':([1,2,3,4,5,6,9,10,17,44,49,71,],[0,-1,-3,-5,-6,-7,-4,-8,-50,-51,-9,-22,]),'LPAREN':([7,16,18,23,24,25,26,27,28,29,31,32,33,34,35,37,38,39,43,50,51,52,53,54,55,56,57,58,59,61,64,67,68,71,75,89,90,97,98,101,102,103,105,106,],[11,33,33,33,33,-10,-12,-13,-14,-15,-17,61,33,64,33,68,33,33,33,-11,-16,33,33,33,33,33,33,33,33,33,33,33,33,-22,33,-21,33,33,33,33,-18,-20,33,-19,]),'STRING':([8,16,18,23,24,25,26,27,28,29,31,33,35,38,39,43,50,51,52,53,54,55,56,57,58,59,61,63,64,67,68,71,74,75,89,90,97,98,101,102,103,105,106,],[12,22,22,48,22,-10,-12,-13,-14,-15,-17,22,22,22,22,22,-11,-16,22,22,22,22,22,22,22,22,22,87,22,22,22,-22,87,22,-21,22,22,22,22,-18,-20,22,-19,]),'RPAREN':([11,14,21,22,37,40,41,42,62,68,69,70,72,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,93,94,99,100,104,],[13,19,-52,-42,-39,-40,-41,-43,86,92,-35,-34,-53,-46,-25,-26,-27,-28,-29,-30,-31,-32,-38,97,-33,98,-24,-36,100,-44,-23,-37,-45,]),'TYPE':([11,16,18,20,23,24,25,26,27,28,29,31,33,35,38,39,43,50,51,52,53,54,55,56,57,58,59,61,64,67,68,71,75,89,90,97,98,101,102,103,105,106,],[15,36,36,45,36,36,-10,-12,-13,-14,-15,-17,36,36,36,36,36,-11,-16,36,36,36,36,36,36,36,36,36,36,36,36,-22,36,-21,36,36,36,36,-18,-20,36,-19,]),'LBRACE':([12,13,16,18,19,23,24,25,26,27,28,29,31,33,35,38,39,43,50,51,52,53,54,55,56,57,58,59,61,64,67,68,71,75,89,90,97,98,101,102,103,105,106,],[16,18,23,23,18,23,23,-10,-12,-13,-14,-15,-17,63,63,63,63,23,-11,-16,63,63,63,63,63,63,63,63,63,63,63,63,-22,63,-21,63,23,23,63,-18,-20,23,-19,]),'COMMA':([14,21,22,37,40,41,42,47,69,70,72,73,76,77,78,79,80,81,82,83,84,86,91,92,93,94,96,99,100,104,],[20,-52,-42,-39,-40,-41,-43,74,-35,-34,-53,-46,-25,-26,-27,-28,-29,-30,-31,-32,-38,-33,-24,-36,101,-44,-49,-23,-37,-45,]),'IF':([16,18,23,24,25,26,27,28,29,31,43,50,51,71,89,97,98,102,103,105,106,],[32,32,32,32,-10,-12,-13,-14,-15,-17,32,-11,-16,-22,-21,32,32,-18,-20,32,-19,]),'WHILE':([16,18,23,24,25,26,27,28,29,31,43,50,51,71,89,97,98,102,103,105,106,],[34,34,34,34,-10,-12,-13,-14,-15,-17,34,-11,-16,-22,-21,34,34,-18,-20,34,-19,]),'RETURN':([16,18,23,24,25,26,27,28,29,31,43,50,51,71,89,97,98,102,103,105,106,],[35,35,35,35,-10,-12,-13,-14,-15,-17,35,-11,-16,-22,-21,35,35,-18,-20,35,-19,]),'NOT':([16,18,23,24,25,26,27,28,29,31,33,35,38,39,43,50,51,52,53,54,55,56,57,58,59,61,64,67,68,71,75,89,90,97,98,101,102,103,105,106,],[39,39,39,39,-10,-12,-13,-14,-15,-17,39,39,39,39,39,-11,-16,39,39,39,39,39,39,39,39,39,39,39,39,-22,39,-21,39,39,39,39,-18,-20,39,-19,]),'MINUS':([16,18,22,23,24,25,26,27,28,29,30,31,33,35,37,38,39,40,41,42,43,48,50,51,52,53,54,55,56,57,58,59,61,62,64,65,67,68,69,70,71,73,75,76,77,78,79,80,81,82,83,84,85,86,88,89,90,91,92,94,96,97,98,99,100,101,102,103,104,105,106,],[38,38,-42,38,38,-10,-12,-13,-14,-15,53,-17,38,38,-39,38,38,-40,-41,-43,38,-42,-11,-16,38,38,38,38,38,38,38,38,38,53,38,53,38,38,-35,-34,-22,-46,38,-25,-26,-27,-28,53,53,53,53,-38,53,-33,53,-21,38,53,-36,53,53,38,38,53,-37,38,-18,-20,53,38,-19,]),'INT':([16,18,23,24,25,26,27,28,29,31,33,35,38,39,43,50,51,52,53,54,55,56,57,58,59,61,64,67,68,71,75,89,90,97,98,101,102,103,105,106,],[40,40,40,40,-10,-12,-13,-14,-15,-17,40,40,40,40,40,-11,-16,40,40,40,40,40,40,40,40,40,40,40,40,-22,40,-21,40,40,40,40,-18,-20,40,-19,]),'FLOAT':([16,18,23,24,25,26,27,28,29,31,33,35,38,39,43,50,51,52,53,54,55,56,57,58,59,61,64,67,68,71,75,89,90,97,98,101,102,103,105,106,],[41,41,41,41,-10,-12,-13,-14,-15,-17,41,41,41,41,41,-11,-16,41,41,41,41,41,41,41,41,41,41,41,41,-22,41,-21,41,41,41,41,-18,-20,41,-19,]),'RBRACE':([16,18,22,23,24,25,26,27,28,29,31,37,40,41,42,43,46,47,50,51,69,70,71,73,76,77,78,79,80,81,82,83,84,86,89,91,92,95,96,97,98,99,100,102,103,105,106,],[-2,-2,-42,-2,49,-10,-12,-13,-14,-15,-17,-39,-40,-41,-43,71,73,-47,-11,-16,-35,-34,-22,-46,-25,-26,-27,-28,-29,-30,-31,-32,-38,-33,-21,-24,-36,-48,-49,-2,-2,-23,-37,-18,-20,-2,-19,]),'SEMI':([22,30,37,40,41,42,48,65,69,70,73,76,77,78,79,80,81,82,83,84,86,91,92,99,100,],[-42,51,-39,-40,-41,-43,-42,89,-35,-34,-46,-25,-26,-27,-28,-29,-30,-31,-32,-38,-33,-24,-36,-23,-37,]),'PLUS':([22,30,37,40,41,42,48,62,65,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,52,-39,-40,-41,-43,-42,52,52,-35,-34,-46,-25,-26,-27,-28,52,52,52,52,-38,52,-33,52,52,-36,52,52,52,-37,52,]),'TIMES':([22,30,37,40,41,42,48,62,65,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,54,-39,-40,-41,-43,-42,54,54,-35,-34,-46,54,54,-27,-28,54,54,54,54,-38,54,-33,54,54,-36,54,54,54,-37,54,]),'DIVIDE':([22,30,37,40,41,42,48,62,65,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,55,-39,-40,-41,-43,-42,55,55,-35,-34,-46,55,55,-27,-28,55,55,55,55,-38,55,-33,55,55,-36,55,55,55,-37,55,]),'RELOP':([22,30,37,40,41,42,48,62,65,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,56,-39,-40,-41,-43,-42,56,56,-35,-34,-46,-25,-26,-27,-28,None,56,56,56,-38,56,-33,56,56,-36,56,56,56,-37,56,]),'AND':([22,30,37,40,41,42,48,62,65,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,57,-39,-40,-41,-43,-42,57,57,-35,-34,-46,-25,-26,-27,-28,-29,-30,57,57,-38,57,-33,57,57,-36,57,57,57,-37,57,]),'OR':([22,30,37,40,41,42,48,62,65,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,58,-39,-40,-41,-43,-42,58,58,-35,-34,-46,-25,-26,-27,-28,-29,-30,-31,58,-38,58,-33,58,58,-36,58,58,58,-37,58,]),'ASSIGN':([22,30,37,40,41,42,48,62,65,66,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,59,67,-40,-41,-43,-42,59,59,90,-35,-34,-46,-25,-26,-27,-28,-29,-30,-31,59,-38,59,-33,59,59,-36,59,59,59,-37,59,]),'DOT':([22,30,37,40,41,42,48,62,65,69,70,73,76,77,78,79,80,81,82,83,84,85,86,88,91,92,94,96,99,100,104,],[-42,60,-39,-40,-41,-43,-42,60,60,60,60,-46,60,60,60,60,60,60,60,60,-38,60,-33,60,60,-36,60,60,60,-37,60,]),'ELSE':([26,27,28,29,31,51,71,89,97,98,102,103,105,106,],[-12,-13,-14,-15,-17,-16,-22,-21,-2,-2,105,-20,-2,-19,]),'COLON':([48,87,],[75,75,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_part_list':([0,3,],[2,9,]),'program_part':([0,3,],[3,3,]),'event_list':([0,3,],[4,4,]),'function_list':([0,3,],[5,5,]),'event':([0,3,4,],[6,6,10,]),'var_list':([11,],[14,]),'comp_statement':([13,16,18,19,23,24,43,97,98,105,],[17,29,29,44,29,29,29,29,29,29,]),'statement_list':([16,18,23,],[24,43,43,]),'statement':([16,18,23,24,43,97,98,105,],[25,25,25,50,50,102,103,106,]),'if_statement':([16,18,23,24,43,97,98,105,],[26,26,26,26,26,26,26,26,]),'while_statement':([16,18,23,24,43,97,98,105,],[27,27,27,27,27,27,27,27,]),'return_statement':([16,18,23,24,43,97,98,105,],[28,28,28,28,28,28,28,28,]),'expression':([16,18,23,24,33,35,38,39,43,52,53,54,55,56,57,58,59,61,64,67,68,75,90,97,98,101,105,],[30,30,30,30,62,65,69,70,30,76,77,78,79,80,81,82,83,85,88,91,94,96,99,30,30,104,30,]),'empty':([16,18,23,24,43,97,98,105,],[31,31,31,31,31,31,31,31,]),'json':([16,18,23,24,33,35,38,39,43,52,53,54,55,56,57,58,59,61,64,67,68,75,90,97,98,101,105,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'json_list':([23,63,74,],[46,46,95,]),'json_pair':([23,63,74,],[47,47,47,]),'args':([68,],[93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_part_list','program',1,'p_program','parser.py',26),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',32),
  ('program_part_list -> program_part','program_part_list',1,'p_program_part_list','parser.py',36),
  ('program_part_list -> program_part program_part_list','program_part_list',2,'p_program_part_list','parser.py',37),
  ('program_part -> event_list','program_part',1,'p_program_part','parser.py',45),
  ('program_part -> function_list','program_part',1,'p_program_part','parser.py',46),
  ('event_list -> event','event_list',1,'p_event_list','parser.py',51),
  ('event_list -> event_list event','event_list',2,'p_event_list','parser.py',52),
  ('event -> EVENT STRING LBRACE statement_list RBRACE','event',5,'p_event','parser.py',60),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',65),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',66),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',74),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',75),
  ('statement -> return_statement','statement',1,'p_statement','parser.py',76),
  ('statement -> comp_statement','statement',1,'p_statement','parser.py',77),
  ('statement -> expression SEMI','statement',2,'p_statement','parser.py',78),
  ('statement -> empty','statement',1,'p_statement','parser.py',79),
  ('if_statement -> IF LPAREN expression RPAREN statement','if_statement',5,'p_if_statement','parser.py',84),
  ('if_statement -> IF LPAREN expression RPAREN statement ELSE statement','if_statement',7,'p_if_statement','parser.py',85),
  ('while_statement -> WHILE LPAREN expression RPAREN statement','while_statement',5,'p_while_statement','parser.py',94),
  ('return_statement -> RETURN expression SEMI','return_statement',3,'p_return_statement','parser.py',99),
  ('comp_statement -> LBRACE statement_list RBRACE','comp_statement',3,'p_comp_statement','parser.py',104),
  ('expression -> TYPE ID ASSIGN expression','expression',4,'p_expression','parser.py',109),
  ('expression -> ID ASSIGN expression','expression',3,'p_expression','parser.py',110),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',111),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',112),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser.py',113),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',114),
  ('expression -> expression RELOP expression','expression',3,'p_expression','parser.py',115),
  ('expression -> expression AND expression','expression',3,'p_expression','parser.py',116),
  ('expression -> expression OR expression','expression',3,'p_expression','parser.py',117),
  ('expression -> expression ASSIGN expression','expression',3,'p_expression','parser.py',118),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','parser.py',119),
  ('expression -> NOT expression','expression',2,'p_expression','parser.py',120),
  ('expression -> MINUS expression','expression',2,'p_expression','parser.py',121),
  ('expression -> ID LPAREN RPAREN','expression',3,'p_expression','parser.py',122),
  ('expression -> ID LPAREN args RPAREN','expression',4,'p_expression','parser.py',123),
  ('expression -> expression DOT ID','expression',3,'p_expression','parser.py',124),
  ('expression -> ID','expression',1,'p_expression','parser.py',125),
  ('expression -> INT','expression',1,'p_expression','parser.py',126),
  ('expression -> FLOAT','expression',1,'p_expression','parser.py',127),
  ('expression -> STRING','expression',1,'p_expression','parser.py',128),
  ('expression -> json','expression',1,'p_expression','parser.py',129),
  ('args -> expression','args',1,'p_args','parser.py',142),
  ('args -> args COMMA expression','args',3,'p_args','parser.py',143),
  ('json -> LBRACE json_list RBRACE','json',3,'p_json','parser.py',151),
  ('json_list -> json_pair','json_list',1,'p_json_list','parser.py',156),
  ('json_list -> json_pair COMMA json_list','json_list',3,'p_json_list','parser.py',157),
  ('json_pair -> STRING COLON expression','json_pair',3,'p_json_pair','parser.py',165),
  ('function_list -> ID LPAREN RPAREN comp_statement','function_list',4,'p_function_list','parser.py',170),
  ('function_list -> ID LPAREN var_list RPAREN comp_statement','function_list',5,'p_function_list','parser.py',171),
  ('var_list -> TYPE ID','var_list',2,'p_var_list','parser.py',180),
  ('var_list -> var_list COMMA TYPE ID','var_list',4,'p_var_list','parser.py',181),
]
