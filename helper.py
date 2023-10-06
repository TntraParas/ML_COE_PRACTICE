from typing import Callable


def print_stars(func: Callable[[], None]) -> Callable[[], None]:
    """
    It is function wrapper which will pretty print the function execution
    Input:
        func: a void function
    Returns:
        () -> None
    """

    def pretty_function_printer():
        print("\n*******************\n")
        func()
        print("\n*******************\n")

    return pretty_function_printer
