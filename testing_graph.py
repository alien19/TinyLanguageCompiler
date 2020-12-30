from graphviz import Source
temp = """
graph {
0 -- 20;
20 -- 2;
2 -- 1;
2 -- 3;
20 -- 5;
5 -- 4;
5 -- 17;
17 -- 9;
9 -- 7;
7 -- 6;
7 -- 8;
9 -- 13;
13 -- 11;
11 -- 10;
11 -- 12;
17 -- 15;
15 -- 14;
15 -- 16;
17 -- 19;
19 -- 18;

0 -- 20 [ style=invis ]
2 -- 5 -- 17 -- 19 [ style=invis ]
1 -- 3 -- 4 -- 9 -- 13 -- 15 -- 18 [ style=invis ]
7 -- 11 -- 14 -- 16 [ style=invis ]
6 -- 8 -- 10 -- 12 [ style=invis ]

{rank=same;0 ,20}
{rank=same;2 ,5 ,17 ,19}
{rank=same;1 ,3 ,4 ,9 ,13 ,15 ,18}
{rank=same;7 ,11 ,14 ,16}
{rank=same;6 ,8 ,10 ,12}

{
    0 [shape="square" label="read"]
    20 [shape="square" label="if"]
    2 [shape="ellipse" label="op"]
    5 [shape="square" label="assign"]
    17 [shape="square" label="repeat"]
    9 [shape="square" label="assign"]
    13 [shape="square" label="assign"]
    19 [shape="square" label="write"]
    1 [shape="ellipse" label="const"]
    3 [shape="ellipse" label="id"]
    4 [shape="ellipse" label="const"]
    7 [shape="ellipse" label="op"]
    6 [shape="ellipse" label="id"]
    8 [shape="ellipse" label="id"]
    11 [shape="ellipse" label="op"]
    10 [shape="ellipse" label="id"]
    12 [shape="ellipse" label="const"]
    15 [shape="ellipse" label="op"]
    14 [shape="ellipse" label="id"]
    16 [shape="ellipse" label="const"]
    18 [shape="ellipse" label="id"]
}

}
"""

s = Source(temp, filename="test.gv", format="png")
s.view()