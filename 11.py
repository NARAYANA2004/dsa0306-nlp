class Parser:
    def _init_(self, grammar):
        self.grammar = grammar

    def parse(self, input_str):
        self.input_str = input_str
        self.pos = 0
        self.current_token = None
        self.next_token()
        if self.S():
            if self.current_token is None:
                return True
        return False

    def next_token(self):
        if self.pos < len(self.input_str):
            self.current_token = self.input_str[self.pos]
            self.pos += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.next_token()
            return True
        return False

    def S(self):
        return self.A() and self.B()

    def A(self):
        if self.match('a'):
            return True
        elif self.EPSILON():
            return True
        return False

    def B(self):
        return self.match('b')

    def EPSILON(self):
        return True


# Example usage:
grammar = {
    'S': ['AB'],
    'A': ['a', ''],
    'B': ['b']
}

parser = Parser(grammar)
input_str = 'ab'
print(parser.parse(input_str))  # Output: True
