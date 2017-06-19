"""
This is a short file containing a levenshtein implementation.
"""


def levenshtein(seq1, seq2):
    """Function to compute the Levenshtein distance between two strings.
    Reference: https://en.wikipedia.org/wiki/Levenshtein_distance

    Parameters
    ----------

    seq1 : str
        The first string to compare
    seq2 : str
        The second string to compare

    Returns
    -------
    distance : int
        The Levenshtein distance between two strings

    Notes
    -----
    The Levenshtein distance between two words is the minimum number of
    single-character edits required to change one word into the other.  This is
    often very useful for finding approximate string matches. For example
    throwing an error with suggestions due to a keyword mismatch.

    Examples
    --------

    Find the distance between kitten and sitting:

    >>> levenshtein("kitten", "sitting")
    3
    """

    # Do some type checking if desired
    if not isinstance(seq1, str):
        raise TypeError("levenshtein: first arguement must be a string, input type %s" % type(seq1))

    if not isinstance(seq2, str):
        raise TypeError("levenshtein: second arguement must be a string, input type %s" % type(seq2))

    # Iterative "two row" levenshtein implementation
    oneago = None
    thisrow = list(range(1, len(seq2) + 1)) + [0]
    for x in range(len(seq1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in range(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)

    # Return
    return thisrow[len(seq2) - 1]
