
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFnonassocELSErightASSIGNleftORleftANDleftEQUALleftLTGTleftPLUSMINUSleftTIMESDIVIDErightUOPTYPECASTAND ASSIGN BOOL CINT COMMA DEF DIVIDE ELSE EQUAL EXTERN FALSE FLOAT GT ID IF INT LBRACE LBRACKET LIT LPAREN LT MINUS NOALIAS NOT OR PLUS PRINT RBRACE RBRACKET REF RETURN RPAREN SEMICOLON SLIT TIMES TRUE VARID VOID WHILEprog : funcs\n          | externs funcsexterns : extern\n             | extern externsfuncs : func\n           | func funcsextern : EXTERN TYPE globid LPAREN RPAREN SEMICOLON\n            | EXTERN TYPE globid LPAREN tdecls RPAREN SEMICOLONfunc : DEF TYPE globid LPAREN RPAREN blk\n          | DEF TYPE globid LPAREN vdecls RPAREN blkblk : LBRACE RBRACE\n         | LBRACE stmts RBRACEstmts : stmt\n           | stmt stmtsstmt : blkstmt : RETURN SEMICOLON\n          | RETURN exp SEMICOLONstmt : vdecl ASSIGN exp SEMICOLONstmt : exp SEMICOLONstmt : WHILE LPAREN exp RPAREN stmtstmt : IF LPAREN exp RPAREN stmt %prec IF\n          | IF LPAREN exp RPAREN stmt ELSE stmtstmt : PRINT exp SEMICOLONstmt : PRINT slit SEMICOLON exps : exp\n           | exp COMMA expsexp : LPAREN exp RPARENexp : binop\n         | uopexp : litexp : varidexp : globid LPAREN RPAREN\n         | globid LPAREN exps RPARENbinop : arithOps\n           | logicOps\n           | varid ASSIGN exp\n           | LBRACKET TYPE RBRACKET exp %prec TYPECASTarithOps : exp TIMES exp\n              | exp DIVIDE exp\n              | exp PLUS exp\n              | exp MINUS explogicOps : exp EQUAL exp\n              | exp LT exp\n              | exp GT exp\n              | exp AND exp\n              | exp OR expuop : MINUS exp %prec UOP\n         | NOT exp %prec UOPlit : TRUE\n         | FALSE\n         | LITslit : SLITvarid : VARIDglobid : IDTYPE : INT\n          | CINT\n          | FLOAT\n          | BOOL\n          | VOID\n          | REF TYPE\n          | NOALIAS REF TYPEvdecls : vdecl\n            | vdecl COMMA vdeclstdecls : TYPE\n            | TYPE COMMA tdeclsvdecl : TYPE varid'
    
