class Pyramid:
    def __init__(self, rows):
        self.rows = rows
        self.symbol = '*'

    def print_pyramid(self):
        for i in range(1, self.rows + 1):
            print(' ' * (self.rows - i) + self.symbol * (2 * i - 1))

    def change_symbol(self, symbol):
        self.symbol = symbol

# Example usage:
p = Pyramid(4)
p.print_pyramid()   
p.change_symbol('#')
p.print_pyramid()
