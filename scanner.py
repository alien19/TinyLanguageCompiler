from enum import Enum, auto
import re

class TokenType(Enum):
  IF = auto()
  THEN = auto()
  ELSE = auto()
  WRITE = auto()
  READ = auto()
  UNTIL = auto()
  # BEGIN = auto()
  END = auto()
  # MAIN = auto()
  # STRING = auto()
  # REAL = auto()
  # INT = auto()
  # RETURN = auto()
  REPEAT = auto()

  SEMICOLON = auto()
  OPEN_PARAN = auto()
  CLOSE_PARAN = auto()
  LESS_THAN = auto()
  # COMMA = auto()
  PLUS = auto()
  MINUS = auto()
  MULT = auto()
  DIVIDE = auto()
  ASSIGN = auto()
  EQUAL = auto()
  # NOT_EQUAL = auto()

  NUM = auto()
  ID = auto()

MAP_PREDEFINED_TO_ENUM = {
  'if': TokenType.IF,
  'then': TokenType.THEN,
  'else': TokenType.ELSE,
  'write': TokenType.WRITE,
  'read': TokenType.READ,
  # 'begin': TokenType.BEGIN,
  'end': TokenType.END,
  'repeat': TokenType.REPEAT,
  'until': TokenType.UNTIL,
  # 'main': TokenType.MAIN,
  # 'string': TokenType.STRING,
  # 'real': TokenType.REAL,
  # 'int': TokenType.INT,
  # 'return': TokenType.RETURN,
  ';': TokenType.SEMICOLON,
  '(': TokenType.OPEN_PARAN,
  ')': TokenType.CLOSE_PARAN,
  '<': TokenType.LESS_THAN,
  # ',': TokenType.COMMA,
  '+': TokenType.PLUS,
  '-': TokenType.MINUS,
  '*': TokenType.MULT,
  '/': TokenType.DIVIDE,
  ':=': TokenType.ASSIGN,
  '=': TokenType.EQUAL,
  # '==': TokenType.EQUAL,
  # '!=': TokenType.NOT_EQUAL,
}

MAP_FLEXIBLE_TO_ENUM = {
  # '(-)?[0-9]+(.[0-9]+)?(e(+|-)?[0-9]+)?': TokenType.NUM,
  '(-)?[0-9]+(.[0-9]+)?(e(\+|-)?[0-9]+)?': TokenType.NUM,
  '[_a-zA-Z]([_a-zA-Z0-9])*': TokenType.ID
}

FILE_PATH = "example1.tiny"
OPERATORS = ["*", "+", "-", "/", ":=", "(", ")", ",", ";"]

f = open(FILE_PATH, "r")
content = "".join(f.readlines())
content = re.sub('\{(.|\n)*?\}', '', content)
lines = content.split("\n")
strings = []

for line in lines:
    for op in OPERATORS:
        line = line.replace(op, " "+op+" ")
    line = line.replace("=", " = ")
    line = line.replace(": =", ":=")
    line = line.replace("  ", " ")
    strings += line.split(" ")

while '' in strings:
  strings.remove('')
print(strings)

stringsAndTokens = []

for string in strings:
  if string.lower() in MAP_PREDEFINED_TO_ENUM.keys():
    stringsAndTokens.append((string, MAP_PREDEFINED_TO_ENUM[string.lower()]))
    continue
  flag = True
  for regex in MAP_FLEXIBLE_TO_ENUM.keys():
    if bool(re.match(regex, string)):
      stringsAndTokens.append((string, MAP_FLEXIBLE_TO_ENUM[regex]))
      flag = False
      continue
  if flag:
    print(string)
    raise Exception("Unknown Token")

result = ""

for stringAndToken in stringsAndTokens:
  result += ("{}\t{}\n".format(stringAndToken[0], stringAndToken[1].name))

result = result[:-1]
f = open("result.txt", "w")
f.write(result)
f.close()

print(result)


