from common import StructType
from compiler import Compiler
from graphviz import Digraph

f = open("example1.tiny", "r")
content = "".join(f.readlines())
f.close()

c = Compiler(text=content)
it = c.get_parse_tree_iterator()

# f = Digraph('finite_state_machine', filename='fsm.png')
# f.attr(rankdir='LR', size='8,5')

# f.attr('node', shape='circle')

nodes = {}
sameRank = {}
links = []

def iterate(it, index, previous=-1):
    
    if index not in sameRank: sameRank[index] = []
    sameRank[index].append(it.get_node_id())
    nodes[it.get_node_id()] = it
    if previous != -1: links.append((nodes[previous].get_text(), it.get_text()))
    
    for t in it.children():
        iterate(t, index+1, it.get_node_id())
    if it.has_next():
        iterate(it.next(), index, it.get_node_id())

iterate(it, 0)

print(sameRank)
print(links)