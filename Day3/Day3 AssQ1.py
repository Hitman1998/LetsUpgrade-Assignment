class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return print(self.a + self.b)


c = Sum(int(input()), int(input()))
c.sum()