FILE_PATH = "test.tiny"
OPERATORS = ["*", "+", "-", "/", "="]

TOKEN_TYPE = {
    "if": "IF",
    "begin":"BEGIN"
}

f = open(FILE_PATH, "r")
content = "".join(f.readlines())
lines = content.split("\n")
tokens = []

for line in lines:
    for op in OPERATORS:
        line = line.replace(op, " "+op+" ")
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")
    line = line.replace("  ", " ")
    line = line.replace(",", " , ")
    line = line.replace(";", " ; ")
    tokens += line.split(" ")

while "" in tokens:
    tokens.remove("")

print(tokens)

print(token, map[token])