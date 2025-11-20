#!/usr/bin/python
def multiple_returns(sentence):
    if sentence == '':
        return None
    else:
        chars_tuple = tuple(sentence)
        length = len(chars_tuple)
        first = chars_tuple[0]
