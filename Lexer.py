import re
class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.token_spec = [
            ('SET', r'set'),              # 'set' keyword
            ('TO', r'to'),                # 'to' keyword
            ('ADD', r'add'),              # 'add' keyword
            ('SUBTRACT', r'subtract'),    # 'subtract' keyword
            ('DISPLAY', r'display'),      # 'display' keyword
            ('REPEAT', r'repeat'),        # 'repeat' keyword
            ('TIMES', r'times'),          # 'times' keyword
            ('IF', r'if'),                # 'if' keyword
            ('IS', r'is'),                # 'is' keyword
            ('GREATER', r'greater'),      # 'greater' keyword
            ('LESS', r'less'),            # 'less' keyword
            ('ELSE', r'else'),            # 'else' keyword
            ('CLASS', r'class'),          # 'class' keyword
            ('DEFINE', r'define'),        # 'define' keyword
            ('CALL', r'call'),            # 'call' keyword
            ('NEW', r'new'),              # 'new' keyword
            ('STRING', r'"[^"]*"'),       # Strings in double quotes
            ('PLUS', r'\+'),              # Addition/concatenation
            ('IDENTIFIER', r'[a-zA-Z_]+'),# Variable or function names
            ('NUMBER', r'\d+'),           # Numbers
            ('COLON', r':'),              # Colon
            ('NEWLINE', r'\n'),           # Newlines
            ('SKIP', r'[ \t]+'),          # Spaces or tabs
            ('MISMATCH', r'.'),           # Any other character
        ]
        self.token_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_spec))

    def tokenize(self):
        for match in self.token_regex.finditer(self.code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'SKIP' or kind == 'NEWLINE':
                continue
            elif kind == 'MISMATCH':
                position = match.start()
                raise RuntimeError(f"Unexpected character '{value}' at position {position}")
            self.tokens.append((kind, value))
        return self.tokens