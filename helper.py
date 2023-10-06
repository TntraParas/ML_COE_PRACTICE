from typing import Callable

def printStars(func: Callable[[],None]) -> Callable[[],None]:
    """
    It is function wrapper which will pritty print the function execution
    Input:
        func: a void function
    Returns:
        () -> None
    """
    def preety_function_printer():
        print("\n*******************\n")
        func()
        print("\n*******************\n")
    return preety_function_printer
