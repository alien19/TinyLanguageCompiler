# from common import StructType, TokenType

class Node:
    def __init__(self, text: str, value: str, structVal, tokenType):
        self.text: str = text
        self.value: str = value
        self.structVal = structVal
        self.tokenType = tokenType
        self.nxt: Node = None
        self.prev: Node = None
        self.parent: Node = None
        self.children: list = []   

    def add_child(self, node):
        self.children.append(node)
