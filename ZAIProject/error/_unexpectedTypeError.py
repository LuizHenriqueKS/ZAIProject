class UnexpectedTypeError(Exception):
    def __init__(self, data, expectedType):
        self.data = data
        self.expectedType = expectedType

    def __str__(self):
        return f'Excepted "{self.data}" be {self.expectedType}'
