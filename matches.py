"""Match multiple patterns."""

from dataclasses import dataclass
import re
from typing import Any, Iterator, Optional


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


def multiple_finditer(
    patterns: list[re.Pattern[Any]], string: str
) -> Iterator[re.Match[Any]]:
    """
    Yield all matches from multiple regular expression patterns applied to a
    string.

    Args:
        patterns (List[re.Pattern[Any]]): A list of compiled regular expression
            patterns.
        string (str): The string to search for matches.

    Yields:
        re.Match[Any]: Match objects from the `finditer` function of each
            pattern.
    """
    for pattern in patterns:
        for match_ in pattern.finditer(string):
            yield match_


def multiple_match(
    patterns: list[re.Pattern[Any]], string: str
) -> Optional[re.Match[Any]]:
    """Tries to match the given string against a list of regex patterns.

    Args:
        patterns (list[re.Pattern[Any]]): A list of compiled regex patterns.
        string (str): The string to be matched.

    Returns:
        Optional[re.Match[Any]]: The first match object if a match is found,
            otherwise None.
    """
    for pattern in patterns:
        if match := pattern.match(string):
            return match
    return None


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
