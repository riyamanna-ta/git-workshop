# Custom python functions


def double_number(a):
    """
    Doubles a number

    Parameters
    ----------
    a : float

    Returns
    -------
    float
        The double of the number

    Example
    -------
    >> double_number(2)
        4
    """
    print(f"value before double_number(): {a}")
    result = a + a
    print(f"value after double_number(): {result}")


def square_number(a):
    """
    Squares a number

    Parameters
    ----------
    a : float

    Returns
    -------
    float
        The Square of the number
    Example
    -------
    >> square_number(3)
        9
    """
    print(f"value before square_number(): {a}")
    result = a * a
    print(f"value after square_number(): {result}")
    return a + a
