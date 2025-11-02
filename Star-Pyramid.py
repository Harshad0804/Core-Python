class StarPyramid:
    def __init__(self, rows, symbol='*'):
        self.rows = rows
        self.symbol = symbol

    def __str__(self):
        return f'StarPyramid(rows={self.rows}, symbol="{self.symbol}")'

    def __add__(self, other):
        if isinstance(other, StarPyramid):
            return StarPyramid(self.rows + other.rows, self.symbol)
        return NotImplemented

    def __eq__(self, other):
        return self.rows == other.rows and self.symbol == other.symbol

    def print_pyramid(self):
        for i in range(self.rows):
            print(' ' * (self.rows - i - 1) + (self.symbol + ' ') * (i + 1))

    def change_symbol(self, new_symbol):
        self.symbol = new_symbol

# Usage:
pyramid1 = StarPyramid(5)
pyramid1.print_pyramid()       
pyramid2 = StarPyramid(3, '#')
pyramid2.print_pyramid()       

pyramid3 = pyramid1 + pyramid2 
print(pyramid3)                

pyramid3.change_symbol('$')
pyramid3.print_pyramid()
