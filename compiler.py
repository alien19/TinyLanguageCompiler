from code_parser import Parser
from scanner import Scanner


class Compiler:
    def __init__(self, text: str):
        self.scanner: Scanner = Scanner(text)
        stringsAndTokens = self.scanner.get_strings_and_tokens_list()
        self.parser: Parser = Parser(stringsAndTokens)

    def set_text(self, text: str):
        self.scanner.set_text(text)
        stringsAndTokens = self.scanner.get_strings_and_tokens_list()
        self.parser.set_strings_and_tokens(stringsAndTokens)

    def get_parse_tree_iterator(self):
        return self.parser.get_parse_tree_iterator()


if __name__ == "__main__":
    # Get input file name
    # print("The input file should exist in the same directory as the executable file.")
    # inputFileName = input("Enter the input file name:")
    inputFileName = "example1.tiny"
    OUTPUT_FILE_NAME = "result.txt"
    # Read file content
    f = open(inputFileName, "r")
    content = "".join(f.readlines())
    # Use the scanner to get the tokens of the text
    scanner = Compiler(content)
    # Write the strings and the tokens in the output file
    # f = open(OUTPUT_FILE_NAME, "w")
    # f.write(result)
    # f.close()