# TODO
class Node:
    def __init__(self, text:str, value: str, structVal: StructType, tokenType: TokenType):
      self.text:str = text
      self.value:str = value
      self.structVal:StructType = structVal
      self.tokenType:TokenType = tokenType
      self.nxt:Node = None
      self.prev:Node = None
      self.parent:Node = None
      self.children:list = []
    
    def add_child(node:Node):
      pass
