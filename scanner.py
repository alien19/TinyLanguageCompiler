import re
from common import TokenType


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
        '+': TokenType.PLUS,
        '-': TokenType.MINUS,
        '*': TokenType.MULT,
        '/': TokenType.DIVIDE,
        ':=': TokenType.ASSIGN,
        '=': TokenType.EQUAL
    }

    MAP_REGEX_TO_ENUM = {
        '(-)?[0-9]+(.[0-9]+)?(e(\+|-)?[0-9]+)?': TokenType.NUM,
        '[_a-zA-Z]([_a-zA-Z0-9])*': TokenType.ID
    }

    OPERATORS = ["*", "+", "-", "/", ":=", "(", ")", ",", ";"]

    def __init__(self, text: str = ""):
        self.text = text
        self.stringsAndTokens = []

        self.scan()

    def set_text(self, text: str):
        self.text = text

        self.scan()

    def get_strings_and_tokens_list(self):
        return self.stringsAndTokens

    def get_strings_and_tokens_list_as_string(self):
        result = ""
        # Put the strings and tokens on the desired format
        for stringAndToken in self.stringsAndTokens:
            result += ("{}\t{}\n".format(stringAndToken[0], stringAndToken[1].name))
        result = result[:-1]
        return result

    def scan(self):
        self.stringsAndTokens = []
        # Remove comments
        self.text = re.sub('\{(.|\n)*?\}', '', self.text)
        # Split text by lines
        lines = self.text.split("\n")
        # Divide the lines into separatable strings to get the token for each string
        strings = []
        for line in lines:
            for op in Scanner.OPERATORS:
                line = line.replace(op, " " + op + " ")
            line = line.replace("=", " = ")
            line = line.replace(": =", ":=")
            line = line.replace("  ", " ")
            strings += line.split(" ")
        # Remove empty strings from list
        while '' in strings:
            strings.remove('')
        # Identify the suitable token for each string
        for string in strings:
            # If the string is a keyword or a symbol
            if string.lower() in Scanner.MAP_PREDEFINED_TO_ENUM.keys():
                self.stringsAndTokens.append((string, Scanner.MAP_PREDEFINED_TO_ENUM[string.lower()]))
                continue
            isNumOrId = False
            # Check if the string is an identifier or a number
            for regex in Scanner.MAP_REGEX_TO_ENUM.keys():
                if bool(re.match(regex, string)):
                    self.stringsAndTokens.append((string, Scanner.MAP_REGEX_TO_ENUM[regex]))
                    isNumOrId = True
                    continue
            if not isNumOrId:
                # Raise exception if no suitable token was found
                raise Exception("Unknown Token: {}".format(string))


def main():
    # Get input file name
    print("The input file should exist in the same directory as the executable file.")
    inputFileName = input("Enter the input file name:")
    OUTPUT_FILE_NAME = "result.txt"
    # Read file content
    f = open(inputFileName, "r")
    content = "".join(f.readlines())
    # Use the scanner to get the tokens of the text
    scanner = Scanner(content)
    result = scanner.get_strings_and_tokens_list_as_string()
    # Write the strings and the tokens in the output file
    f = open(OUTPUT_FILE_NAME, "w")
    f.write(result)
    f.close()


if __name__ == "__main__":
    main()
