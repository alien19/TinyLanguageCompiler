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

