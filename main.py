from table.table import Table

new_table = Table(columns=["Heading 1", "Heading 2", "Heading 3"])

new_table.add_row(["1"], ["2"], ["3"], ["4"], ["5", "a", "jk"])
# new_table.add_row(row=["2"])
# new_table.add_row(row=["3"])
# new_table.add_row(row=["4"])
# new_table.add_row(row=["5"])

new_table.edit_cell(cell_row=5, cell_column=7, new_value=None)

new_table.print_table()
