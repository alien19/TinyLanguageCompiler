from node import Node

class ParseTreeIterator:
    def __init__(self, node):
      self.node = node

    def nxt(self):
      return ParseTreeIterator(self.node.nxt)

    def prev(self):
      return ParseTreeIterator(self.node.prev)    

    def get_text(self):
      return str(self.node)

    def get_value(self):
      return self.node.value

    # def get_token_type(self):
    #   return self.node.tokenType

    def get_struct_type(self):
      return self.node.structType

    def children(self):
      itrs = [ParseTreeIterator(child) for child in children]
      return itrs

    def has_next(self):
      return self.node.nxt is not None

    def has_previous(self):
      return self.node.prev is not None

    def has_children(self):
      return len(self.node.children) > 0
      
