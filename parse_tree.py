from enum import Enum, auto
from common import ParseTreeIterator, StructType, TokenType
from node import Node

class ParseTree:
  def __init__(self):
    self.root: Node = None
    self.currentNode: Node = None

  def iterator(self):
    return ParseTreeIterator(self.root)

  def root(self):
    return self.root

  def go_left(self):
    tmp_node = self.currentNode
    self.currentNode = self.currentNode.prev
    self.currentNode.nxt = tmp_node

  def go_right(self):
    tmp_node = self.currentNode
    self.currentNode = self.currentNode.nxt
    self.currentNode.prev = tmp_node

  def go_child(self, index: int):
    tmp_node = self.currentNode
    self.currentNode = self.currentNode.children[index]
    self.currentNode.parent = tmp_node

  def go_first_child(self):
    tmp_node = self.currentNode
    self.currentNode = self.currentNode.children[index]
    self.currentNode.parent = tmp_node

  def go_last_child(self):
    tmp_node = self.currentNode
    n_children = len(cur.children)
    self.currentNode = cur.children[n_children-1]
    self.currentNode.parent = tmp_node

  def go_top(self):
    tmp_node = self.currentNode
    self.currentNode = self.currentNode.parent
    self.currentNode.prev = tmp_node

  def insert_right(self, text: str, value: str, structVal: StructType, tokenType: TokenType):
    # Insert a̶n̶d̶ g̶o̶ t̶o̶ t̶h̶e̶ r̶i̶g̶h̶t̶
    self.currentNode.nxt = Node(text, value, structVal, tokenType)

  def insert_child(self, text: str, value: str, structVal: StructType, tokenType: TokenType):
    # Insert a̶n̶d̶ g̶o̶ t̶o̶ t̶h̶e̶ c̶h̶i̶l̶d̶
    # self.currentNode.children.append(Node(text, value, structVal, tokenType))
    self.currentNode.add_child(Node(text, value, structVal, tokenType))
