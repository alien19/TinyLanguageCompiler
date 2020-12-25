from code_parser import Parser
from scanner import Scanner


class Compiler:
    def __init__(self, text: str=""):
        self.scanner: Scanner = Scanner(text)
        stringsAndTokens = self.scanner.get_strings_and_tokens_list()
        self.parser: Parser = Parser(stringsAndTokens)

    def set_text(self, text: str):
        self.scanner.set_text(text)
        stringsAndTokens = self.scanner.get_strings_and_tokens_list()
        self.parser.set_strings_and_tokens(stringsAndTokens)

    def get_parse_tree_iterator(self):
        return self.parser.get_parse_tree_iterator()
