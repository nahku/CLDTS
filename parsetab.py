
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALTERNATIVE_SYMBOL CLOSE_PARENTHESIS CLOSE_SQUARE_BRACKET COMMENT LGRAMMAR_EXPRESSION LMACRO_EXPRESSION LSTRICT_EXPRESSION LTOKEN_EXPRESSION NT_SYMBOL OPEN_PARENTHESIS OPEN_SQUARE_BRACKET REPETITION_SYMBOL T_SYMBOL\n        grammar_list : comment_block\n                    |  grammar_expression\n                    |  token_expression\n                    |  strict_expression\n                    |  macro_expression\n                    |  grammar_list grammar_expression\n                    |  grammar_list token_expression\n                    |  grammar_list strict_expression\n                    |  grammar_list macro_expression\n                    |  grammar_list comment_block\n        \n        comment_block : COMMENT\n                    |   comment_block COMMENT\n        \n        grammar_expression : LGRAMMAR_EXPRESSION productions_list\n                            | LGRAMMAR_EXPRESSION\n\n        \n        token_expression : LTOKEN_EXPRESSION productions_list\n        \n        strict_expression : LSTRICT_EXPRESSION productions_list\n        \n        macro_expression : LMACRO_EXPRESSION productions_list\n        \n        productions_list : production\n                        | productions_list ALTERNATIVE_SYMBOL production\n        \n        xor_productions_list : production\n                        | xor_productions_list ALTERNATIVE_SYMBOL production\n        \n            t_symbol_production : OPEN_SQUARE_BRACKET T_SYMBOL CLOSE_SQUARE_BRACKET\n                             |    OPEN_SQUARE_BRACKET REPETITION_SYMBOL CLOSE_SQUARE_BRACKET\n                             |    OPEN_SQUARE_BRACKET ALTERNATIVE_SYMBOL CLOSE_SQUARE_BRACKET\n                             |    T_SYMBOL\n            \n        production_element : OPEN_SQUARE_BRACKET NT_SYMBOL CLOSE_SQUARE_BRACKET\n                |    NT_SYMBOL REPETITION_SYMBOL\n                |    t_symbol_production REPETITION_SYMBOL\n                |    OPEN_SQUARE_BRACKET CLOSE_SQUARE_BRACKET\n                |    NT_SYMBOL\n                |    t_symbol_production\n        \n        production : production_element\n                |    production production_element\n                |    OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS\n                |    OPEN_PARENTHESIS production CLOSE_PARENTHESIS\n                |    production OPEN_PARENTHESIS production CLOSE_PARENTHESIS\n                |    production OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS\n                |    OPEN_PARENTHESIS production CLOSE_PARENTHESIS production\n                |    OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS production\n                |    OPEN_PARENTHESIS production CLOSE_PARENTHESIS REPETITION_SYMBOL\n                |    production OPEN_PARENTHESIS production CLOSE_PARENTHESIS REPETITION_SYMBOL\n\n\n        '
    
