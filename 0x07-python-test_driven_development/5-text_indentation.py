#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """  A function that prints a text with 2 new lines after
         each of these characters: ., ? and :
    Args:
        text (string): The text to print.
    Raises:
        text must be a string, otherwise raise
        a TypeError exception with the message
        text must be a string
    """
    l_t = len(text)
    if type(text) is not str:
        raise TypeError("text must be a string")
    ch = 1
    while ((ch >= l_t) is False) and text[ch] == ' ':
        ch = ch + 1
    l_t = len(text)
    while ((ch >= l_t) is False):
        print(text[ch], end="")
        if text[ch] == "\n" or text[ch] in ".?:":
            if text[ch] in ".?:":
                print("\n")
            ch = ch + 1
            while(((ch >= l_t) is False) and (text[ch] == ' ')):
                ch = ch + 1
            continue
        ch = ch + 1
