from graphviz import Source
temp = """
graph {
    {
        0 [shape="square" label="Ali"]
    }
0 -- b;
b -- c;
b -- d;
{ rank=same; b, 0 }
}
"""

s = Source(temp, filename="test.gv", format="png")
s.view()