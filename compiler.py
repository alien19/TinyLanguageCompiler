from code_parser import Parser
from parse_tree_iterator import ParseTreeIterator
from scanner import Scanner


class Compiler:
    def __init__(self, text: str=""):
        self.scanner: Scanner = Scanner(text)
        stringsAndTokens = self.scanner.get_strings_and_tokens_list()
        self.parser: Parser = Parser(stringsAndTokens)

    def set_text(self, text: str) -> None:
        self.scanner.set_text(text)
        stringsAndTokens = self.scanner.get_strings_and_tokens_list()
        self.parser.set_strings_and_tokens(stringsAndTokens)

    def get_parse_tree_iterator(self) -> ParseTreeIterator:
        return self.parser.get_parse_tree_iterator()
