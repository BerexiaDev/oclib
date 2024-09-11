class NotFoundError(Exception):
    """Exception raised when required data is not available."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DataUnavailableError(Exception):
    """Exception raised when required data is not available."""


class AlreadyExists(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Unmodifiable(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
class DateValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)