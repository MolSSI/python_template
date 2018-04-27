"""
Unit and regression test for the numeric file.
"""

# Import our module and shorten the name
import python_template as pt
import pytest


# Test python_template/text/levenstein


def test_add_simple():
    """
    This is a simple test that checks the return value
    """

    assert 10 == pt.add(5, 5)
    assert 3 == pt.add(5, -2)
    assert 3 == pt.add(-2, 5)


def test_add_return_type():
    """
    Check the return value of the duck-typed function
    """

    assert isinstance(pt.add(5, 5), int)
    assert isinstance(pt.add(5, 5.0), float)
    assert isinstance(pt.add(5.0, 5.0), float)
