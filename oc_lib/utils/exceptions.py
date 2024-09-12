class NotFoundError(Exception):
    """Exception raised when required data is not available."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DataUnavailableError(Exception):
    """Exception raised when required data is not available."""


class AlreadyExistsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UnmodifiableError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

        
class DateValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidDataError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)