class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def consume(self, expected_kind=None):
        token = self.peek()
        if expected_kind and token[0] != expected_kind:
            raise RuntimeError(f"Expected {expected_kind} but found {token[0]}")
        self.pos += 1
        return token

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.peek()

        if token[0] == 'SET':
            return self.parse_assignment()
        elif token[0] == 'DISPLAY':
            return self.parse_display()
        elif token[0] == 'IF':
            return self.parse_if()
        elif token[0] == 'REPEAT':
            return self.parse_repeat()
        elif token[0] == 'CLASS':
            return self.parse_class()
        else:
            raise RuntimeError(f"Unknown statement: {token[1]}")

    def parse_assignment(self):
        self.consume('SET')
        var_name = self.consume('IDENTIFIER')[1]
        self.consume('TO')
        value = self.consume()[1]
        return ('assign', var_name, value)

    def parse_display(self):
        self.consume('DISPLAY')
        value = self.parse_expression()
        return ('display', value)

    def parse_if(self):
        self.consume('IF')
        left = self.consume('IDENTIFIER')[1]
        self.consume('IS')
        operator = self.consume()[0]  # GREATER or LESS
        right = self.consume('NUMBER')[1]
        self.consume('COLON')
        body = []
        while self.peek()[0] not in ('ELSE', None):
            body.append(self.parse_statement())
        else_body = []
        if self.peek()[0] == 'ELSE':
            self.consume('ELSE')
            while self.peek()[0] not in (None, 'NEWLINE'):
                else_body.append(self.parse_statement())
        return ('if', left, operator, right, body, else_body)

    def parse_repeat(self):
        self.consume('REPEAT')
        times = self.consume('NUMBER')[1]
        self.consume('TIMES')
        self.consume('COLON')
        body = []
        while self.peek()[0] not in (None, 'NEWLINE'):
            body.append(self.parse_statement())
        return ('repeat', times, body)

    def parse_class(self):
        self.consume('CLASS')
        class_name = self.consume('IDENTIFIER')[1]
        self.consume('COLON')
        body = []
        while self.peek()[0] not in (None, 'NEWLINE'):
            body.append(self.parse_statement())
        return ('class', class_name, body)
    
    def parse_expression(self):
        # Parse a simple expression or concatenation
        left = self.consume()
        if self.peek()[0] == 'PLUS':
            self.consume('PLUS')
            right = self.parse_expression()
            return ('concat', left, right)
        return left