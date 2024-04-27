from table.table import Table

# make a new table
new_table = Table(columns=["Heading 1", "Heading 2", "Heading 3"])

# Add new row(s)
new_table.add_row(["1"], ["2"], ["3"], ["4"], [["5"], new_table.edit_cell, {"jk": "jk"}])

# Edit a cell
new_table.edit_cell(cell_row=5, cell_column=7, new_value=None)  # Error

# Print the table
new_table.print_table()

# Save the table
path = new_table.save_data("new_table")
