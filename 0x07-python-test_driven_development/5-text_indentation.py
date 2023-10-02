#!/usr/bin/python3
"""
    This module supplies the text_indentation function

    Usage:
    ------
        >>> text_indentation = __import__('5-text_indentation').
        text_indentation
        >>> text_indentation(text)
"""


def text_indentation(text):
    """
        This function adds newlines to characters such as '.', '?' and ':'

        Argument:
        ---------
            text (string)
        Return Value:
        -------------
            It returns no value
    """
    if text is None:
        raise TypeError
    elif not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        # Initialize an empty result string
        result = ""

        # Initialize a flag to track if we are at the beginning of a line
        beginning_of_line = True

        # Iterate through each character in the input text
        for char in text:
            # If the character is one of the specified characters,
            # add two new lines
            if char in ".?:":
                result += "\n\n"
                beginning_of_line = True
            # If the character is not a space, add it to the result
            elif char != " ":
                # If we are at the beginning of a line,
                # add the character without a space
                if beginning_of_line:
                    result += char
                    beginning_of_line = False
                # If we are not at the beginning of a line,
                # add the character with a space
                else:
                    result += char
            else:
            # If the character is a space and we are not at the beginning of a line,
            # add it to the result
                if not beginning_of_line:
                    result += char
        # Print the formatted result
        print(result)
