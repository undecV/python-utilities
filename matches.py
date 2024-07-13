"""Match multiple patterns."""

from dataclasses import dataclass
import re


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