_lr_action_items = {'COMMENT':([0,1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,30,35,39,40,41,44,46,47,48,49,50,51,52,53,55,56,57,],[7,7,17,-2,-3,-4,-5,-11,-14,-6,-7,-8,-9,17,-12,-13,-18,-32,-30,-31,-25,-15,-16,-17,-33,-29,-27,-28,-19,-34,-35,-26,-22,-23,-24,-36,-37,-39,-38,-40,-41,]),'LGRAMMAR_EXPRESSION':([0,1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,30,35,39,40,41,44,46,47,48,49,50,51,52,53,55,56,57,],[8,8,-1,-2,-3,-4,-5,-11,-14,-6,-7,-8,-9,-10,-12,-13,-18,-32,-30,-31,-25,-15,-16,-17,-33,-29,-27,-28,-19,-34,-35,-26,-22,-23,-24,-36,-37,-39,-38,-40,-41,]),'LTOKEN_EXPRESSION':([0,1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,30,35,39,40,41,44,46,47,48,49,50,51,52,53,55,56,57,],[9,9,-1,-2,-3,-4,-5,-11,-14,-6,-7,-8,-9,-10,-12,-13,-18,-32,-30,-31,-25,-15,-16,-17,-33,-29,-27,-28,-19,-34,-35,-26,-22,-23,-24,-36,-37,-39,-38,-40,-41,]),'LSTRICT_EXPRESSION':([0,1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,30,35,39,40,41,44,46,47,48,49,50,51,52,53,55,56,57,],[10,10,-1,-2,-3,-4,-5,-11,-14,-6,-7,-8,-9,-10,-12,-13,-18,-32,-30,-31,-25,-15,-16,-17,-33,-29,-27,-28,-19,-34,-35,-26,-22,-23,-24,-36,-37,-39,-38,-40,-41,]),'LMACRO_EXPRESSION':([0,1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,30,35,39,40,41,44,46,47,48,49,50,51,52,53,55,56,57,],[11,11,-1,-2,-3,-4,-5,-11,-14,-6,-7,-8,-9,-10,-12,-13,-18,-32,-30,-31,-25,-15,-16,-17,-33,-29,-27,-28,-19,-34,-35,-26,-22,-23,-24,-36,-37,-39,-38,-40,-41,]),'$end':([1,2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,30,35,39,40,41,44,46,47,48,49,50,51,52,53,55,56,57,],[0,-1,-2,-3,-4,-5,-11,-14,-6,-7,-8,-9,-10,-12,-13,-18,-32,-30,-31,-25,-15,-16,-17,-33,-29,-27,-28,-19,-34,-35,-26,-22,-23,-24,-36,-37,-39,-38,-40,-41,]),'OPEN_PARENTHESIS':([8,9,10,11,19,20,21,23,24,25,29,30,31,33,35,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[21,21,21,21,31,-32,21,-30,-31,-25,21,-33,21,31,-29,-27,-28,31,31,21,21,21,-26,-22,-23,-24,-36,-37,31,31,31,-40,-41,]),'OPEN_SQUARE_BRACKET':([8,9,10,11,19,20,21,23,24,25,29,30,31,33,35,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[22,22,22,22,22,-32,22,-30,-31,-25,22,-33,22,22,-29,-27,-28,22,22,22,22,22,-26,-22,-23,-24,-36,-37,22,22,22,-40,-41,]),'NT_SYMBOL':([8,9,10,11,19,20,21,22,23,24,25,29,30,31,33,35,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[23,23,23,23,23,-32,23,34,-30,-31,-25,23,-33,23,23,-29,-27,-28,23,23,23,23,23,-26,-22,-23,-24,-36,-37,23,23,23,-40,-41,]),'T_SYMBOL':([8,9,10,11,19,20,21,22,23,24,25,29,30,31,33,35,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[25,25,25,25,25,-32,25,36,-30,-31,-25,25,-33,25,25,-29,-27,-28,25,25,25,25,25,-26,-22,-23,-24,-36,-37,25,25,25,-40,-41,]),'ALTERNATIVE_SYMBOL':([18,19,20,22,23,24,25,26,27,28,30,32,33,35,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,],[29,-18,-32,38,-30,-31,-25,29,29,29,-33,45,-20,-29,-27,-28,-19,-20,45,-34,-35,-26,-22,-23,-24,-36,-37,-39,-21,-38,-40,-41,]),'CLOSE_PARENTHESIS':([20,23,24,25,30,32,33,35,39,40,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,],[-32,-30,-31,-25,-33,44,46,-29,-27,-28,51,52,-34,-35,-26,-22,-23,-24,-36,-37,-39,-21,-38,-40,-41,]),'CLOSE_SQUARE_BRACKET':([22,34,36,37,38,],[35,47,48,49,50,]),'REPETITION_SYMBOL':([22,23,24,25,46,48,49,50,51,],[37,39,40,-25,56,-22,-23,-24,57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'grammar_list':([0,],[1,]),'comment_block':([0,1,],[2,16,]),'grammar_expression':([0,1,],[3,12,]),'token_expression':([0,1,],[4,13,]),'strict_expression':([0,1,],[5,14,]),'macro_expression':([0,1,],[6,15,]),'productions_list':([8,9,10,11,],[18,26,27,28,]),'production':([8,9,10,11,21,29,31,44,45,46,],[19,19,19,19,33,41,42,53,54,55,]),'production_element':([8,9,10,11,19,21,29,31,33,41,42,44,45,46,53,54,55,],[20,20,20,20,30,20,20,20,30,30,30,20,20,20,30,30,30,]),'t_symbol_production':([8,9,10,11,19,21,29,31,33,41,42,44,45,46,53,54,55,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'xor_productions_list':([21,31,],[32,43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> grammar_list","S'",1,None,None,None),
  ('grammar_list -> comment_block','grammar_list',1,'p_grammar_list','yacc.py',72),
  ('grammar_list -> grammar_expression','grammar_list',1,'p_grammar_list','yacc.py',73),
  ('grammar_list -> token_expression','grammar_list',1,'p_grammar_list','yacc.py',74),
  ('grammar_list -> strict_expression','grammar_list',1,'p_grammar_list','yacc.py',75),
  ('grammar_list -> macro_expression','grammar_list',1,'p_grammar_list','yacc.py',76),
  ('grammar_list -> grammar_list grammar_expression','grammar_list',2,'p_grammar_list','yacc.py',77),
  ('grammar_list -> grammar_list token_expression','grammar_list',2,'p_grammar_list','yacc.py',78),
  ('grammar_list -> grammar_list strict_expression','grammar_list',2,'p_grammar_list','yacc.py',79),
  ('grammar_list -> grammar_list macro_expression','grammar_list',2,'p_grammar_list','yacc.py',80),
  ('grammar_list -> grammar_list comment_block','grammar_list',2,'p_grammar_list','yacc.py',81),
  ('comment_block -> COMMENT','comment_block',1,'p_comment_block','yacc.py',91),
  ('comment_block -> comment_block COMMENT','comment_block',2,'p_comment_block','yacc.py',92),
  ('grammar_expression -> LGRAMMAR_EXPRESSION productions_list','grammar_expression',2,'p_grammar_expression','yacc.py',103),
  ('grammar_expression -> LGRAMMAR_EXPRESSION','grammar_expression',1,'p_grammar_expression','yacc.py',104),
  ('token_expression -> LTOKEN_EXPRESSION productions_list','token_expression',2,'p_token_expression','yacc.py',114),
  ('strict_expression -> LSTRICT_EXPRESSION productions_list','strict_expression',2,'p_strict_expression','yacc.py',120),
  ('macro_expression -> LMACRO_EXPRESSION productions_list','macro_expression',2,'p_macro_expression','yacc.py',126),
  ('productions_list -> production','productions_list',1,'p_productions_list','yacc.py',132),
  ('productions_list -> productions_list ALTERNATIVE_SYMBOL production','productions_list',3,'p_productions_list','yacc.py',133),
  ('xor_productions_list -> production','xor_productions_list',1,'p_xor_productions_list','yacc.py',143),
  ('xor_productions_list -> xor_productions_list ALTERNATIVE_SYMBOL production','xor_productions_list',3,'p_xor_productions_list','yacc.py',144),
  ('t_symbol_production -> OPEN_SQUARE_BRACKET T_SYMBOL CLOSE_SQUARE_BRACKET','t_symbol_production',3,'p_t_symbol_production','yacc.py',154),
  ('t_symbol_production -> OPEN_SQUARE_BRACKET REPETITION_SYMBOL CLOSE_SQUARE_BRACKET','t_symbol_production',3,'p_t_symbol_production','yacc.py',155),
  ('t_symbol_production -> OPEN_SQUARE_BRACKET ALTERNATIVE_SYMBOL CLOSE_SQUARE_BRACKET','t_symbol_production',3,'p_t_symbol_production','yacc.py',156),
  ('t_symbol_production -> T_SYMBOL','t_symbol_production',1,'p_t_symbol_production','yacc.py',157),
  ('production_element -> OPEN_SQUARE_BRACKET NT_SYMBOL CLOSE_SQUARE_BRACKET','production_element',3,'p_production_element','yacc.py',169),
  ('production_element -> NT_SYMBOL REPETITION_SYMBOL','production_element',2,'p_production_element','yacc.py',170),
  ('production_element -> t_symbol_production REPETITION_SYMBOL','production_element',2,'p_production_element','yacc.py',171),
  ('production_element -> OPEN_SQUARE_BRACKET CLOSE_SQUARE_BRACKET','production_element',2,'p_production_element','yacc.py',172),
  ('production_element -> NT_SYMBOL','production_element',1,'p_production_element','yacc.py',173),
  ('production_element -> t_symbol_production','production_element',1,'p_production_element','yacc.py',174),
  ('production -> production_element','production',1,'p_production','yacc.py',194),
  ('production -> production production_element','production',2,'p_production','yacc.py',195),
  ('production -> OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS','production',3,'p_production','yacc.py',196),
  ('production -> OPEN_PARENTHESIS production CLOSE_PARENTHESIS','production',3,'p_production','yacc.py',197),
  ('production -> production OPEN_PARENTHESIS production CLOSE_PARENTHESIS','production',4,'p_production','yacc.py',198),
  ('production -> production OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS','production',4,'p_production','yacc.py',199),
  ('production -> OPEN_PARENTHESIS production CLOSE_PARENTHESIS production','production',4,'p_production','yacc.py',200),
  ('production -> OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS production','production',4,'p_production','yacc.py',201),
  ('production -> OPEN_PARENTHESIS production CLOSE_PARENTHESIS REPETITION_SYMBOL','production',4,'p_production','yacc.py',202),
  ('production -> production OPEN_PARENTHESIS production CLOSE_PARENTHESIS REPETITION_SYMBOL','production',5,'p_production','yacc.py',203),
]
