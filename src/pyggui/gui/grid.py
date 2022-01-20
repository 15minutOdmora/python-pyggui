"""

"""

from typing import Union, List, Tuple

import pygame

from pyggui.gui.item import Item


class Cell(StaticItem):
    def __init__(
        self,
        grid: Grid,
        position_in_grid: Tuple,
        position: List[int] = [0, 0],
        size: Tuple[int, int] = (1, 1),
    ):
        """
        Args:
            position (List[int] = [0, 0]): Position to place item on screen (or on page).
            size (Tuple[int, int] = (1, 1)): Size of item.
            visible (bool): If item is currently visible.
            selected (bool): If item is currently selected.
        """
        super().__init__(position, size, False, False)
        self.grid = grid

        # Possible alignments
        self.alignments = {
            "left": self._left,
            "right": self._right,
            "top": self._top,
            "bottom": self._bottom,
            "centre": self._centre,
            None: self._centre
        }
        # Possible paddings
        self._padding = {
            "top": 0,
            "bottom": 0,
            "left": 0,
            "right": 0
        }

    @property
    def padding(self):
        return self._padding

    @padding.setter
    def padding(self, padding):
        # Todo
        pass

    def _left(self, item: any) -> None:
        """
        Method aligns item to the left side of cell.
        """
        item.position = (self.position[0], item.position[1])

    def _right(self, item: any) -> None:
        """
        Method aligns item to the right side of cell.
        """
        # Set right cell border to match item right side
        diff = (self.width - item.width) if self.width > item.width else 0
        # Set new x position
        item.position = (self.position[0] + diff, item.position[1])

    def _top(self, item: any) -> None:
        """
        Method aligns item to the top side of cell.
        """
        # Set top borders to match
        item.position = (item.position[0], self.position[1])

    def _bottom(self, item: any) -> None:
        """
        Method aligns item to the bottom side of cell.
        """
        # Set bottom cell border to match item bottom
        diff = (self.height - item.height) if self.height > item.height else 0
        item.position = (item.position[0], self.position[1] + diff)

    def _centre(self, item: any) -> None:
        """
        Method aligns item so its centre matches the cells centre.
        """
        # Item centre is at cell centre
        centered_x = self.position[0] + ((self.width - item.width) // 2)
        centered_y = self.position[1] + ((self.height - item.height) // 2)
        item.position = (centered_x, centered_y)

    def resize(self, width: int = None, height: int = None) -> None:
        """
        Todo

        Args:
            width ():
            height ():

        Returns:

        """
        if not (width and height):
            return

    def __pad(self, item: any, padding: str, value: int) -> None:
        """
        Method adds padding to item based on cell position and size.

        Args:
            item (any): Item to pad.
            padding (str): Padding type (top, bottom, left, right).
            value (int): Number of px to pad.
        """
        if paddin in self.padding.keys():
            if padding == "top":
                item.y += value
            elif padding == "bottom":
                item.y -= value
            elif padding == "left":
                item.x += value
            elif padding == "right":
                item.x -= value

    def add_item(self, item: any, alignment: str = None, padding: str = None) -> None:
        """
        Method adds item to cell, aligns and pads it base on passed values.

        Args:
            item (any): Item to add.
            alignment (str): String defining alignment type. Multiple alignments are separated by a space character.
                Example: alignment = "centre top"  # Centre should always be first.
            padding (str): String defining padding of item. Multiple alignments are separated by a comma. Value is
                passed next to the alignment position as an integer value.
                Example: padding = "top 5, left 3"  # 5px from top 3px from bottom
        """
        self.items.append(item)  # Add item to item list
        # Handle alignment
        if alignment:
            for align in alignment.split(" "):  #
                if align in self.alignments:
                    self.alignments[align](item)  # Align item in set way
        else:
            self.alignments[alignment](item)  # Default alignment for None is centre
        # Handle padding
        if padding:
            for pad in padding.split(","):  # Go over each padding
                pad.strip()  # Remove whitespace around
                _pad = pad.split(" ")
                key, value = _pad[0], int(_pad[1])  # Todo add exception handling
                self.__pad(item, padding=key, value=value)

    def update(self):
        for item in self.items:
            item.update()

    def draw(self, visible: bool = False):
        if visible:  # Only draw if grid is visible
            pygame.draw.rect(
                self.display,
                color=(0, 0, 0),
                rect=self.rect,
                width=0  # Fill this one
            )
            pygame.draw.rect(
                self.display,
                color(255, 255, 255),
                rect=self.rect,
                width=2
            )
        for item in self.items:
            item.draw()


class Row:
    def __init__(self, grid: Grid, data: List = None):
        self.grid = grid

        if data:
            self._list = list(data)
        else:
            self._list = list()

    def __len__(self):
        """ List length """
        return len(self._list)

    def __getitem__(self, i):
        """ Get a list item """
        return self._list[i]

    def __delitem__(self, i):
        """ Delete an item """
        del self._list[i]

    def __setitem__(self, i, val):
        """ Set item """
        # optional: self._acl_check(val)
        self._list[i] = val

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __str__(self):
        return str(self._list)

    def insert(self, i, val):
        """ Insert value at index """
        # optional: self._acl_check(val)
        self._list.insert(i, val)

    def append(self, val):
        """ Append value at end of list """
        self.insert(len(self._list), val)


class Grid(StaticItem):
    def __init__(
        self,
        position: List[int] = [0, 0],
        rows: int = 1,
        columns: int = 1,
        row_sizes: Union[List[int], List[float]] = None,
        column_sizes: Union[List[int], List[float]] = None,
        size: Tuple[int, int] = None,
        visible: bool = False,
        selected: bool = False
    ):
        """
        Args:
            position (List[int] = [0, 0]): Position to place item on screen (or on page).
            rows (int): An integer representing number of rows.
            columns (int): An integer representing number of columns.
            row_sizes (Union[List[int], List[float]]): List of heights for each row, heights can either (all together)
                be integer values (representing height of each row in px) or float numbers (representing height of each
                row by percentage relative to grid size)
            column_sizes (Union[List[int], List[float]]): List of widths for each column, widths can either
                (all together) be integer values (representing width of each row in px) or float numbers
                (representing width of each row by percentage relative to grid size)
            size (Tuple[int, int] = (1, 1)): Size of item.
            visible (bool): If item is currently visible.
            selected (bool): If item is currently selected.
        """
        if not size:  # Fetch whole screen size if not passed
            size = pygame.display.get_surface().get_size()
        super().__init__(posiiton=position, size=size, visible=visible, selected=selected)

        self._list: List[Row] = []
        self._normalize = lambda vec, vec_sum: [val / vec_sum for val in vec]  # Normalize vector:
        self.row_sizes = row_sizes[:rows]
        self.column_sizes = column_sizes[:columns]
        self.__make(rows, columns)

    def __make(self, number_of_rows: int, number_of_columns: int) -> None:
        """
        Method creates grids list which contains rows of cells.

        Args:
            number_of_rows (int): Number of rows.
            number_of_columns (int): Number of columns.
        """
        # TODO: Set and normalize row and column sizes, incorporate in bottom functionality
        row_height = int(self.height // number_of_rows)
        column_width = int(self.width // number_of_columns)
        curr_x, curr_y = 0, 0
        for i in range(number_of_rows):
            row = Row(self)
            for j in range(number_of_columns):
                row.append(
                    Cell(
                        grid=self,
                        position_in_grid=(i, j),
                        position=[curr_x, curr_y],
                        size=(column_width, row_height)
                    )
                )
                curr_x += column_width
            self._list.append(row)
            curr_x = 0
            curr_y += row_height

    @property
    def rows(self):
        return len(self._list)

    @property
    def columns(self):
        return len(self._list[0])

    def normalize(self) -> None:
        pass

    def add_item(self,
                 item: any,
                 row: int = None,
                 column: int = None,
                 alignment: str = None,
                 padding: str = None
                 ) -> None:
        """
        Method adds item to the grid in the specified cell at position row, column. Optional alignments, and paddings
        can be defined relative to the cell where the item is being added.

        Args:
            item (any): Item to add.
            row (int): Row in grid to add the item in. Starting at 0.
            column (int): Column in grid to add the item in. Starting at 0.
            alignment (str): Representing one or more alignment types. These include: centre, top, bottom, left, right.
                Centre should be defined first. Separate alignments using a space " ".
            padding (str): Representing one or more paddings of each side of the cell. Multiple can be passed by
                separating them with commas ",", each padding should be passed as "side px". Where sides include: top,
                bottom, left, right. Px represents an integer number of pixels to pad.
                Ex.: padding = "top 5, left 10"
        """
        self._list[row][column].add_item(item=item, alignment=alignment, padding=padding)

    def update(self):
        for row in self._list:
            for cell in row:
                cell.update()

    def draw(self):
        for row in self._list:
            for cell in row:
                cell.draw(visible=self.visible)  # Pass if self visible

    def __iter__(self):
        for row in self._list:
            yield row

    def __len__(self):
        """ List length """
        return len(self._list)

    def __getitem__(self, i):
        """ Get a list item """
        return self._list[i]

    def __delitem__(self, i):
        """ Delete an item """
        del self._list[i]

    def __setitem__(self, i, val):
        """ Set item """
        self._list[i] = val

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __str__(self):
        return str(self._list)
