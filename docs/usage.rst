=====
Usage
=====

Setup
-----
Install the library from PyPI, prefferably into a virtual environment. Creating a virtual environment (venv) helps if your project will later be packaged with a tool like Pyinstaller.

Create your project directory::

    > mkdir MyNewProject
    
Create virtual environment inside the directory::

    > cd MyNewProject  # Move into directory
    > python -m venv venv  # Create venv (Path to venv will look like this: /path/to/MyNewProject/venv)
    
Activate virtual environment and install the library using Pip::

    > venv/scripts/activate  # Activate, a (venv) will appear at the beggining of the command line
    (venv)> pip install pyggui
    
To use pyggui in a project::

	import pyggui
    
As the project consists of multiple packages and modules it is recomended that each item, class or function is imported separatley. 

Project structure
-----------------

Recomended project structure is as follows::
    
    MyNewProject/
        venv/
        assets/  # All assets (images, sounds, etc.)
        pages/  # Page python files 
        logic/  # Custom logic such as a Player module, Entity, Map, etc.
        main.py
        __init__.py

Ofcourse you can personalize you structure as you want, but having a main file is recomended (again because of packaging).
Optionally the library has a client included for command line tools where the above described directory structure can be generated automatically, see paragraph below. 

Generate project structure
==========================
Generate you projects structure using one command. This will copy all needed directories and files into your project so you can get straight into coding!

Activate virtual environment and call Pythons make command passing it pyggui::
    
    (venv)> python -m pyggui
    
This will then create the above structure in the directory where the virtual environment is contained.
Optionally you can pass the -p parameter specifying where the structure should be created, in case you're not running from inside your virtual environment::

    > python -m pyggui -p=C:\absolute\path\to\project\directory\MyNewProject
    
Getting started
---------------
The library is oriented around pages, where pages are custom classes you create and add items to (such as buttons, images, ...). Pages are stored, and handled inside the controller object. Everything along with the main loop, controller, input and window is defined inside the Game object. 

Main file and Game object
=========================
Creating our main loop is done by initializing the Game object to which we can set some global properties and settings::

    from pyggui import Game
    
    game = Game(
        display_size = (720, 360),  # Define display size 
        page_directory = "pages"  # Optionally pas the directory where pages are defined, this helps internally as pages are automatically found and imported
        entry_page = "WelcomePage",  # Optionally set the entry page to your game, this will be more clear as we create some pages 
        fps = 60,  # Optionally set an FPS cap
        display = my_custom_surface  # Optionally pass your own custom pygame.surface.Surface object with your own settings
    )
    
    if __name__ == '__main__':
        game.run()  # Run the main loop

There are more parameters you can set but above ones are the basics, none of them are needed for a basic loop. 
Try running below code, this will open a default page::

    from pyggui import Game
    
    game = Game()
    
    if __name__ == '__main__':
        game.run()

Pages and Controller
====================
Whole project is based around pages and the controller object. Pages are custom classes that inherit from the pyggui.gui.Page class. Once you create a custom page, it gets automatically detected and imported by the controller, it is also added to the controllers pages dictionary attribute. This simplifies importing and redirecting between pages.
Each page recieves the controller object so you should always include it in the __init__'s arguments.

Lets define a simple page, first create the pages py file inside pages (MyNewProject/pages/welcome_page.py)::

    from pyggui.gui import Page
    
    class WelcomePage(Page):
        def __init__(self, controller):  # Always have a parameter for controller
            super().__init__(controller)  # Initialize parent class and pass it the controller object
            
This is all that is needed for creating a simple page. 
If we want this to be our landing page in the game, we pass the classes name as a string in the Games class parameter entry_page::

    game = Game(
        page_directory="pages",  # Set directory where pages are defined
        entry_page="WelcomePage"
    )

Controller stores every defined page in our project in the pages attribute, where the key is the class name of page as a string.
More about this in the controllers documentation TODO add link to docs.

Redirecting between pages can be done using controllers redirect_to_page method, where you pass it the pages name as a parameter.
Lets define a send page and redirect to it as we land on the WelcomePage::


    from pyggui.gui import Page
    
    class SecondPage(Page):
        def __init__(self, controller):
            super().__init__(controller)
            
            print("We are on the SecondPage")
    
    
    class WelcomePage(Page):
        def __init__(self, controller):
            super().__init__(controller)
            
            print("We are on the WelcomePage")
            
            # Instantly redirect
            print("Redirecting...")
            self.controller.redirect_to_page("SecondPage")  # Notice the controller is an attribute, this gets set when we call supers __init__ method above,
                                                            # Controller can also be accesed without self (i.e. controller.redirect_to_page("SomePage")) inside the innit method.
            
