#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines after chars
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The text to print.

    Raises:
    TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace each of the specified characters with the same character
    for char in ".:?":
        text = text.replace(char, char + "\n\n")

    # Print the resulting text, removing leading or trailing whitespaces
    print("\n".join(line.strip() for line in text.split("\n")), end="")
