#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return None
    else:
        words = sentence.split()
        words_tuple = tuple(words)
        length = len(words_tuple)
        first = words_tuple[0]
