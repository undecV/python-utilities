import difflib


def color_diff(old, new):
    """Show diff of two string sequences in colors.

    Reference:
      - https://stackoverflow.com/a/64404008 (CC BY-SA 4.0)

    Args:
        old, new (string): strings to be diff.

    Returns:
        string: A color formatted string.
    """
    red = lambda text: f"\033[38;2;255;0;0m{text}\033[38;2;255;255;255m"
    green = lambda text: f"\033[38;2;0;255;0m{text}\033[38;2;255;255;255m"
    blue = lambda text: f"\033[38;2;0;0;255m{text}\033[38;2;255;255;255m"
    white = lambda text: f"\033[38;2;255;255;255m{text}\033[38;2;255;255;255m"

    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    for code in codes:
        if code[0] == "equal":
            result += white(old[code[1]:code[2]])
        elif code[0] == "delete":
            result += red(old[code[1]:code[2]])
        elif code[0] == "insert":
            result += green(new[code[3]:code[4]])
        elif code[0] == "replace":
            result += (red(old[code[1]:code[2]]) + green(new[code[3]:code[4]]))
    return result
