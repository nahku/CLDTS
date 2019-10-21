import unittest
import lexer

class TestExpressions(unittest.TestCase):
    def test_comment(self):
        lexer.lexer()
        lexer.lex.input(lexer.import_tptp_file('TestCaseComment.txt'))
        type = True
        while 1:
            tok = lexer.lex.token()
            if not tok: break  # No more input
            if tok.type != 'COMMENT':
                type = False
        self.assertEqual(True, type)

    def test_grammar_rule(self):
        lexer.lexer()
        lexer.lex.input('::=')
        type = True
        while 1:
            tok = lexer.lex.token()
            if not tok: break  # No more input
            if tok.type != 'GRAMMAR_SYMBOL':
                type = False
        self.assertEqual(True, type)

    def test_token_rule(self):
        lexer.lexer()
        lexer.lex.input('::-')
        type = True
        while 1:
            tok = lexer.lex.token()
            if not tok: break  # No more input
            if tok.type != 'TOKEN_SYMBOL':
                type = False
        self.assertEqual(True, type)

    def test_strict_rule(self):
        lexer.lexer()
        lexer.lex.input(':==')
        type = True
        i = 0
        while 1:
            tok = lexer.lex.token()
            if not tok: break  # No more input
            if tok.type != 'STRICT_SYMBOL':
                type = False
        self.assertEqual(True, type)

    def test_macro_rule(self):
        lexer.lexer()
        lexer.lex.input(':::')
        type = True
        i = 0
        while 1:
            tok = lexer.lex.token()
            if not tok: break  # No more input
            if tok.type != r'MACRO_SYMBOL':
                type = False
            i += 1
        self.assertEqual(True, type)

    def test_alternative_rule(self):
        lexer.lexer()
        lexer.lex.input('|')
        type = True
        i = 0
        while 1:
            tok = lexer.lex.token()
            if not tok: break  # No more input
            if tok.type != 'ALTERNATIVE_SYMBOL':
                type = False
            i += 1
        self.assertEqual(True, type)

if __name__ == '__main__':
    unittest.main()
