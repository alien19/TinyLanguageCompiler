import re
from common import TokenType

# TODO
class Scanner:
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
    '=': TokenType.EQUAL
  }

  MAP_FLEXIBLE_TO_ENUM = {
    '(-)?[0-9]+(.[0-9]+)?(e(\+|-)?[0-9]+)?': TokenType.NUM,
    '[_a-zA-Z]([_a-zA-Z0-9])*': TokenType.ID
  }

  OPERATORS = ["*", "+", "-", "/", ":=", "(", ")", ",", ";"]

  def __init__(self, text:str = ""):
    self.text = text
    self.stringsAndTokens = []

    self.parse()
  
  def set_text(self, text: str):
    self.text = text

    self.parse()
  
  def get_strings_and_tokens_list(self):
    return self.stringsAndTokens
  
  def get_strings_and_tokens_list_as_string(self):
    result = ""

    for stringAndToken in self.stringsAndTokens:
      result += ("{}\t{}\n".format(stringAndToken[0], stringAndToken[1].name))
    result = result[:-1]
    return result
  
  def parse(self):
    self.stringsAndTokens = []
    
    self.text = re.sub('\{(.|\n)*?\}', '', self.text)
    lines = self.text.split("\n")
    strings = []

    for line in lines:
        for op in Scanner.OPERATORS:
            line = line.replace(op, " "+op+" ")
        line = line.replace("=", " = ")
        line = line.replace(": =", ":=")
        line = line.replace("  ", " ")
        strings += line.split(" ")

    while '' in strings:
      strings.remove('')

    for string in strings:
      if string.lower() in Scanner.MAP_PREDEFINED_TO_ENUM.keys():
        self.stringsAndTokens.append((string, Scanner.MAP_PREDEFINED_TO_ENUM[string.lower()]))
        continue
      flag = True
      for regex in Scanner.MAP_FLEXIBLE_TO_ENUM.keys():
        if bool(re.match(regex, string)):
          self.stringsAndTokens.append((string, Scanner.MAP_FLEXIBLE_TO_ENUM[regex]))
          flag = False
          continue
      if flag:
        raise Exception("Unknown Token")


def main():
  # print("The input file should exist in the same directory as the executable file.")
  # inputFileName = input("Enter the input file name:")
  inputFileName = "example1.tiny"
  OUTPUT_FILE_NAME = "result.txt"


  f = open(inputFileName, "r")
  content = "".join(f.readlines())
  scanner = Scanner(content)
  result = scanner.get_strings_and_tokens_list_as_string()
  print("result: {}".format(result))

  
  f = open(OUTPUT_FILE_NAME, "w")
  f.write(result)
  f.close()

if __name__ == "__main__":
  main()




