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
