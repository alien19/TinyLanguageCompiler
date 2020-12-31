from common import StructType
from compiler import Compiler
from graphviz import Source
from exceptions import ScannerError, ParserError

def compile(content):
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
    SHAPE_LINK
    RANK_GRAPH
    ORDER_GRAPH
        {
    SHAPE_GRAPH
        }
    }
    """

    shapes_graph = ""
    for id in squares:
        lbl = nodes[id].get_text() if nodes[id].get_value() is None else nodes[id].get_text() + "\n(" + nodes[id].get_value() + ")"
        shapes_graph += "\t{} [shape=\"square\" label=\"{}\"]\n".format(id, lbl)
    for id in elipses:
        lbl = nodes[id].get_text() if nodes[id].get_value() is None else nodes[id].get_text() + "\n(" + nodes[id].get_value() + ")"
        shapes_graph += "\t{} [shape=\"ellipse\" label=\"{}\"]\n".format(id, lbl)
    links_graph = ""
    for link in links:
        links_graph += "{} -- {};\n".format(link[0], link[1])

    rank_graph = ""
    order_graph = ""

    for index in sameRank:
        rank_graph += "{rank=same;"
        last_index = None
        for i in sameRank[index]:
            rank_graph += i + " ,"
            if last_index is not None: order_graph += "{} -- {} [ style=invis ]\n".format(last_index, i)
            last_index = i
        rank_graph = rank_graph[:-2]
        rank_graph += "}\n"

    processed_links = links_graph.split("\n")
    for a in processed_links:
        if a[:-1] in order_graph: order_graph = order_graph.replace(a[:-1], "")

    processed_order_graph = order_graph.split("\n")
    order_graph = ""
    for a in processed_order_graph:
        if len(a) > 0 and a[0] != " ": order_graph += a + "\n"

    # print(order_graph)
    # print(links_graph)
    graph = graph.replace("SHAPE_GRAPH", shapes_graph)
    graph = graph.replace("SHAPE_LINK", links_graph)
    graph = graph.replace("RANK_GRAPH", rank_graph)
    graph = graph.replace("ORDER_GRAPH", order_graph)

    s = Source(graph, filename="test.gv", format="png")
    s.view()
