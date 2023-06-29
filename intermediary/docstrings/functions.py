"""This module is a exemple

This module has functions and its functions documentation
The sum function you really how to know.
"""
var_1 = 1


def sum_(x: int | float, y: int | float) -> int | float:
    """Sum x and y

    Args:
        x (int | float): Number 1
        y (int | float): Number 2

    Returns:
        int | float: The sum between x and y
    """
    return x + y


def multiply(
    x: int | float,
    y: int | float,
    z: int | float | None
) -> int | float:
    """Multiply x, y and/or z

    Args:
    x (int | float): Number 1
    y (int | float): Number 2
    z (int | float | None): Number 3

    Multiply x and y. If z was sent, multiply x, y, z

    """
    if z is None:
        return x * y
    return x * y * z


var_2 = 2
var_3 = 3
var_4 = 4
