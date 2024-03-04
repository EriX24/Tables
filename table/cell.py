class Cell:
    def __init__(self, cell_name: str, cell_loc: list):
        self.cell_name = cell_name

        self.cell_loc = cell_loc

    def __str__(self):
        return self.cell_name
