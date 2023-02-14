class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


    def __str__(self):
        return f'({self.x},{self.y}),{self.value}'
        #return self.value
