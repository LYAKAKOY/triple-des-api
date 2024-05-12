class TextError(Exception):

    def __init__(self):
        super().__init__("Text must be 64 lenght and contains 0 and 1")


class KeyError(Exception):

    def __init__(self):
        super().__init__("Text must be 16 lenght and contains hex symbol")
