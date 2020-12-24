from enum import Enum, auto
from node import Node


class TokenType(Enum):
    IF = auto()
    THEN = auto()
    ELSE = auto()
    WRITE = auto()
    READ = auto()
    UNTIL = auto()
    END = auto()
    REPEAT = auto()

    SEMICOLON = auto()
    OPEN_PARAN = auto()
    CLOSE_PARAN = auto()
    LESS_THAN = auto()
    # COMMA = auto()
    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUAL = auto()

    NUM = auto()
    ID = auto()


class StructType(Enum):
  EXPRESSION = auto()
  STATEMENT = auto()

# TODO

class ParseTreeIterator:
    def __init__(self):
      pass

    def get_text(self): #-> str:
      pass

    def get_value(self): # -> str:
      pass

    def get_token_type(self): # -> TokenType:
      pass

    def get_struct_type(self): #-> StructType:
      pass

    def __next__(self): # -> ParseTreeIterator:
      pass

    def previous(self): # -> ParseTreeIterator:
      pass

    def children(self): # -> list:
      pass

    def has_next(self): # -> bool:
      pass

    def has_previous(self): # -> bool:
      pass

    def has_children(self): # -> bool:
      pass
