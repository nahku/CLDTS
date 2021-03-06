from enum import Enum
import Lexer
import ply.yacc as yacc
from typing import List


class ProductionProperty(Enum):
    NONE = 1
    REPETITION = 2
    OPTIONAL = 3


class SYMBOL:
    def __init__(self, value):
        self.value = value


class T_SYMBOL(SYMBOL):
    def __init__(self, value, property=ProductionProperty.NONE):
        super().__init__(value)
        self.property = property

    def __str__(self):
        symbol_string = ""
        if self.property == ProductionProperty.NONE:
            symbol_string += self.value
        elif self.property == ProductionProperty.REPETITION:
            symbol_string += self.value
            symbol_string += "*"
        elif self.property == ProductionProperty.OPTIONAL:
            symbol_string += "["
            symbol_string += self.value
            symbol_string += "]"

        return symbol_string


class NT_SYMBOL(SYMBOL):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return self.value


class RULE:
    def __init__(self, name, productions_list):
        self.name = name
        self.productions_list = productions_list
        self.position = None


class GRAMMAR_RULE(RULE):
    def __init__(self, name, productions_list):
        super().__init__(name, productions_list)


class TOKEN_RULE(RULE):
    def __init__(self, name, productions_list):
        super().__init__(name, productions_list)


class STRICT_RULE(RULE):
    def __init__(self, name, productions_list):
        super().__init__(name, productions_list)


class MACRO_RULE(RULE):
    def __init__(self, name, productions_list):
        super().__init__(name, productions_list)


class GRAMMAR_LIST:
    def __init__(self, grammar_list):
        self.list = grammar_list


class PRODUCTIONS_LIST:
    def __init__(self, productions_list):
        self.list = productions_list

    def __str__(self):
        productions_list_string = ""
        length = len(self.list)
        index = 1
        for production in self.list:
            productions_list_string += str(production)
            if index < length:
                productions_list_string += " | "
            index += 1

        return productions_list_string


class XOR_PRODUCTIONS_LIST(PRODUCTIONS_LIST):
    def __init__(self, xor_productions_list):
        super().__init__(xor_productions_list)

    def __str__(self):
        xor_productions_list_string = ""
        xor_productions_list_string += "("
        productions_list_string = ""
        length = len(self.list)
        j = 1
        for production in self.list:
            productions_list_string += str(production)
            if j < length:
                productions_list_string += "|"
            j = j + 1
        xor_productions_list_string += productions_list_string
        xor_productions_list_string += ")"
        return xor_productions_list_string


class PRODUCTION:
    def __init__(self, list, productionProperty=ProductionProperty.NONE):
        self.list = list
        self.productionProperty = productionProperty

    def __str__(self):
        production_string = ""
        if self.productionProperty == ProductionProperty.REPETITION:
            production_string += "("
        elif self.productionProperty == ProductionProperty.OPTIONAL:
            production_string += "["

        for element in self.list:
            production_string += str(element)

        if self.productionProperty == ProductionProperty.REPETITION:
            production_string += ")"
            production_string += "*"
        elif self.productionProperty == ProductionProperty.OPTIONAL:
            production_string += "]"
        return production_string


class PRODUCTION_ELEMENT:
    def __init__(self, symbol: SYMBOL, productionProperty=ProductionProperty.NONE):
        self.symbol = symbol
        self.productionProperty = productionProperty  # none, repetition or optional

    def __str__(self):
        production_element_string = ""
        if self.productionProperty == ProductionProperty.NONE:
            production_element_string += str(self.symbol)
        elif self.productionProperty == ProductionProperty.REPETITION:
            production_element_string += str(self.symbol)
            production_element_string += "*"
        elif self.productionProperty == ProductionProperty.OPTIONAL:
            production_element_string += "["
            production_element_string += str(self.symbol)
            production_element_string += "]"
        return production_element_string


