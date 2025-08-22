"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module provides helpers to compute preparation, baking,
and total elapsed times for a lasagna recipe.
"""

from typing import Final

# Constants
EXPECTED_BAKE_TIME: Final[int] = 40  # minutes the lasagna should bake in total
PREPARATION_TIME_PER_LAYER: Final[int] = 2  # minutes of prep per layer


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Return remaining bake time in minutes.

    Args:
        elapsed_bake_time: Minutes the lasagna has already baked.

    Returns:
        Remaining minutes to bake, based on EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """Return total preparation time for the given number of layers.

    Args:
        layers: Number of layers in the lasagna.

    Returns:
        Total preparation time in minutes.
    """
    return layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """Return total time spent so far (prep + baking elapsed).

    Args:
        layers: Number of layers in the lasagna.
        elapsed_bake_time: Minutes the lasagna has already baked.

    Returns:
        Total elapsed time in minutes (preparation plus elapsed baking).
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time