"""
Unit and regression test for the python_template/text submodule.
"""

# Import our module and shorten the name
import python_template as pt
import pytest


# Test python_template/text/levenstein

def test_levenshtein_return_simple():
    """
    This is a simple test that checks the return value for a single call
    """

    ret = pt.text.levenshtein("dog", "dag")
    assert ret == 1


tests = [("", "", 0),                # Edge case!
         ("a", "ab", 1),
         ("cat", "cat", 0),          # Identity
         ("  ", "  a", 1),           # White space
         ("  ", "  a", 1),
         ("Saturday", "Sunday", 3),  # Case sensitivity
         ("Saturday", "sunday", 4),
         ("kitten", "sitting", 3),   # Random tests
         ("mnemonic", "memory", 4),
        ]


@pytest.mark.parametrize("args", tests)
def test_levenshtein_return(args):
    """
    We can write more complex tests that test many calls.
    """

    # Unpack testing data
    seq1, seq2, benchmark = args

    # Test the function
    ret = pt.text.levenshtein(seq1, seq2)
    assert ret == benchmark


def test_levenshtein_exception():
    """
    Test that exception are properly raised
    """

    with pytest.raises(TypeError):
        pt.text.levenshtein("cat", 1)

    with pytest.raises(TypeError):
        pt.text.levenshtein((5, 5), "cat")
