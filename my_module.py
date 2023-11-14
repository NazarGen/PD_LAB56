# my_module.py

def sum2numbers(num1,num2):
    """Summ of 2 numbers

    Args:
        num1 (float) or (int): first number.
        num2 (float) or (int): second number.

    Returns:
        float or int: Summ.
    """
    summ = num1 + num2
    return summ


def split_string_by_comma(input_string):
    """Split a string into a list using commas as separators.

    Args:
        input_string (str): The input string to be split.

    Returns:
        list: A list of substrings separated by commas.
    """
    result = input_string.split(',')
    return result