class COMMENT_BLOCK:
    def __init__(self, comment_lines):
        self.comment_lines = comment_lines

    def __str__(self):
        comment_string = ""
        if self.comment_lines is not None:
            for line in self.comment_lines:
                comment_string += line + "\n"
        return comment_string

    def __eq__(self, other):
        if not isinstance(other, COMMENT_BLOCK):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.comment_lines == other.comment_lines

    def __hash__(self):
        return hash(self.comment_lines)

    def extend(self, comment_lines: List[str]):
        self.comment_lines.extend(comment_lines)

    def find_top_of_page_line_ids(self) -> List[int]:
        """Find the IDs of top of page lines ordered ascending.

        :return: List of IDs of top of page lines.
        :rtype: List[int]
        """
        index = 0
        index_list = []
        for line in self.comment_lines:
            if line == "%----Top of Page---------------------------------------------------------------":
                index_list.append(index)
            index += 1
        return index_list

    def split_comment_block_by_top_of_page(self) -> List:
        """Split a COMMENT_BLOCK by top of page lines and return a list of split COMMENT_BLOCKs without
        the top of page lines.

        :return: List of COMMENT_BLOCKs split by top of page.
        :rtype: List[COMMENT_BLOCK]
        """
        top_of_page_indexes = self.find_top_of_page_line_ids()
        comment_block_list = []
        if not top_of_page_indexes:  # if list is empty
            comment_block_list = [self]
        else:
            # potential leading comment block
            first_top_of_page_index = top_of_page_indexes[0]
            if first_top_of_page_index != 0:
                first_comment_block = COMMENT_BLOCK(self.comment_lines[0:first_top_of_page_index])
                comment_block_list.append(first_comment_block)

            for index_in_list, top_of_page_index in enumerate(top_of_page_indexes):
                # if top of page is not last line
                if top_of_page_index != len(self.comment_lines) - 1:
                    start = top_of_page_index + 1
                    #if this is not last top_of_page_index
                    if index_in_list + 1 < len(top_of_page_indexes):
                        #end is next top_of_page_index
                        end = top_of_page_indexes[index_in_list + 1]
                    else:
                        #end is end of comment lines
                        end = len(self.comment_lines)
                    new_comment_block = COMMENT_BLOCK(self.comment_lines[start:end])
                    comment_block_list.append(new_comment_block)

        return comment_block_list


