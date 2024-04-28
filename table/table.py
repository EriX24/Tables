# Imports
from colorama import Fore, Style
from table import settings
from table.cell import Cell
import json
import os

# `row` is for `print_table`
row = ""


class Table:
    def __init__(self, columns: list):
        # Create and the columns to the table
        self.table = []
        added_cells = []

        # Can be expressed just by `columns`
        """
        all_columns_key = []
        for name in columns:
            all_columns_key.append(name)
        """

        # Check if a value in columns is invalid
        for heading in columns:
            if isinstance(heading, int) or isinstance(heading, str):
                heading = str(heading)
                if heading is None or heading == "" or len(heading) < 3:
                    if settings.ALLOW_INVALID_ENTRY:
                        dash = "-"
                        blank = ""
                        if not heading:
                            change = "None"
                            heading = ""
                        else:
                            change = "---"[len(heading):]
                        print(
                            f"{Fore.LIGHTYELLOW_EX}Warning!!: {heading+change.replace(dash, blank)} is invalid!! It has been replaced with {heading}{change}{Style.RESET_ALL}"
                        )
                        added_cells.append(Cell(str(f"{heading}{change}")))
                    else:
                        raise ValueError("Headings cannot be `None`, empty or have a length lower than 3")
                else:
                    added_cells.append(Cell(str(heading)))
            else:
                raise TypeError("Headings have to be string or integer")

        # Add the cells to the table
        # added_cells = []
        # for heading in columns:
        #     added_cells.append(Cell(str(heading)))

        self.table.append(added_cells)

        # Get how long `columns` is
        self.variables_in_row = len(columns)

    def add_row(self, *rows: list):
        """ Add a new row to the table """
        for new_row in rows:
            # Get every row

            if len(new_row) > self.variables_in_row:
                if settings.GIVE_WARNING:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}Warning!!: The new row should match"
                        f" the amount of headings!{Style.RESET_ALL}"
                    )
                else:
                    raise AttributeError("The new row should match the amount of headings!")
                return

            # Simplified code after the comment
            """
            if len(appended_row) == self.variables_in_row:
                self.table.append(appended_row)
            else:
                while len(appended_row) != self.variables_in_row:
                    appended_row.append("_")
            """

            # Repeat until all the columns are filled, or show a warning/error
            while len(new_row) != self.variables_in_row:
                if settings.ALLOW_NONE:
                    # Currently '-' acts as None
                    new_row.append("-")
                else:
                    if settings.GIVE_WARNING:
                        print(
                            f"{Fore.LIGHTYELLOW_EX}Warning!!: You are not allowed to insert "
                            f"`None` as a attribute!! To change this go to settings.{Style.RESET_ALL}"
                        )
                    else:
                        raise AttributeError("You are not allowed to insert `None` as a attribute!!"
                                             " To change this go to settings."
                                             )
                    return

            # Add the new row to the table
            added_cells = []
            for cell in new_row:
                added_cells.append(Cell(cell))

            self.table.append(added_cells)

    def assign_value(self, item, row_padding, text):
        """ Used in print_table to decide the value of items """
        # List?
        if isinstance(item.__str__(), list):
            text += f"{Fore.GREEN}<L>{Style.RESET_ALL}" + row_padding[len("<l>"):] + " | "
        # Dict?
        elif isinstance(item.__str__(), dict):
            text += f"{Fore.YELLOW}<D>{Style.RESET_ALL}" + row_padding[len("<d>"):] + " | "
        # String or int? (Default)
        elif isinstance(item.__str__(), str) or isinstance(item.__str__(), int):
            return "Early"
            # text += str(item.__str__()) + row_padding[len(str(item.__str__())):] + " | "
        # A class?
        else:
            text += f"{Fore.BLUE}<O>{Style.RESET_ALL}" + row_padding[len("<o>"):] + " | "
        return text

    def print_table(self):
        """ Use for checking the table """
        global row
        text = "| "
        print_table = []
        row_lengths = []
        for i in self.table[0]:
            row_lengths.append(len(i.__str__()))

        for row in self.table:
            for index in range(len(row)):
                row_length = row_lengths[index]
                row_padding = " " * row_length

                if self.assign_value(row[index], row_padding, text) == "Early":
                    text += str(row[index].__str__()) + row_padding[len(str(row[index].__str__())):] + " | "
                else:
                    text = self.assign_value(row[index], row_padding, text)
                # Working on
                # if len(row[index].__str__()) <= row_length:
                #     text = self.assign_value(row[index], row_padding, text)
                # else:
                #     text = self.assign_value(row[index], row_padding, text)
            print_table.append(text)
            text = "| "

        border = "+" + "-"*(len(print_table[0])-3) + "+"
        print(border)
        print(print_table[0])
        out = ""
        for i in print_table[0]:
            if i == "|":
                out += "+"
            else:
                out += "-"
        print(out[:-1])

        # print("|" + " | ".join([i.__str__() for i in self.table[0]]) + " |")
        for row in print_table[1:]:
            print(row)
        print(border)

    def edit_cell(self, cell_column: int, cell_row: int, new_value: None or str):
        """ Edit a cell directly """
        try:
            # `_` is not needed is why it is _
            _ = self.table[cell_row][cell_column]

        except IndexError:
            if settings.GIVE_WARNING:
                print(f"{Fore.LIGHTYELLOW_EX}Warning!!: Your cell needs to exist to be searched!!{Style.RESET_ALL}")
            else:
                raise AttributeError("Your cell needs to exist to be searched!!")
            return

        else:
            if new_value is None:
                # See if `new_value` is None
                if settings.ALLOW_NONE:
                    self.table[cell_row][cell_column].edit_name("-")
                else:
                    if settings.GIVE_WARNING:
                        print(
                            f"{Fore.LIGHTYELLOW_EX}Warning!!: You are not allowed to insert `None` as a attribute!!"
                            f" To change this go to settings.{Style.RESET_ALL}"
                        )
                    else:
                        raise AttributeError(
                            f"You are not allowed to insert `None` as a attribute!! To change this go to settings."
                        )
                    return
            else:
                # Set the cell to the value if all of above is avoided
                self.table[cell_row][cell_column].edit_name(new_value)

    def save_data(self, table_name: str) -> str:
        """ Returns the path of the saved file and saves the file """
        if os.path.isdir(settings.SAVE_PATH):
            with open(os.path.join(str(settings.SAVE_PATH), str(table_name)), "w") as f:
                json_data = {"data": []}
                for table_row in self.table:
                    filtered_row = []
                    for i in table_row:
                        choices = isinstance(i.__str__(), object) and not isinstance(i.__str__(), list) and not \
                                    isinstance(i.__str__(), dict) and not isinstance(i.__str__(), str) \
                                    and not isinstance(i.__str__(), int)
                        if choices:
                            filtered_row.append("<O>")
                            print(f"{Fore.RED}Alert: You cannot save a object it has been replaced with '<O>'{Style.RESET_ALL}")
                        else:
                            filtered_row.append(i.__str__())

                    json_data["data"].append(filtered_row)

                json.dump(json_data, f)

        return os.path.join(str(settings.SAVE_PATH), str(table_name))
