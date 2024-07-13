"A class that acts like a dict."


from typing import Any


class DictLike():
    """A class that acts like a dict: `instance.key == instance["key"]`.
    Reference: https://stackoverflow.com/a/61202765
    """
    def __setitem__(self, key, value) -> None:
        setattr(self, key, value)

    def __getitem__(self, key) -> Any:
        return getattr(self, key)

    def __repr__(self) -> str:
        return str(vars(self))

    def __str__(self) -> str:
        return self.__repr__()
