from node import Node
from parse_tree_iterator import ParseTreeIterator


class ParseTree:
    def __init__(self):
        self.root: Node = None
        self.currentNode: Node = None

    def iterator(self) -> ParseTreeIterator:
        if self.is_empty():
            return None
        return ParseTreeIterator(self.root)

    def set_root(self, node: Node) -> None:
        self.root = node

    def is_empty(self) -> bool:
        return self.root is None

    # def go_left(self):
    #     tmp_node = self.currentNode
    #     self.currentNode = self.currentNode.prev
    #     self.currentNode.nxt = tmp_node

    # def go_right(self):
    #     tmp_node = self.currentNode
    #     self.currentNode = self.currentNode.nxt
    #     self.currentNode.prev = tmp_node

    # def go_child(self, index: int):
    #     tmp_node = self.currentNode
    #     self.currentNode = self.currentNode.children[index]
    #     self.currentNode.parent = tmp_node

    # def go_first_child(self):
    #     tmp_node = self.currentNode
    #     self.currentNode = self.currentNode.children[index]
    #     self.currentNode.parent = tmp_node

    # def go_last_child(self):
    #     tmp_node = self.currentNode
    #     n_children = len(cur.children)
    #     self.currentNode = cur.children[n_children - 1]
    #     self.currentNode.parent = tmp_node

    # def go_top(self):
    #     tmp_node = self.currentNode
    #     self.currentNode = self.currentNode.parent
    #     self.currentNode.prev = tmp_node

    # def insert_right(self, text: str, value: str, structType: StructType, tokenType: TokenType):
    #     # Insert a̶n̶d̶ g̶o̶ t̶o̶ t̶h̶e̶ r̶i̶g̶h̶t̶
    #     insertedNode = Node(text, value, structType, tokenType)
    #     if self.root is None:
    #         self.root = insertedNode
    #     else:
    #         self.currentNode.nxt = insertedNode

    # def insert_child(self, text: str, value: str, structType: StructType, tokenType: TokenType):
    #     # Insert a̶n̶d̶ g̶o̶ t̶o̶ t̶h̶e̶ c̶h̶i̶l̶d̶
    #     insertedNode = Node(text, value, structType, tokenType)
    #     if self.root is None:
    #         self.root = insertedNode
    #     else:
    #         self.currentNode.add_child(insertedNode)

    # def insert_right_node(self, node: Node):
    #     # Insert a̶n̶d̶ g̶o̶ t̶o̶ t̶h̶e̶ r̶i̶g̶h̶t̶
    #     if self.root is None:
    #         self.root = node
    #     else:
    #         self.currentNode.nxt = node

    # def insert_child(self, node: Node):
    #     # Insert a̶n̶d̶ g̶o̶ t̶o̶ t̶h̶e̶ c̶h̶i̶l̶d̶
    #     if self.root is None:
    #         self.root = node
    #     else:
    #         self.currentNode.add_child(node)
