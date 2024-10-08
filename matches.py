"""Match multiple patterns."""

from dataclasses import dataclass
import re
from typing import Iterator


class BadFormatError(ValueError):
    """Inappropriate format of value that can not be parsed."""


def multiple_matches(text: str, patterns: list[re.Pattern]) -> re.Match:
    """Match multiple patterns."""
    match: re.Match | None = None
    for pattern in patterns:
        match = pattern.match(text)
    if not match:
        raise BadFormatError()
    return match


def multiple_match(patterns: list[re.Pattern], string: str, flags: int | re.RegexFlag = 0) -> re.Match | None:
    """
    Tries to match the given string against a list of regex patterns.

    Args:
        patterns (List[re.Pattern]): A list of compiled regex patterns.
        string (str): The string to be matched.
        flags (Union[int, re.RegexFlag], optional): Flags to be passed to the match function. Defaults to 0.

    Returns:
        Optional[re.Match]: The first match object if a match is found, otherwise None.
    """
    for pattern in patterns:
        match = re.match(pattern, string, flags)
        if match:
            return match
    return None


def multiple_finditer(patterns: list[re.Pattern], string: str) -> Iterator[re.Match[str]]:
    """Yield all matches from multiple regular expression patterns applied to a string.
    
    Args:
        patterns (List[re.Pattern]): A list of compiled regular expression patterns.
        string (str): The string to search for matches.
    
    Yields:
        re.Match[str]: Match objects from the `finditer` function of each pattern.
    """
    for pattern in patterns:
        for match_ in pattern.finditer(string):
            yield match_


@dataclass
class RegexEqual(str):
    """
    Regex - Match-Case Helper.
    Reference:
      Recipes and Tricks for Effective Structural Pattern Matching in Python:
      https://martinheinz.dev/blog/78
    """
    string: str
    match: re.Match = None  # type: ignore

    def __eq__(self, pattern):
        self.match = re.search(pattern, self.string)  # type: ignore
        return self.match is not None

    def __getitem__(self, group):
        return self.match[group]
