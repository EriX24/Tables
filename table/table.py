# Imports
from colorama import Fore, Style
from table import settings

# `row` is for `print_table`
row = ""


class Table:
    def __init__(self, columns):
        # Create and the columns to the table
        self.table = []

        # Can be expressed just by `columns`
        """
        all_columns_key = []
        for name in columns:
            all_columns_key.append(name)
        """

        # Add the `columns` to the table
        self.table.append(columns)

        # Get how long `columns` is
        self.variables_in_row = len(columns)

    def add_row(self, *rows):
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
            self.table.append(new_row)

    def print_table(self):
        """ Use for debugging ONLY!! """
        global row
        text = "| "
        print_table = []

        for row in self.table:
            for index in range(len(row)):
                text += row[index] + " | "
            print_table.append(text)
            text = "| "

        table_extra = "+"
        for i in self.table[0]:
            for _ in range(len(i) + len(self.table[0])):
                table_extra += "-"
        table_extra += "+"

        print(table_extra)

        for row in print_table:
            print(row)

        print(table_extra)

    def edit_cell(self, cell_column, cell_row, new_value):
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
                    self.table[cell_row][cell_column] = "-"
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
                self.table[cell_row][cell_column] = new_value
