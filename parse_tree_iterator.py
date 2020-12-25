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
