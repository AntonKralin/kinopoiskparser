class ValueNoException(Exception):
    """exception class"""
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return f"ValueNoException: {self.message}"
        else:
            return "ValueNoException"