_lr_action_items = {'DEF':([0,3,4,5,10,37,42,44,68,71,72,],[6,6,6,-3,-4,-9,-7,-11,-10,-8,-12,]),'EXTERN':([0,5,42,71,],[7,7,-7,-8,]),'$end':([1,2,4,8,9,37,44,68,72,],[0,-1,-5,-2,-6,-9,-11,-10,-12,]),'INT':([6,7,17,23,25,27,38,40,41,44,46,47,62,72,74,76,98,112,113,119,120,121,125,126,128,129,],[12,12,12,12,12,12,12,12,12,-11,12,-15,12,-12,-16,-19,-17,-23,-24,-18,12,12,-20,-21,12,-22,]),'CINT':([6,7,17,23,25,27,38,40,41,44,46,47,62,72,74,76,98,112,113,119,120,121,125,126,128,129,],[13,13,13,13,13,13,13,13,13,-11,13,-15,13,-12,-16,-19,-17,-23,-24,-18,13,13,-20,-21,13,-22,]),'FLOAT':([6,7,17,23,25,27,38,40,41,44,46,47,62,72,74,76,98,112,113,119,120,121,125,126,128,129,],[14,14,14,14,14,14,14,14,14,-11,14,-15,14,-12,-16,-19,-17,-23,-24,-18,14,14,-20,-21,14,-22,]),'BOOL':([6,7,17,23,25,27,38,40,41,44,46,47,62,72,74,76,98,112,113,119,120,121,125,126,128,129,],[15,15,15,15,15,15,15,15,15,-11,15,-15,15,-12,-16,-19,-17,-23,-24,-18,15,15,-20,-21,15,-22,]),'VOID':([6,7,17,23,25,27,38,40,41,44,46,47,62,72,74,76,98,112,113,119,120,121,125,126,128,129,],[16,16,16,16,16,16,16,16,16,-11,16,-15,16,-12,-16,-19,-17,-23,-24,-18,16,16,-20,-21,16,-22,]),'REF':([6,7,17,18,23,25,27,38,40,41,44,46,47,62,72,74,76,98,112,113,119,120,121,125,126,128,129,],[17,17,17,23,17,17,17,17,17,17,-11,17,-15,17,-12,-16,-19,-17,-23,-24,-18,17,17,-20,-21,17,-22,]),'NOALIAS':([6,7,17,23,25,27,38,40,41,44,46,47,62,72,74,76,98,112,113,119,120,121,125,126,128,129,],[18,18,18,18,18,18,18,18,18,-11,18,-15,18,-12,-16,-19,-17,-23,-24,-18,18,18,-20,-21,18,-22,]),'ID':([11,12,13,14,15,16,19,22,26,38,44,46,47,48,52,54,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[21,-55,-56,-57,-58,-59,21,-60,-61,21,-11,21,-15,21,21,21,21,21,-12,-16,-19,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-17,-23,-24,21,-18,21,21,21,-20,-21,21,-22,]),'VARID':([12,13,14,15,16,22,26,28,38,44,46,47,48,52,54,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[-55,-56,-57,-58,-59,-60,-61,36,36,-11,36,-15,36,36,36,36,36,-12,-16,-19,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-17,-23,-24,36,-18,36,36,36,-20,-21,36,-22,]),'COMMA':([12,13,14,15,16,22,26,31,32,35,36,55,56,57,58,60,61,65,66,67,96,97,99,100,101,102,103,104,105,106,107,110,114,115,117,122,124,],[-55,-56,-57,-58,-59,-60,-61,40,41,-66,-53,-31,-28,-29,-30,-34,-35,-49,-50,-51,-47,-48,-38,-39,-40,-41,-42,-43,-44,-45,-46,-27,-36,-32,123,-33,-37,]),'RPAREN':([12,13,14,15,16,22,25,26,27,30,31,32,34,35,36,55,56,57,58,60,61,65,66,67,69,70,88,94,96,97,99,100,101,102,103,104,105,106,107,109,110,111,114,115,116,117,122,124,127,],[-55,-56,-57,-58,-59,-60,29,-61,33,39,-62,-64,43,-66,-53,-31,-28,-29,-30,-34,-35,-49,-50,-51,-63,-65,110,115,-47,-48,-38,-39,-40,-41,-42,-43,-44,-45,-46,120,-27,121,-36,-32,122,-25,-33,-37,-26,]),'RBRACKET':([12,13,14,15,16,22,26,95,],[-55,-56,-57,-58,-59,-60,-61,118,]),'LPAREN':([20,21,24,38,44,46,47,48,51,52,53,54,59,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[25,-54,27,52,-11,52,-15,52,87,52,89,52,94,52,52,-12,-16,-19,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-17,-23,-24,52,-18,52,52,52,-20,-21,52,-22,]),'LBRACE':([29,38,39,44,46,47,72,74,76,98,112,113,119,120,121,125,126,128,129,],[38,38,38,-11,38,-15,-12,-16,-19,-17,-23,-24,-18,38,38,-20,-21,38,-22,]),'SEMICOLON':([33,36,43,48,49,55,56,57,58,60,61,65,66,67,75,90,91,92,96,97,99,100,101,102,103,104,105,106,107,108,110,114,115,122,124,],[42,-53,71,74,76,-31,-28,-29,-30,-34,-35,-49,-50,-51,98,112,113,-52,-47,-48,-38,-39,-40,-41,-42,-43,-44,-45,-46,119,-27,-36,-32,-33,-37,]),'ASSIGN':([35,36,50,55,],[-66,-53,86,93,]),'TIMES':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,77,-31,-28,-29,-30,-34,-35,-49,-50,-51,77,77,77,-47,-48,-38,-39,77,77,77,77,77,77,77,77,77,-27,77,77,-32,77,-33,-37,]),'DIVIDE':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,78,-31,-28,-29,-30,-34,-35,-49,-50,-51,78,78,78,-47,-48,-38,-39,78,78,78,78,78,78,78,78,78,-27,78,78,-32,78,-33,-37,]),'PLUS':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,79,-31,-28,-29,-30,-34,-35,-49,-50,-51,79,79,79,-47,-48,-38,-39,-40,-41,79,79,79,79,79,79,79,-27,79,79,-32,79,-33,-37,]),'MINUS':([36,38,44,46,47,48,49,52,54,55,56,57,58,60,61,63,64,65,66,67,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,120,121,122,123,124,125,126,128,129,],[-53,63,-11,63,-15,63,80,63,63,-31,-28,-29,-30,-34,-35,63,63,-49,-50,-51,-12,-16,80,-19,63,63,63,63,63,63,63,63,63,63,63,80,63,80,63,63,-47,-48,-17,-38,-39,-40,-41,80,80,80,80,80,80,80,-27,80,-23,-24,80,-32,80,63,-18,63,63,-33,63,-37,-20,-21,63,-22,]),'EQUAL':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,81,-31,-28,-29,-30,-34,-35,-49,-50,-51,81,81,81,-47,-48,-38,-39,-40,-41,-42,-43,-44,81,81,81,81,-27,81,81,-32,81,-33,-37,]),'LT':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,82,-31,-28,-29,-30,-34,-35,-49,-50,-51,82,82,82,-47,-48,-38,-39,-40,-41,82,-43,-44,82,82,82,82,-27,82,82,-32,82,-33,-37,]),'GT':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,83,-31,-28,-29,-30,-34,-35,-49,-50,-51,83,83,83,-47,-48,-38,-39,-40,-41,83,-43,-44,83,83,83,83,-27,83,83,-32,83,-33,-37,]),'AND':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,84,-31,-28,-29,-30,-34,-35,-49,-50,-51,84,84,84,-47,-48,-38,-39,-40,-41,-42,-43,-44,-45,84,84,84,-27,84,84,-32,84,-33,-37,]),'OR':([36,49,55,56,57,58,60,61,65,66,67,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,122,124,],[-53,85,-31,-28,-29,-30,-34,-35,-49,-50,-51,85,85,85,-47,-48,-38,-39,-40,-41,-42,-43,-44,-45,-46,85,85,-27,85,85,-32,85,-33,-37,]),'RBRACE':([38,44,45,46,47,72,73,74,76,98,112,113,119,125,126,129,],[44,-11,72,-13,-15,-12,-14,-16,-19,-17,-23,-24,-18,-20,-21,-22,]),'RETURN':([38,44,46,47,72,74,76,98,112,113,119,120,121,125,126,128,129,],[48,-11,48,-15,-12,-16,-19,-17,-23,-24,-18,48,48,-20,-21,48,-22,]),'WHILE':([38,44,46,47,72,74,76,98,112,113,119,120,121,125,126,128,129,],[51,-11,51,-15,-12,-16,-19,-17,-23,-24,-18,51,51,-20,-21,51,-22,]),'IF':([38,44,46,47,72,74,76,98,112,113,119,120,121,125,126,128,129,],[53,-11,53,-15,-12,-16,-19,-17,-23,-24,-18,53,53,-20,-21,53,-22,]),'PRINT':([38,44,46,47,72,74,76,98,112,113,119,120,121,125,126,128,129,],[54,-11,54,-15,-12,-16,-19,-17,-23,-24,-18,54,54,-20,-21,54,-22,]),'LBRACKET':([38,44,46,47,48,52,54,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[62,-11,62,-15,62,62,62,62,62,-12,-16,-19,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-17,-23,-24,62,-18,62,62,62,-20,-21,62,-22,]),'NOT':([38,44,46,47,48,52,54,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[64,-11,64,-15,64,64,64,64,64,-12,-16,-19,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-17,-23,-24,64,-18,64,64,64,-20,-21,64,-22,]),'TRUE':([38,44,46,47,48,52,54,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[65,-11,65,-15,65,65,65,65,65,-12,-16,-19,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-17,-23,-24,65,-18,65,65,65,-20,-21,65,-22,]),'FALSE':([38,44,46,47,48,52,54,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[66,-11,66,-15,66,66,66,66,66,-12,-16,-19,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-17,-23,-24,66,-18,66,66,66,-20,-21,66,-22,]),'LIT':([38,44,46,47,48,52,54,63,64,72,74,76,77,78,79,80,81,82,83,84,85,86,87,89,93,94,98,112,113,118,119,120,121,123,125,126,128,129,],[67,-11,67,-15,67,67,67,67,67,-12,-16,-19,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-17,-23,-24,67,-18,67,67,67,-20,-21,67,-22,]),'ELSE':([44,47,72,74,76,98,112,113,119,125,126,129,],[-11,-15,-12,-16,-19,-17,-23,-24,-18,-20,128,-22,]),'SLIT':([54,],[92,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'funcs':([0,3,4,],[2,8,9,]),'externs':([0,5,],[3,10,]),'func':([0,3,4,],[4,4,4,]),'extern':([0,5,],[5,5,]),'TYPE':([6,7,17,23,25,27,38,40,41,46,62,120,121,128,],[11,19,22,26,28,32,28,28,32,28,95,28,28,28,]),'globid':([11,19,38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[20,24,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'vdecls':([25,40,],[30,69,]),'vdecl':([25,38,40,46,120,121,128,],[31,50,31,50,50,50,50,]),'tdecls':([27,41,],[34,70,]),'varid':([28,38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[35,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'blk':([29,38,39,46,120,121,128,],[37,47,68,47,47,47,47,]),'stmts':([38,46,],[45,73,]),'stmt':([38,46,120,121,128,],[46,46,125,126,129,]),'exp':([38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[49,49,75,88,90,96,97,99,100,101,102,103,104,105,106,107,108,109,111,114,117,124,49,49,117,49,]),'binop':([38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'uop':([38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'lit':([38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'arithOps':([38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'logicOps':([38,46,48,52,54,63,64,77,78,79,80,81,82,83,84,85,86,87,89,93,94,118,120,121,123,128,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'slit':([54,],[91,]),'exps':([94,123,],[116,127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> funcs','prog',1,'p_prog','ekparser.py',20),
  ('prog -> externs funcs','prog',2,'p_prog','ekparser.py',21),
  ('externs -> extern','externs',1,'p_externs','ekparser.py',30),
  ('externs -> extern externs','externs',2,'p_externs','ekparser.py',31),
  ('funcs -> func','funcs',1,'p_funcs','ekparser.py',41),
  ('funcs -> func funcs','funcs',2,'p_funcs','ekparser.py',42),
  ('extern -> EXTERN TYPE globid LPAREN RPAREN SEMICOLON','extern',6,'p_extern','ekparser.py',52),
  ('extern -> EXTERN TYPE globid LPAREN tdecls RPAREN SEMICOLON','extern',7,'p_extern','ekparser.py',53),
  ('func -> DEF TYPE globid LPAREN RPAREN blk','func',6,'p_func','ekparser.py',62),
  ('func -> DEF TYPE globid LPAREN vdecls RPAREN blk','func',7,'p_func','ekparser.py',63),
  ('blk -> LBRACE RBRACE','blk',2,'p_blk','ekparser.py',72),
  ('blk -> LBRACE stmts RBRACE','blk',3,'p_blk','ekparser.py',73),
  ('stmts -> stmt','stmts',1,'p_statements','ekparser.py',82),
  ('stmts -> stmt stmts','stmts',2,'p_statements','ekparser.py',83),
  ('stmt -> blk','stmt',1,'p_blkStmt','ekparser.py',100),
  ('stmt -> RETURN SEMICOLON','stmt',2,'p_return','ekparser.py',104),
  ('stmt -> RETURN exp SEMICOLON','stmt',3,'p_return','ekparser.py',105),
  ('stmt -> vdecl ASSIGN exp SEMICOLON','stmt',4,'p_vdeclStmt','ekparser.py',112),
  ('stmt -> exp SEMICOLON','stmt',2,'p_expSemi','ekparser.py',116),
  ('stmt -> WHILE LPAREN exp RPAREN stmt','stmt',5,'p_while','ekparser.py',120),
  ('stmt -> IF LPAREN exp RPAREN stmt','stmt',5,'p_if','ekparser.py',124),
  ('stmt -> IF LPAREN exp RPAREN stmt ELSE stmt','stmt',7,'p_if','ekparser.py',125),
  ('stmt -> PRINT exp SEMICOLON','stmt',3,'p_printExp','ekparser.py',132),
  ('stmt -> PRINT slit SEMICOLON','stmt',3,'p_printSlit','ekparser.py',136),
  ('exps -> exp','exps',1,'p_exps','ekparser.py',142),
  ('exps -> exp COMMA exps','exps',3,'p_exps','ekparser.py',143),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_expParen','ekparser.py',158),
  ('exp -> binop','exp',1,'p_expBinOpUop','ekparser.py',162),
  ('exp -> uop','exp',1,'p_expBinOpUop','ekparser.py',163),
  ('exp -> lit','exp',1,'p_expLit','ekparser.py',167),
  ('exp -> varid','exp',1,'p_expVarid','ekparser.py',176),
  ('exp -> globid LPAREN RPAREN','exp',3,'p_expGlobid','ekparser.py',180),
  ('exp -> globid LPAREN exps RPAREN','exp',4,'p_expGlobid','ekparser.py',181),
  ('binop -> arithOps','binop',1,'p_binop','ekparser.py',193),
  ('binop -> logicOps','binop',1,'p_binop','ekparser.py',194),
  ('binop -> varid ASSIGN exp','binop',3,'p_binop','ekparser.py',195),
  ('binop -> LBRACKET TYPE RBRACKET exp','binop',4,'p_binop','ekparser.py',196),
  ('arithOps -> exp TIMES exp','arithOps',3,'p_arithOps','ekparser.py',210),
  ('arithOps -> exp DIVIDE exp','arithOps',3,'p_arithOps','ekparser.py',211),
  ('arithOps -> exp PLUS exp','arithOps',3,'p_arithOps','ekparser.py',212),
  ('arithOps -> exp MINUS exp','arithOps',3,'p_arithOps','ekparser.py',213),
  ('logicOps -> exp EQUAL exp','logicOps',3,'p_logicOps','ekparser.py',230),
  ('logicOps -> exp LT exp','logicOps',3,'p_logicOps','ekparser.py',231),
  ('logicOps -> exp GT exp','logicOps',3,'p_logicOps','ekparser.py',232),
  ('logicOps -> exp AND exp','logicOps',3,'p_logicOps','ekparser.py',233),
  ('logicOps -> exp OR exp','logicOps',3,'p_logicOps','ekparser.py',234),
  ('uop -> MINUS exp','uop',2,'p_uop','ekparser.py',250),
  ('uop -> NOT exp','uop',2,'p_uop','ekparser.py',251),
  ('lit -> TRUE','lit',1,'p_lit','ekparser.py',262),
  ('lit -> FALSE','lit',1,'p_lit','ekparser.py',263),
  ('lit -> LIT','lit',1,'p_lit','ekparser.py',264),
  ('slit -> SLIT','slit',1,'p_slit','ekparser.py',270),
  ('varid -> VARID','varid',1,'p_varid','ekparser.py',281),
  ('globid -> ID','globid',1,'p_globid','ekparser.py',287),
  ('TYPE -> INT','TYPE',1,'p_type','ekparser.py',293),
  ('TYPE -> CINT','TYPE',1,'p_type','ekparser.py',294),
  ('TYPE -> FLOAT','TYPE',1,'p_type','ekparser.py',295),
  ('TYPE -> BOOL','TYPE',1,'p_type','ekparser.py',296),
  ('TYPE -> VOID','TYPE',1,'p_type','ekparser.py',297),
  ('TYPE -> REF TYPE','TYPE',2,'p_type','ekparser.py',298),
  ('TYPE -> NOALIAS REF TYPE','TYPE',3,'p_type','ekparser.py',299),
  ('vdecls -> vdecl','vdecls',1,'p_vdecls','ekparser.py',310),
  ('vdecls -> vdecl COMMA vdecls','vdecls',3,'p_vdecls','ekparser.py',311),
  ('tdecls -> TYPE','tdecls',1,'p_tdecls','ekparser.py',321),
  ('tdecls -> TYPE COMMA tdecls','tdecls',3,'p_tdecls','ekparser.py',322),
  ('vdecl -> TYPE varid','vdecl',2,'p_vdecl','ekparser.py',332),
]
