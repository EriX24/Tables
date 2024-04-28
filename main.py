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

# Cool patterns (not sure why the 'moore' doesn't work, code is from YongbinFan)
pattern = Table(columns=["H", "H", "H", "H", "H", "H", "H", "H", "H"])

pattern.add_row([], [], [], [], [], [], [], [], [], [])

res = []

coordinates = [5, 4]

distance = 3

moore_var = [(i, j) for i in range(distance - 1, distance + 1) for j in range(distance - 1, distance + 1) if
             (i, j) != (0, 0)]

van_var = [(i, j) for i in range(0, distance + 1) for j in range(distance + 1) if
           (i, j) != (0, 0) and i + j <= distance]

van_change = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

van_var_set = {(cell_x * change_x, cell_y * change_y) for cell_x, cell_y in van_var for change_x, change_y in
               van_change}

for i, j in van_var_set:  # Change 'van_var_set' to moore_var if you want to see the one that doesn't work
    if True:
        res.append([coordinates[0] + i, coordinates[1] + j])

for i in res:
    pattern.edit_cell(cell_row=i[0], cell_column=i[1], new_value=[])

pattern.print_table()
