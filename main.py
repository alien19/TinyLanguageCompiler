from common import StructType
from compiler import Compiler
from graphviz import Source

f = open("example1.tiny", "r")
content = "".join(f.readlines())
f.close()

c = Compiler(text=content)
it = c.get_parse_tree_iterator()

nodes = {}
sameRank = {}
squares = []
elipses = []
links = []

def iterate(it, index, previous=-1):
    
    if index not in sameRank: sameRank[index] = []
    sameRank[index].append(it.get_node_id())
    nodes[it.get_node_id()] = it
    if previous != -1: links.append((nodes[previous].get_node_id(), it.get_node_id()))
    if it.get_struct_type() == StructType.EXPRESSION: elipses.append(it.get_node_id())
    else: squares.append(it.get_node_id())

    for t in it.children():
        iterate(t, index+1, it.get_node_id())
    if it.has_next():
        iterate(it.next(), index, it.get_node_id())

iterate(it, 0)

graph = """
graph {
    {
SHAPE_GRAPH
    }
SHAPE_LINK
RANK_GRAPH
}
"""

shapes_graph = ""
for id in squares:
    shapes_graph += "\t{} [shape=\"square\" label=\"{}\"]\n".format(id, nodes[id].get_text())
for id in elipses:
    shapes_graph += "\t{} [shape=\"ellipse\" label=\"{}\"]\n".format(id, nodes[id].get_text())
links_graph = ""
for link in links:
    links_graph += "{} -- {};\n".format(link[0], link[1])
rank_graph = ""
for index in sameRank:
    rank_graph += "{rank=same;"
    for i in sameRank[index]:
        rank_graph += i + " ,"
    rank_graph = rank_graph[:-2]
    rank_graph += "}\n"

graph = graph.replace("SHAPE_GRAPH", shapes_graph)
graph = graph.replace("SHAPE_LINK", links_graph)
graph = graph.replace("RANK_GRAPH", rank_graph)

s = Source(graph, filename="test.gv", format="png")
s.view()
