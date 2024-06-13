"""XOR Opreation"""

from typing import Any


def xor(a: Any, b: Any) -> bool:  # pylint: disable=C0103
    """The logical operation of Exclusive or / exclusive disjunction.

    Args:
        a,b (boolean): Boolean-able variables.

    Returns:
        Boolean: a xor b.
    """
    return bool((a and not b) or (not a and b))
