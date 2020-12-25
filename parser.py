from common import TokenType, StructType
from parse_tree import ParseTree

# TODO
class Parser:
  STATEMENT_TOKENS = [TokenType.IF, TokenType.REPEAT, TokenType.READ, TokenType.WRITE, TokenType.ID]

  def __init__(self, stringsAndTokens: list = []):
    # self.stringsAndTokens = stringsAndTokens
    # self.currentIndex = 0
    # self.parseTree = None
    # self.parse()
    self.set_strings_and_tokens(stringsAndTokens)
  
  def set_strings_and_tokens(self, stringsAndTokens: list):
    self.stringsAndTokens = stringsAndTokens
    self.currentIndex = 0
    self.parseTree: ParseTree = None
    self.parse()
  
  def has_finished(self) -> bool:
    return self.currentIndex >= len(self.stringsAndTokens)
  
  def current_token(self) -> TokenType:
    return self.stringsAndTokens[self.currentIndex][1]
  
  def current_string(self) -> TokenType:
    return self.stringsAndTokens[self.currentIndex][0]
  
  def current_string_and_token(self) -> TokenType:
    return self.stringsAndTokens[self.currentIndex]
  
  def parse(self):
    self.add_stmt_seq()
    
  def add_stmt_seq(self):
    while self.current_token() in Parser.STATEMENT_TOKENS and not self.has_finished():
      self.add_stmt()
      
  def add_stmt(self):
    if currentToken == TokenType.IF:
      self.add_if_stmt()
    elif currentToken == TokenType.REPEAT:
      self.add_repeat_stmt()
    elif currentToken == TokenType.READ:
      self.add_read_stmt()
    elif currentToken == TokenType.WRITE:
      self.add_write_stmt()
    elif currentToken == TokenType.ID:
      self.add_assign_stmt()
  
  def add_read_stmt(self):
    self.currentIndex += 1
    self.parseTree.insert_right("read", self.current_string(), StructType.EXPRESSION, TokenType.READ)
    self.parseTree.go_right()
    self.currentIndex += 2
  
  def add_write_stmt(self):
    self.currentIndex += 1
    self.parseTree.insert_right("write", None, StructType.EXPRESSION, TokenType.WRITE)
    self.parseTree.go_right()
    self.parseTree.insert_child("id", self.current_string(), StructType.STATEMENT, TokenType.ID)
    self.currentIndex += 2
