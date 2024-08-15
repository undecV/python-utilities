class Flags:
    """
    A class to manage a set of boolean flags.

    Attributes:
        flags (dict): A dictionary holding the state of each flag.

    Methods:
        set(label: str): Sets the specified flag to True.
        clear(): Clears all flags (sets them to False).
        toggle(label: str): Toggles the state of the specified flag.
        is_set(label: str) -> bool: Checks if the specified flag is set.
        any_set() -> bool: Returns True if any flag is set.
        all_set() -> bool: Returns True if all flags are set.
        unset(label: str): Unsets the specified flag (sets it to False).
        __str__() -> str: Returns a string representation of the flags.
        __repr__() -> str: Returns a detailed string representation of the Flags object.
    """

    def __init__(self, *flag_labels: str):
        """
        Initializes the Flags object with the given flag labels, all set to False initially.

        Args:
            *flag_labels (str): The labels for the flags to be managed.
        """
        self.flags = {label: False for label in flag_labels}

    def set(self, label: str):
        """
        Sets the specified flag to True.

        Args:
            label (str): The label of the flag to set.
        """
        if label in self.flags:
            self.flags[label] = True

    def clear(self):
        """
        Clears all flags, setting them to False.
        """
        for label in self.flags:
            self.flags[label] = False

    def toggle(self, label: str):
        """
        Toggles the state of the specified flag.

        Args:
            label (str): The label of the flag to toggle.
        """
        if label in self.flags:
            self.flags[label] = not self.flags[label]

    def is_set(self, label: str) -> bool:
        """
        Checks if the specified flag is set (True).

        Args:
            label (str): The label of the flag to check.

        Returns:
            bool: True if the flag is set, False otherwise.
        """
        return self.flags.get(label, False)

    def any_set(self) -> bool:
        """
        Checks if any flag is set (True).

        Returns:
            bool: True if any flag is set, False otherwise.
        """
        return any(self.flags.values())

    def all_set(self) -> bool:
        """
        Checks if all flags are set (True).

        Returns:
            bool: True if all flags are set, False otherwise.
        """
        return all(self.flags.values())

    def unset(self, label: str):
        """
        Unsets the specified flag, setting it to False.

        Args:
            label (str): The label of the flag to unset.
        """
        if label in self.flags:
            self.flags[label] = False

    def __str__(self) -> str:
        """
        Returns a string representation of the flags, with set flags showing their label and unset flags as spaces.

        Returns:
            str: A string showing the state of each flag.
        """
        return ''.join(label if self.flags[label] else ' ' for label in self.flags)

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the Flags object.

        Returns:
            str: A string representation of the Flags object.
        """
        return f"<Flags {self.flags}>"
