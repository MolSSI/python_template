"""
Contains several numerical related functions.
"""


def add(x, y):
    """The sum of two numbers.

    Parameters
    ----------

    x : (int, float)
        The first number to be added.
    y : (int, float)
        The second number to be added.

    Returns
    -------
    ret : (int, float)
        The sum of the inputs a and b

    Notes
    -----
    Python will often convert the types of the input values. For example if the
    input of x and y are integers the result will be in an integer.  However if
    the input is a integer and a float a float will be returned.

    Examples
    --------

    Adding two integers together:

    >>> add(5, 3)
    8

    An example of mixed input type:

    >>> add(5.0, 3)
    8.0
    """

    return x + y
