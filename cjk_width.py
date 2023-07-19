"""
String Width but Contain CJK Full-Width Chars.
Reference: https://stackoverflow.com/a/16118005
"""

import unicodedata


def char_width(char):
    """Returns the east asian width assigned to the character chr as string."""
    return 2 if unicodedata.east_asian_width(char) in ('F', 'W') else 1


def string_width(string):
    """Return String Width but Contain CJK Full-Width Chars."""
    return sum([char_width(char) for char in string])


def center(string, width: int = 80, fill_char=' '):
    """Return centered in a string of length width."""
    fill_char_width = string_width(fill_char)
    if fill_char_width == 0:
        return string
    fill_length = ((width - string_width(string)) // 2) // fill_char_width
    return fill_char * fill_length + string + fill_char * fill_length


def ljust(string, width: int = 80, fill_char=' '):
    """Return the string left justified in a string of length width."""
    fill_char_width = string_width(fill_char)
    if fill_char_width == 0:
        return string
    fill_length = (width - string_width(string)) // fill_char_width
    return string + fill_char * fill_length


def rjust(string, _width: int = 80, fill_char=' '):
    """Return the string right justified in a string of length width."""
    fill_char_width = string_width(fill_char)
    if fill_char_width == 0:
        return string
    fill_length = (_width - string_width(string)) // fill_char_width
    return fill_char * fill_length + string


def cut(string, width, keep=False):
    inv = False
    str_a: str = ''
    str_b: str = ''
    str_w: int = 0

    if width < 0:
        inv = True
        string = string[::-1]
        width = 0 - width

    for char in string:
        char_w = char_width(char)
        if str_w >= width:
            str_b += char
        elif str_w < width < str_w + char_w:
            if keep:
                str_a += char
            else:
                str_b += char
        else:
            str_a += char
        str_w += char_w

    if inv:
        str_a = str_a[::-1]
        str_b = str_b[::-1]
        return str_b, str_a
    else:
        return str_a, str_b


def overflow(string: str, width: int, ellipsis: str = '...', fill_char: str = '') -> str:
    """Like CSS styled text-overflow."""
    ellipsis_w = string_width(ellipsis)
    assert width >= ellipsis_w, 'Output width should >= ellipsis width.'
    if string_width(string) <= width:
        return string
    str_a, _ = cut(string, width-ellipsis_w)
    str_a = str_a + ellipsis
    str_a = ljust(str_a, width, fill_char)
    return str_a


if __name__ == '__main__':
    pass
    # test_str = "asd謝謝茄子asd"
    # print(f'"{test_str}", len = {len(test_str)}, width = {string_width(test_str)}')
    # # print(ljust("こんにちは", 80, "は"))
    # # print(rjust("こんにちは", 80, "こ"))
    # test_str = "asd茄子asd"
    # test_str = "asd茄子"
    # for w in range(-9, 10):
    #     print(f'cut({test_str}, {w:3}) =', cut(test_str, w))
    # for w in range(-9, 12):
    #     print(f'cut({test_str}, {w:3}, k) =', cut(test_str, w, True))
    # test_str = 'asd私はガラスasd'
    # for w in range(3, 18):
    #     print(f'overflow({test_str}, {w:3}) = "{overflow(test_str, w, "...", "_")}"')
    # try:
    #     overflow(test_str, 1)
    # except Exception as e:
    #     print('ERROR:', e)
