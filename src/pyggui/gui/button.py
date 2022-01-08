"""
Module containing different buttons.
"""

from typing import Callable, List, Tuple, Union

import pygame

from pyggui.gui.item import Item
from pyggui.gui.text import Text


class DefaultButton(Item):
    """
    Default button is used when the user hasn't specified an image for the button itself.
    """
    def __init__(
        self,
        controller: 'Controller',
        position: List[int] = [0, 0],
        size: Tuple[int, int] = (100, 40),
        on_click: Callable = lambda: None,
        text: Union[str, Text] = "Button",
        fill_color: Tuple[int, int, int] = (0, 0, 0),
        border_color: Tuple[int, int, int] = (255, 255, 255),
        movable: bool = False
    ):
        """
        Args:
            controller (Controller): Main controller object.
            position (List[int]): Position of item on screen (or page). Defaults to [0, 0]
            size (Tuple[int, int]): Size of item. Defaults to (100, 40).
            on_click (Callable): Callable function gets triggered once the button is clicked. Defaults to None.
            text (Union[str, Text]): String or Text object to add as text to button. Defaults to 'Button'.
            fill_color (Tuple[int, int, int]): Inside color of button. Defaults to white.
            border_color (Tuple[int, int, int]): Border color of button, also determines the color of text if text was
                passed as string. Defaults to black.
            movable (bool): If item will be moved by on_click action. Used for slider buttons. Defaults to false.
        """
        super().__init__(controller, position, size, on_click, movable)

        self.controller = controller

        # Check if passed argument is string => create Text object
        if type(text) is str:
            self.text = Text(
                value=text,
                font_size=16,
            )
        else:
            self.text = text

        # Set colors
        self._fill_color = fill_color  # These ones define the colors
        self._border_color = border_color
        self.fill_color = self._fill_color  # These ones get used
        self.border_color = self._border_color

        # Set position of text and add object to items
        self.text.position = self.get_text_position()
        self.items.append(
            self.text
        )

    def get_text_position(self) -> List[int]:
        """
        Method calculates the position of text inside button to that it is centered.

        Returns:
            list[int, int]: Position of centered text.
        """
        # Center text in button
        x_pos = int((self.x + (self.width * 0.5)) - (self.text.width * 0.5))
        y_pos = int((self.y + (self.height * 0.5)) - (self.text.height * 0.5))
        return [x_pos, y_pos]

    def update(self) -> None:
        """
        Method updates self and re-sets text position.
        """
        if self.visible:
            # Call parent method
            super(self.__class__, self).update()
            # And then re center text
            self.text.position = self.get_text_position()

    def draw(self) -> None:
        """
        Method draws button along with its text on screen.
        """
        if self.visible:
            # Switch colors if hovered
            if self.hovered:
                self.border_color = self._border_color
                self.fill_color = self._fill_color
            else:
                self.border_color = self._fill_color
                self.fill_color = self._border_color

            pygame.draw.rect(
                self.display,
                self.border_color,
                self.rect,
                width=0,
                border_radius=10
            )
            pygame.draw.rect(
                self.display,
                self.fill_color,
                self.rect,
                width=3,
                border_radius=10
            )
            self.text.color = self.fill_color
            self.text.render()
            self.text.update()

            for item in self.items:
                item.draw()


class Button(Item):
    """
    Class for creating a button. Button has on_click method which gets triggered once the item is clicked.
    A directory path parameter should be passed for creating button with images, otherwise a DefaultButton is
    created.
    Directory path for button images should be structured:
        /some/path/button/-
                        normal.png  # Or other format
                        on_click/
                        on_hover/
        The on_click and on_hover directories can also be just files. If directories the files inside will get displayed
        one by one.
    """
    def __new__(cls, *args, **kwargs):
        # Check if directory_path was passed
        kwargs_copy = kwargs.copy()  # Mutate copy so all kwargs still go through
        folder_path = kwargs_copy.pop("directory_path", False)
        if folder_path:
            # Create instance of self is passed
            return super(Button, cls).__new__(cls, *args, **kwargs)
        else:
            # Return default button otherwise
            return DefaultButton(*args, **kwargs)

    def __init__(
        self,
        controller: 'Controller',
        directory_path: str = None,
        position: List[int] = [0, 0],
        size: Tuple[int, int] = (150, 60),
        on_click: Callable = None,
        movable: bool = False,
        animation_speed: Union[float, int] = 1,
    ):
        """
        Args:
            controller (Controller): Main controller object.
            directory_path (str): Path to a structured directory holding button images.
            position (List[int]): Position of button on screen (or page).
            size (Tuple[int, int]): Size of item. Defaults to normal images size if not passed.
            on_click (Callable): Callable function gets triggered once the button is clicked. Defaults to None.
            movable (bool): If item will be moved by on_click action. Used for slider buttons. Defaults to false.
            animation_speed (Union[float, int]): TODO
        """
        super().__init__(controller, position, size, on_click, movable)
        # TODO : Implement
        self.directory_path = directory_path
        self.animation_speed = animation_speed
