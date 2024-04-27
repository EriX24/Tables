class Cell:
    def __init__(self, cell_value):
        self.cell_value = cell_value

    def __str__(self):
        return self.cell_value

    def edit_name(self, new_value):
        self.cell_value = new_value
