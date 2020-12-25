from common import StructType, TokenType

class Node:
    def __init__(self, text: str, value: str, structType: StructType, tokenType: TokenType):
        self.text: str = text
        self.value: str = value
        self.structType = structType
        # self.tokenType = tokenType
        self.nxt: Node = None
        self.prev: Node = None
        self.parent: Node = None
        self.children: list = []

    def __str__(self):
        return self.text  

    def add_right(self, node):
        self.nxt = node
        node.prev = self

    def add_child(self, node):
        self.children.append(node)
        node.parent = self
