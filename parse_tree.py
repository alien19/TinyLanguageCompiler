from enum import Enum, auto
from common import StructVal, TokenType, ParseTreeIterator
from node import Node

# TODO
class ParseTree:
  def __init__(self):
    self.root:Node = None
    self.currentNode:Node = None

  def iterator(self) -> ParseTreeIterator:
    pass

  def root(self) -> Node:
    pass

  def go_left(self) -> None:
    pass

  def go_right(self) -> None:
    pass

  def go_child(self, index:int) -> None:
    pass

  def go_first_child(self) -> None:
    pass

  def go_last_child(self) -> None:
    pass

  def go_top(self) -> None:
    pass

  def insert_right(self, text:str, value: str, structVal: StructType, tokenType: TokenType) -> None:
    # Insert and go to the right
    pass

  def insert_child(self, text:str, value: str, structVal: StructType, tokenType: TokenType) -> None:
    # Insert and go to the child
    pass
