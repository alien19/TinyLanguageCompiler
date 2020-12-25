from common import TokenType, StructType
from parse_tree import ParseTree
from node import Node
from parse_tree_iterator import ParseTreeIterator


class Parser:
    STATEMENT_TOKENS = [TokenType.IF, TokenType.REPEAT, TokenType.READ, TokenType.WRITE, TokenType.ID]
    COMPARISON_OP_TOKENS = [TokenType.EQUAL, TokenType.LESS_THAN]
    ADD_OP_TOKENS = [TokenType.PLUS, TokenType.MINUS]
    MUL_OP_TOKENS = [TokenType.MULT, TokenType.DIVIDE]

    def __init__(self, stringsAndTokens: list = []):
        self.stringsAndTokens = stringsAndTokens
        self.currentIndex = 0
        self.parseTree = None
        self.parse()

    def set_strings_and_tokens(self, stringsAndTokens: list) -> None:
        self.stringsAndTokens = stringsAndTokens
        self.currentIndex = 0
        self.parseTree: ParseTree = None
        self.parse()

    def get_parse_tree_iterator(self) -> ParseTreeIterator:
        if self.parseTree is None:
            return None
        else:
            return self.parseTree.iterator()

    def has_finished(self) -> bool:
        return self.currentIndex >= len(self.stringsAndTokens)

    def current_token(self) -> TokenType:
        return self.stringsAndTokens[self.currentIndex][1]

    def current_string(self) -> str:
        return self.stringsAndTokens[self.currentIndex][0]

    def parse(self):
        seqNode = self.get_stmt_seq_node()
        self.parseTree = ParseTree()
        self.parseTree.set_root(seqNode)

    def get_stmt_seq_node(self) -> Node:
        node: Node = None
        currentNode: Node = None
        while not self.has_finished():
            if self.current_token() not in Parser.STATEMENT_TOKENS:
                break
            addedNode = self.get_stmt_node()
            if node is None:
                node = addedNode
                currentNode = addedNode
            else:
                currentNode.add_right(addedNode)
                currentNode = addedNode
            if not self.has_finished():
                if self.current_token() == TokenType.SEMICOLON:
                    self.currentIndex += 1
        return node

    def get_stmt_node(self) -> Node:
        currentToken = self.current_token()
        node = None
        # Get the required node depending on the TokenType of the current token
        # In case of if statement
        if currentToken == TokenType.IF:
            node = self.get_if_stmt_node()
        # In case of repeat statement
        elif currentToken == TokenType.REPEAT:
            node = self.get_repeat_stmt_node()
        # In case of read statement
        elif currentToken == TokenType.READ:
            node = self.get_read_stmt_node()
        # In case of write statement
        elif currentToken == TokenType.WRITE:
            node = self.get_write_stmt_node()
        # In case of assign statement
        elif currentToken == TokenType.ID:
            node = self.get_assign_stmt_node()
        return node

    def get_if_stmt_node(self) -> Node:
        # Skip the "if" keyword
        self.currentIndex += 1
        # Get the exp node
        expNode = self.get_exp_node()
        # Skip the "then" keyword
        self.currentIndex += 1
        # Get the "then" statement sequence
        thenStmtSeqNode = self.get_stmt_seq_node()
        # Check if "else" exists
        elseStmtSeqNode = None
        if self.current_token() == TokenType.ELSE:
            # Skip the "else" keyword
            self.currentIndex += 1
            # Get the "else" statement sequence
            elseStmtSeqNode = self.get_stmt_seq_node()
        # Skip the "end" keyword
        self.currentIndex += 1
        # Create the "if" statement node
        node = Node("if", None, StructType.STATEMENT)
        node.add_child(expNode)
        node.add_child(thenStmtSeqNode)
        if elseStmtSeqNode is not None:
            node.add_child(elseStmtSeqNode)
        return node

    def get_repeat_stmt_node(self) -> Node:
        # Skip "repeat" keyword
        self.currentIndex += 1
        # Get statement sequence
        stmtSeqNode = self.get_stmt_seq_node()
        # Skip "until" keyword
        self.currentIndex += 1
        # Get exp node
        expNode = self.get_exp_node()
        # Create "repeat" statement node
        node = Node("repeat", None, StructType.STATEMENT)
        node.add_child(stmtSeqNode)
        node.add_child(expNode)
        return node

    def get_read_stmt_node(self) -> Node:
        # Skip "read" keyword
        self.currentIndex += 1
        # Get identifier string
        identifier = self.current_string()
        # Skip the identifier
        self.currentIndex += 1
        # Create "read" statement node
        node = Node("read", identifier, StructType.STATEMENT)
        return node

    def get_write_stmt_node(self) -> Node:
        # Skip "write" keyword
        self.currentIndex += 1
        # Get exp node
        expNode = self.get_exp_node()
        # Create "write" statement node
        node = Node("write", None, StructType.STATEMENT)
        node.add_child(expNode)
        return node

    def get_assign_stmt_node(self) -> Node:
        # Get identifier string
        identifier = self.current_string()
        # Skip identifier
        self.currentIndex += 1
        # Skip assign ":=" symbol
        self.currentIndex += 1
        # Get exp node
        expNode = self.get_exp_node()
        # Create the "assign" statement node
        node = Node("assign", identifier, StructType.STATEMENT)
        node.add_child(expNode)
        return node

    def get_exp_node(self) -> Node:
        # Get a simple exp
        simpleExpNode1: Node = self.get_simple_exp_node()
        # Create other variables for in case there was an comparison op
        compOpNode: Node = None
        simpleExpNode2: Node = None
        # Variable used to know if the the expression is just a simple expression or it contains a comparison op
        simpleExpOnly = True
        if not self.has_finished():
            # Check if there is a comparison op
            if self.current_token() in Parser.COMPARISON_OP_TOKENS:
                simpleExpOnly = False
                # Get the nodes of the comparison op and the other simple expression
                compOpNode = self.get_op_node()
                simpleExpNode2 = self.get_simple_exp_node()
        # Checks if it is a simple expression only
        if simpleExpOnly:
            node = simpleExpNode1
        # In case there was a comparison op
        else:
            compOpNode.add_child(simpleExpNode1)
            compOpNode.add_child(simpleExpNode2)
            node = compOpNode
        return node

    def get_simple_exp_node(self) -> Node:
        # Initialize lists
        termsNodes = []
        addOpsNodes = []
        # Add a term because there must be at least 1 term
        termsNodes.append(self.get_term_node())
        # Keep adding the repeated pattern which is "addop term"
        while not self.has_finished():
            if self.current_token() in Parser.ADD_OP_TOKENS:
                addOpsNodes.append(self.get_op_node())
                termsNodes.append(self.get_term_node())
            else:
                break
        # Get and return the tree created from connecting the terms nodes and the add ops nodes in the right order
        return self.get_ops_tree(termsNodes, addOpsNodes)

    def get_term_node(self) -> Node:
        # Initialize lists
        factorsNodes = []
        mulOpsNodes = []
        # Add a factor because there must be at least 1 factor
        factorsNodes.append(self.get_factor_node())
        # Keep adding the repeated pattern which is "multop factor"
        while not self.has_finished():
            if self.current_token() in Parser.MUL_OP_TOKENS:
                mulOpsNodes.append(self.get_op_node())
                factorsNodes.append(self.get_factor_node())
            else:
                break
        # Get and return the tree created from connecting the factors nodes and the mul ops nodes in the right order
        return self.get_ops_tree(factorsNodes, mulOpsNodes)

    def get_factor_node(self) -> Node:
        node: Node = None
        currentToken = self.current_token()
        currentString = self.current_string()
        if currentToken == TokenType.ID:
            node = Node("id", currentString, StructType.EXPRESSION)
            # Skip the identifier
            self.currentIndex += 1
        elif currentToken == TokenType.NUM:
            node = Node("const", currentString, StructType.EXPRESSION)
            # Skip the number
            self.currentIndex += 1
        elif currentToken == TokenType.OPEN_PARAN:
            # Skip open paran "("
            self.currentIndex += 1
            # Get exp node
            node = self.get_exp_node()
            # Skip close paran ")"
            self.currentIndex += 1
        return node

    def get_ops_tree(self, valuesNodes: list, opsNodes: list) -> Node:
        opsNodesLength = len(opsNodes)
        # Initialize the nodes variables
        leftNode: Node = valuesNodes[0]
        centerNode: Node = valuesNodes[0]
        # Create the tree
        for i in range(opsNodesLength):
            # Left node is the center node from the previous iteration
            # Right node is the next value
            rightNode = valuesNodes[i + 1]
            # The center node is the op node
            centerNode = opsNodes[i]
            # Add both sides of the op node as children to the op node
            centerNode.add_child(leftNode)
            centerNode.add_child(rightNode)
            # Update the value of the left node for the next iteration
            leftNode = centerNode
        # The result is the center node
        node = centerNode
        return node

    def get_op_node(self) -> Node:
        # Create the "op" node
        node = Node("op", self.current_string(), StructType.EXPRESSION)
        # Skip the op
        self.currentIndex += 1
        return node
