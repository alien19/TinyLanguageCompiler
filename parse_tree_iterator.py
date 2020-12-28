from __future__ import annotations

from common import StructType
from node import Node


class ParseTreeIterator:
    def __init__(self, node: Node):
        self.node = node

    def next(self) -> ParseTreeIterator:
        return ParseTreeIterator(self.node.nxt)

    def prev(self) -> ParseTreeIterator:
        return ParseTreeIterator(self.node.prev)

    def get_text(self) -> str:
        return str(self.node)

    def get_value(self) -> str:
        return self.node.value

    # def get_token_type(self):
    #   return self.node.tokenType

    def get_struct_type(self) -> StructType:
        return self.node.structType

    def children(self) -> list:
        itrs = [ParseTreeIterator(child) for child in self.node.children]
        return itrs

    def has_next(self) -> bool:
        return self.node.nxt is not None

    def has_previous(self) -> bool:
        return self.node.prev is not None

    def has_children(self) -> bool:
        return len(self.node.children) > 0
