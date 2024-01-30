#!/usr/bin/python3
"""defines a function that text-endent"""


def text_indentation(text):
    """prints a text with 2 new lines after each of '.', '?' and ':'.

    Args:
        text (string): input text.
    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
        ch += 1

    while ch < len(text):
        print(text[ch], end="")
        if text[ch] in ".:?" or text[ch] == "\n":
            if text[ch] in ".:?":
                print("\n")
            ch += 1
            while ch < len(text) and text[ch] == ' ':
                ch += 1
            continue
        ch += 1
