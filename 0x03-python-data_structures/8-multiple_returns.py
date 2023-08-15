#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    arg_1 = sentence[0]
    if sentence == "":
        return (0, None)
    return (str_len, arg_1)
