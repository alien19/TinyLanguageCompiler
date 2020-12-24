<<<<<<< Updated upstream
from common import TokenType, StructType

# TODO
||||||| constructed merge base
# TODO
=======
# from common import StructType, TokenType


>>>>>>> Stashed changes
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
