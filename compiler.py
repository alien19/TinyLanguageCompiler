from scanner import Scanner
from parser import Parser

# TODO
class Compiler:
  def __init__(self):
    self.scanner = Scanner()
    self.parser = Parser()
  
  def set_text(self, text: str):
    self.scanner.set_text(text)
    stringsAndTokens = self.scanner.get_strings_and_tokens_list()
    self.parser.set_strings_and_tokens(stringsAndTokens)
  
  def get_parse_tree_iterator(self):
    return self.parser.get_parse_tree().iterator()