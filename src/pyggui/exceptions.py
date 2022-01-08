"""
Module containing exceptions.
"""


# Controller errors
class ControllerError(Exception):
    """
    Base exception for controller related errors.
    """
    def __init__(self, message=None):
        if message is None:
            message = "Undefined error."
        super(ControllerError, self).__init__(str(message))


class RedirectionError(ControllerError):
    """
    Page redirection error.
    """
    def __init__(self, message=None):
        super(RedirectionError, self).__init__(message)


# GUI -> Item errors
class ItemError(Exception):
    """
    Base exception for item related errors.
    """
    def __init__(self, message=None):
        if message is None:
            message = "Undefined error."
        super(ItemError, self).__init__(str(message))


class NotResizableError(ItemError):
    """
    Item can not be resized error.
    """
    def __init__(self, message=None):
        super(NotResizableError, self).__init__(message)
