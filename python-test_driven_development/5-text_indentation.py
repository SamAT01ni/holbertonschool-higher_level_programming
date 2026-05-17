#!/usr/bin/python3
"""
"Text Indentation" module
Indent that shit bro
I will attack again
"""


def text_indentation(text):
    """Prints lines after certain syntax i guess
    Im so done with these tasks
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    while i < n:
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < n and text[i] == " ":
                i += 1
            continue
        i += 1
