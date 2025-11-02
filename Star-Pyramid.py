class StarPyramid:
    def __init__(self, rows, symbol='*'):
        self.rows = rows
        self.symbol = symbol

    def __str__(self):
        return f'StarPyramid(rows={self.rows}, symbol="{self.symbol}")'

    def __add__(self, other):
        # Adds two pyramids by combining their row counts
        if isinstance(other, StarPyramid):
            return StarPyramid(self.rows + other.rows, self.symbol)
        return NotImplemented

    def __eq__(self, other):
        # Compare pyramid sizes
        return self.rows == other.rows and self.symbol == other.symbol

    def print_pyramid(self):
        # User-defined function: prints pyramid pattern
        for i in range(self.rows):
            print(' ' * (self.rows - i - 1) + (self.symbol + ' ') * (i + 1))

    def change_symbol(self, new_symbol):
        # Another user-defined function to change the symbol
        self.symbol = new_symbol

# Usage:
pyramid1 = StarPyramid(5)
pyramid1.print_pyramid()       # Prints star pyramid
pyramid2 = StarPyramid(3, '#')
pyramid2.print_pyramid()       # Prints hash pyramid

pyramid3 = pyramid1 + pyramid2 # Uses __add__ method
print(pyramid3)                # Uses __str__

# Change symbol and reprint
pyramid3.change_symbol('$')
pyramid3.print_pyramid()