Above defined will, once the game.run() method is ran, output::

    >>> We are on the WelcomePage
    >>> Redirecting...
    >>> We are on the SecondPage
    
Redirecting can ofcourse be used as an "on click" method with different items, more on that in the below paragraph once we learn to add different items. 
Pages can also have different parameters you can pass, but must always have the controller as the first parameter.

See the Page documentation TODO Add link
          
Adding and controlling Gui elements
===================================

The library consists of many gui elements (called items) you can use. Items can be personalized by passing custom images, sprites or folders containing images used for animations. However if you initially wish to only experiment (and later create your custom images), you can use default items. Default items are defined inside the library and behave exactly like your custom items but have some basic pre-defined animations and looks.

We add each item to a page, we do that inside the init method using the add_item method.

Lets add a simple text item to our WelcomePage::

    from pyggui.gui import Page, Text  # Text class for displaying text on screen

    class WelcomePage(Page):
        def __init__(self, controller):
            super().__init__(controller)
            
            self.add_item(
                item=Text(
                    position=[100, 100],  # Position on screen (and page) to add the item at (upper left corner of item)
                    value="Welcome!",  # Text value to display
                    font_size=40,  # Define the size of the font, 40 in this case as we want it to be big
                )
            )
            
You can store the item in a pages attribute so you can access it from different method, or other items::

    class WelcomePage(Page):
        def __init__(self, controller):
            super().__init__(controller)
            
            self.text = Text(  # Define the item, store in attribute
                position=[100, 100],  # Position on screen (and page) to add the item at (upper left corner of item)
                value="Welcome!",  # Text value to display
                font_size=40,  # Define the size of the font, 40 in this case as we want it to be big
            )
            # Add it later, do not forget this
            self.add_item(self.text)

Above will now have a bigger text (Welcome!) on screen with the libraries default font. Ofcourse we can also add our custom font to the text, more on that here: Text documentation. TODO add link.

Some items have to have the controller passed to them. Controller can view mouse position, clicks, etc. so it is used for detecting hovering above item or clicking on said item.

Lets add a simple buutton that redirects to our other SecondPage::

    from pyggui.gui import Button
    from pyggui.helpers import create_callable

    class WelcomePage(Page):
        def __init__(self, controller):
            super().__init__(controller)
            
            # Above defined text should be here
            
            self.redirect_to_second_page_button = Button(
                controller=self.controller,  # Pass it the controller object
                position=[100, 300],  # Set some position
                size=[120, 40],   # Set some size
                text="Go to second page",  # Give the button text as a string or pass your own Text item.
                on_click=create_callable(self.controller.redirect_to_page, "SecondPage")  # Add on click function
            )
            self.add_item(self.redirect_to_second_page_button)  # Do not forget to add it to page
            
We've now added a button to our page.
Notice the create_callable function used in the on_click parameter. 
This is a very usefull function which is used alot internally. 
What it does is it creates a callable function for the button to use once it's clicked. On click accepts a function name (without brackets) that is executed once the item is clicked. 
So if we wanted to do some custom action when the button is clicked, we can define our own function::

    def make_some_action():
        # Do stuff
        pass
        
and pass it to the on_click parameter::

    self.some_button = Button(
        # parameters
        on_click=make_some_action
    )
    
But what if our function accepts parameters? Thats where the create_callable function comes in handy. It is defined as follows::
    
    def create_callable(func, *args, **kwargs) -> Callable:
    
create_callable accepts some function func, arguments and key word arguments. It then returns a callable function wich, when called, executes our passed func with *args and **kwargs passed to it.

In above example, where we redirect, the controller.redirect_to_page expects a single argument to_page (the page we want to redirect to). As we can not pass controller.redirect_to_page("SecondPage") as an on_click (it executes as we pass it), we use the create_callable to pass arguments. 

On another note, if our page accepts parameters in the init method, we can pass those to the redirect_to_page method as follows::
    
    create_callable(self.controller.redirect_to_page, "SecondPage", first_argument, second_argument, keyword=argument)
    
Our second page, defined as follows::

    class SecondPage(Page):
        def __init__(self, controller, first_argument, second_argument, keyword=None):
            super().__init__(controller)
            
            # Do something

Will recive those arguments passed with the redirect_to_page method.


Event handlers
==============
Todo

Handling files and other helpers
================================
Todo

Custom game loops
=================
Todo
