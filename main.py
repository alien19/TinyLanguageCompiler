from common import StructType
from compiler import Compiler
from graphviz import Digraph

# f = open("example1.tiny", "r")
# content = "".join(f.readlines())
# f.close()
#
# c = Compiler(text=content)
# it = c.get_parse_tree_iterator()
#
# def iterate(it, index):
#     for i in range(index):
#         print("\t", end="")
#     print(it.get_text(), it.get_value(), it.get_struct_type())
#     for t in it.children():
#         iterate(t, index+1)
#     if it.has_next():
#         iterate(it.next(), index)
#
#
# iterate(it, 0)

from graphviz import Digraph
from node import Node

# def generate_tree():
#     Nodes = []
#    # global ParseTreeIterator, currentNode, children
#     d = Digraph(name='Syntax Tree', format='png')
#     for Node in Nodes:
#         if(StructType.EXPRESSION):
#              d.node(str(Node.Node),Node.value, shape='circle')
#         elif(StructType.STATEMENT):
#             d.node(str(Node.Node), Node.value, shape ='square')
#         else:
#             d.node(str(Node.Node), Node.value)
#
#     for Node in Nodes:
#         if (Node.parent != 0):
#             d.edge(str(Node.parentNode), str(Node.Node), style='dashed', color='white')
#
#     d.view()
#
# generate_tree()


import graphviz

d = graphviz.Digraph(filename='rank_same.gv')

with d.subgraph() as s:
    s.attr(rank='same')
    s.node('A')
    s.node('X')

d.node('C')

with d.subgraph() as s:
    s.attr(rank='same')
    s.node('B')
    s.node('D')
    s.node('Y')

d.edges(['AB', 'AC', 'CD', 'XY'])

d.view()