class TPTPParser:

    # production rules

    def p_grammar_list(self, p):
        """
        grammar_list : comment_block
                    |  grammar_expression
                    |  token_expression
                    |  strict_expression
                    |  macro_expression
                    |  grammar_list grammar_expression
                    |  grammar_list token_expression
                    |  grammar_list strict_expression
                    |  grammar_list macro_expression
                    |  grammar_list comment_block
        """
        if len(p) == 2:
            p[0] = GRAMMAR_LIST([p[1]])
        elif len(p) == 3:
            p[1].list.append(p[2])
            p[0] = p[1]

    def p_comment_block(self, p):
        """
        comment_block : COMMENT
                    |   comment_block COMMENT
        """

        if len(p) == 2:
            p[0] = COMMENT_BLOCK([p[1]])
        elif len(p) == 3:
            p[1].comment_lines.append(p[2])
            p[0] = p[1]

    def p_grammar_expression(self, p):
        """
        grammar_expression : LGRAMMAR_EXPRESSION productions_list
                            | LGRAMMAR_EXPRESSION

        """
        if len(p) == 3:
            p[0] = GRAMMAR_RULE(p[1], p[2])
        elif len(p) == 2:  # for case <null> ::=
            p[0] = GRAMMAR_RULE(p[1], PRODUCTIONS_LIST([PRODUCTION([PRODUCTION_ELEMENT(T_SYMBOL(""))])]))

    def p_token_expression(self, p):
        """
        token_expression : LTOKEN_EXPRESSION productions_list
        """
        p[0] = TOKEN_RULE(p[1], p[2])

    def p_strict_expression(self, p):
        """
        strict_expression : LSTRICT_EXPRESSION productions_list
        """
        p[0] = STRICT_RULE(p[1], p[2])

    def p_macro_expression(self, p):
        """
        macro_expression : LMACRO_EXPRESSION productions_list
        """
        p[0] = MACRO_RULE(p[1], p[2])

    def p_productions_list(self, p):
        """
        productions_list : production
                        | productions_list ALTERNATIVE_SYMBOL production
        """
        if len(p) == 2:
            p[0] = PRODUCTIONS_LIST([p[1]])
        elif len(p) == 4:
            p[1].list.append(p[3])
            p[0] = p[1]

    def p_xor_productions_list(self, p):
        """
        xor_productions_list : production
                        | xor_productions_list ALTERNATIVE_SYMBOL production
        """
        if len(p) == 2:
            p[0] = XOR_PRODUCTIONS_LIST([p[1]])
        elif len(p) == 4:
            p[1].list.append(p[3])
            p[0] = p[1]

    def p_t_symbol_production(self, p):
        """
            t_symbol_production : OPEN_SQUARE_BRACKET T_SYMBOL CLOSE_SQUARE_BRACKET
                             |    OPEN_SQUARE_BRACKET REPETITION_SYMBOL CLOSE_SQUARE_BRACKET
                             |    OPEN_SQUARE_BRACKET ALTERNATIVE_SYMBOL CLOSE_SQUARE_BRACKET
                             |    T_SYMBOL
            """
        if len(p) == 2:
            p[0] = T_SYMBOL(p[1])
        elif len(p) == 4:
            p[0] = T_SYMBOL(p[2], ProductionProperty.OPTIONAL)

    def p_production_element(self, p):
        """
        production_element : OPEN_SQUARE_BRACKET NT_SYMBOL CLOSE_SQUARE_BRACKET
                |    NT_SYMBOL REPETITION_SYMBOL
                |    t_symbol_production REPETITION_SYMBOL
                |    OPEN_SQUARE_BRACKET CLOSE_SQUARE_BRACKET
                |    NT_SYMBOL
                |    t_symbol_production
        """
        if len(p) == 2:  # NT_SYMBOL|t_symbol_production
            if type(p[1]) is T_SYMBOL:
                p[0] = PRODUCTION_ELEMENT(p[1], ProductionProperty.NONE)
            else:
                p[0] = PRODUCTION_ELEMENT(NT_SYMBOL(p[1]), ProductionProperty.NONE)
        elif len(p) == 3 and p[1] == "[":  # OPEN_SQUARE_BRACKET CLOSE_SQUARE_BRACKET
            p[0] = PRODUCTION([], ProductionProperty.OPTIONAL)  # evt. Problem wegen leerer Liste
        elif len(p) == 3:  # NT_SYMBOL REPETITION_SYMBOL|t_symbol_production REPETITION_SYMBOL
            if type(p[1]) is T_SYMBOL:
                p[0] = PRODUCTION_ELEMENT(p[1], ProductionProperty.REPETITION)
            else:
                p[0] = PRODUCTION_ELEMENT(NT_SYMBOL(p[1]), ProductionProperty.REPETITION)
        elif len(p) == 4 and p[1] == '[':  # OPEN_SQUARE_BRACKET NT_SYMBOL CLOSE_SQUARE_BRACKET
            p[0] = PRODUCTION_ELEMENT(NT_SYMBOL(p[2]), ProductionProperty.OPTIONAL)

    def p_production(self, p):
        # missing optional production
        """
        production : production_element
                |    production production_element
                |    OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS
                |    OPEN_PARENTHESIS production CLOSE_PARENTHESIS
                |    production OPEN_PARENTHESIS production CLOSE_PARENTHESIS
                |    production OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS
                |    OPEN_PARENTHESIS production CLOSE_PARENTHESIS production
                |    OPEN_PARENTHESIS xor_productions_list CLOSE_PARENTHESIS production
                |    OPEN_PARENTHESIS production CLOSE_PARENTHESIS REPETITION_SYMBOL
                |    production OPEN_PARENTHESIS production CLOSE_PARENTHESIS REPETITION_SYMBOL


        """
        if len(p) == 2:
            p[0] = PRODUCTION([p[1]])
        elif len(p) == 3:
            p[1].list.append(p[2])
            p[0] = p[1]
        elif len(p) == 4 and type(p[2]) is PRODUCTION:
            p[2].list.insert(0, PRODUCTION_ELEMENT(T_SYMBOL('(')))
            p[2].list.append(PRODUCTION_ELEMENT(T_SYMBOL(')')))
            p[0] = p[2]
        elif len(p) == 4 and p[1] == '(':
            p[0] = PRODUCTION([p[2]])
        elif len(p) == 5 and p[4] == '*':
            p[2].productionProperty = ProductionProperty.REPETITION
            p[0] = PRODUCTION([p[2]])
        elif len(p) == 5 and p[3] == ')' and isinstance(p[2], PRODUCTION):
            p[2].list.insert(0, PRODUCTION_ELEMENT(T_SYMBOL('(')))
            p[2].list.append(PRODUCTION_ELEMENT(T_SYMBOL(')')))
            p[4].list.insert(0, PRODUCTION(p[2]))
            p[0] = p[4]
        elif len(p) == 5 and p[3] == ')' and isinstance(p[2], XOR_PRODUCTIONS_LIST):
            p[4].list.insert(0, PRODUCTION([p[2]]))
            p[0] = p[4]
        elif len(p) == 5 and p[4] == ')' and isinstance(p[3], PRODUCTION):
            p[3].list.insert(0, PRODUCTION_ELEMENT(T_SYMBOL('(')))
            p[3].list.append(PRODUCTION_ELEMENT(T_SYMBOL(')')))
            p[1].list.append(p[3])
            p[0] = p[1]
        elif len(p) == 5 and p[4] == ')' and isinstance(p[3], XOR_PRODUCTIONS_LIST):
            p[1].list.append(PRODUCTION([p[3]]))
            p[0] = p[1]
        elif len(p) == 5:
            p[2].productionProperty = ProductionProperty.REPETITION
            p[0] = PRODUCTION([p[2]])
        elif len(p) == 6 and p[5] == '*':
            p[3].productionProperty = ProductionProperty.REPETITION
            p[1].list.append(PRODUCTION([p[3]]))
            p[0] = p[1]

    def p_error(self, t):
        print("Syntax error at '%s'" % t.value)

    def disambigue_square_brackets(self, rules_list: GRAMMAR_LIST) -> GRAMMAR_LIST:
        """Replaces ProductionProperty OPTIONAL by the terminal symbols
         open and closing square bracket for GRAMMAR and STRICT Expressions.

        :param rules_list: List of all rules from the TPTP grammar file.
        :return: List of all rules from TPTP grammar file with correct square bracket interpretation.
        """
        for production_rule in rules_list.list:
            if (isinstance(production_rule, GRAMMAR_RULE)) or (isinstance(production_rule, STRICT_RULE)):
                self.replace_optional_square_brackets_by_terminal(production_rule)
        return rules_list

    def replace_optional_square_brackets_by_terminal(self, rule: RULE):
        """Replaces ProductionProperty OPTIONAL by the terminal square brackets for all productions in an RULE.

        :param rule: GRAMMAR_RULE.
        """
        for production in rule.productions_list.list:
            self.replace_square_brackets_in_production(production)

    def replace_square_brackets_in_production(self, production: PRODUCTION):
        """Replaces ProductionProperty OPTIONAL by the terminal square brackets in a production recursively.

        :param production: Production, where ProductionProperty OPTIONAL is to be replaced by terminal square brackets
        """
        if production.productionProperty == ProductionProperty.OPTIONAL:
            production.list.insert(0, PRODUCTION_ELEMENT(T_SYMBOL("[")))
            production.list.append(PRODUCTION_ELEMENT(T_SYMBOL("]")))
            production.productionProperty = ProductionProperty.NONE

        i = 0
        for element in production.list:
            if isinstance(element, PRODUCTION):
                self.replace_square_brackets_in_production(element)
            elif (isinstance(element, PRODUCTION_ELEMENT) and (
                    element.productionProperty == ProductionProperty.OPTIONAL)):
                element.productionProperty = ProductionProperty.NONE
                production.list[i] = PRODUCTION(
                    [PRODUCTION_ELEMENT(T_SYMBOL("[")), element, PRODUCTION_ELEMENT(T_SYMBOL("]"))])
            i = i + 1

    @staticmethod
    def number_rules(rules_list: GRAMMAR_LIST) -> GRAMMAR_LIST:
        """Number rules by occurrence in TPTP grammar file.

        :param rules_list:  List of all rules from the TPTP grammar file.
        :return: List of all rules from TPTP grammar file numbered by occurence.
        """
        i = 0
        for element in rules_list.list:
            if not isinstance(element, COMMENT_BLOCK):
                element.position = i
                i = i + 1
        return rules_list

    def run(self, file: str) -> GRAMMAR_LIST:
        """Run parser on TPTP grammar file passed as string.

        :param file: TPTP grammar file as string.
        :return: Grammar_List containing the representation of the TPTP grammar.
        """

        rules_list = self.parser.parse(file)
        rules_list = self.number_rules(rules_list)
        rules_list = self.disambigue_square_brackets(rules_list)
        return rules_list

    def __init__(self):
        self.tokens = Lexer.TPTPLexer.tokens
        self.lexer = Lexer.TPTPLexer()
        self.parser = yacc.yacc(module=self)
