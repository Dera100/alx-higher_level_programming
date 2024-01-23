#!/usr/bin/python3
def multiple_returns(sentence):
    """calculate length of stence and first character area

    Args:
        sentence: the sentence area

    Returns:
        return a (length, first-char)/0
    """
    if len(sentence) == 0:
        result = 0, None
    else:
        result = len(sentence), sentence[0]
    return (result)
