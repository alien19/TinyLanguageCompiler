from enum import Enum, auto
import re
from common import TokenType

# TODO
class Scanner:
  pass


MAP_PREDEFINED_TO_ENUM = {
  'if': TokenType.IF,
  'then': TokenType.THEN,
  'else': TokenType.ELSE,
  'write': TokenType.WRITE,
  'read': TokenType.READ,
  'end': TokenType.END,
  'repeat': TokenType.REPEAT,
  'until': TokenType.UNTIL,
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
}

MAP_FLEXIBLE_TO_ENUM = {
  '(-)?[0-9]+(.[0-9]+)?(e(\+|-)?[0-9]+)?': TokenType.NUM,
  '[_a-zA-Z]([_a-zA-Z0-9])*': TokenType.ID
}

print("The input file should exist in the same directory as the executable file.")
inputFileName = input("Enter the input file name:")
OUTPUT_FILE_NAME = "result.txt"

# FILE_PATH = "example1.tiny"
OPERATORS = ["*", "+", "-", "/", ":=", "(", ")", ",", ";"]

f = open(inputFileName, "r")
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
f = open(OUTPUT_FILE_NAME, "w")
f.write(result)
f.close()


