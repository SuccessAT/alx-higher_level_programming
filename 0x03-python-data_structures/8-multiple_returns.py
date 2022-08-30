#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if (length == 0):
        newer_tuple = (length, None)
    else:
        newer_tuple = (length, sentence[0])

    return (newer_tuple)
