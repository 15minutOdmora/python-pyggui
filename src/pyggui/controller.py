"""
Module containing the controller class.

Controller class object acts as an intermediate between game wide objects, used for page redirection, game pausing, ...
"""

from typing import Dict, Callable

from pyggui.helpers.stack import Stack
from pyggui.defaults.__welcome_page import _WelcomePage
from pyggui.configure.pages import get_all_page_classes


class Controller:
    """
    Main object throughout the game. Mediator between game object and everything else.
    Contains page_stack attribute which is a Stack, containing visited pages.
    """
    def __init__(self, game: 'Game'):
        """
        Args:
            game (Game): Main game object.
        """
        self.game = game
        self._input = self.game.input  # Set input attr. Accessible through properties

        # Pages setup
        self.pages: Dict = get_all_page_classes()
        self.page_stack: Stack = Stack()
        # Landing page setup
        # If no page was found or the default entry was left as is -> add the welcome_page from defaults
        if not bool(self.pages) or self.game.entry_page == "_WelcomePage":
            self.pages["_WelcomePage"] = _WelcomePage
            self.current_page = _WelcomePage
        else:
            self.current_page = self.pages[self.game.entry_page]

    @property
    def input(self):
        return self._input

    @property
    def dt(self) -> float:
        """
        Difference in time (milliseconds) between current frame and previous frame.

        Returns:
            float: Milliseconds
        """
        return self.game.dt

    @property
    def dt_s(self) -> float:
        """
        Difference in time (seconds) between current frame and previous frame.

        Returns:
            float: Seconds
        """
        return self.game.dt_s

    @property
    def paused(self) -> bool:
        """
        If game is currently paused.

        Returns:
            bool: If paused
        """
        return self.game.paused

    @property
    def current_page(self) -> any:
        """
        Current page on top of the page stack.

        Returns:
            any: Page
        """
        return self.page_stack.peak()

    @current_page.setter
    def current_page(self, page: any) -> None:
        """
        Set current page to be on top of stack.

        Args:
            page (any): Page to push on top of stack.
        """
        self.page_stack.push(page(self))  # Initialize page

    def add_event_handler(self, event_handler: 'EventHandler') -> None:
        """
        Method adds a game-wide EventHandler object.

        Args:
            event_handler (EventHandler): EventHandler object to add.
        """
        self.input.add_event_type_handler(event_handler)

    def add_event_type_handler(self, event_type: int, handler: Callable):
        """
        Method adds a single game-wide event type handler. The handler callable function gets triggered once the
        event_type appears in the main input loop.

        Args:
            event_type (int): Pygame event type.
            handler (Callable): Callable function to get called once the event type appears in the main input loop.
        """
        # This method adds an event type handler game wide, if you want the event to be deleted after page is not used
        # i.e. after redirection, use the pages custom event handler.
        self.input.add_event_type_handler(event_type=event_type, handler=handler)

    def redirect_to_page(self, to_page: str, *args, **kwargs) -> None:
        """
        Method redirects to page defined as a string. Args and Kwargs are passed to page class initialization.
        Error gets displayed if page does not exist. TODO: Make custom error

        Args:
            to_page (str): Page to redirect to, has to be defined in the pages dictionary.
            *args (any): Get passed to pages class initialization.
            **kwargs (any): Get passed to pages class initialization.
        """
        if to_page in self.pages.keys():
            self.current_page.on_exit()  # Call on-exit function
            self.page_stack.push(self.pages[to_page](self, *args, **kwargs))  # Initialize page and push on stack
        else:
            print(f"Controller: Redirection error to page {to_page}. Page does not exist.")

    def go_back(self) -> None:
        """
        Method goes back one page in the page stack.
        """
        if not self.page_stack.empty():
            self.current_page.on_exit()  # Call on-exit function
            self.page_stack.pop()  # Remove current page
            self.current_page.on_appearance()  # Call on appearance on new page
        else:
            print(f"Controller: Redirection error calling go_back.\n   Page stack is empty.")

    def pause_game(self) -> None:
        """
        Method pauses and un-pauses game.
        """
        self.game.paused = not self.game.paused
