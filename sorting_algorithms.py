"""Sorting algorithms for Player objects using various methods."""

import numpy as np
from typing import List
from .player import Player


STAT_MAPPING = {
    "ppg": "points_per_game",
    "apg": "assists_per_game",
    "bpg": "blocks_per_game",
    "spg": "steals_per_game",
}


def numpy_sort(players: List[Player], stat: str = "ppg", descending: bool = True) -> List[Player]:
    """
    Sort a list of Player objects by a specified statistic using NumPy's sorting algorithm.
    
    Args:
        players: List of Player objects to sort.
        stat: Statistic to sort by. Options: 'ppg' (points per game), 'apg' (assists per game),
              'bpg' (blocks per game), 'spg' (steals per game), 'championships'.
        descending: If True (default), sort in descending order. If False, sort ascending.
    
    Returns:
        A new sorted list of Player objects.
    
    Raises:
        ValueError: If an invalid stat is provided.
    """
    if stat not in STAT_MAPPING:
        raise ValueError(
            f"Invalid stat '{stat}'. Choose from: {', '.join(STAT_MAPPING.keys())}"
        )
    
    attr_name = STAT_MAPPING[stat]
    
    # Create array of stat values
    stat_values = np.array([getattr(player, attr_name) for player in players])
    
    # Get sorted indices using NumPy
    if descending:
        sorted_indices = np.argsort(-stat_values)  # Negative for descending
    else:
        sorted_indices = np.argsort(stat_values)
    
    # Return players sorted by indices
    return [players[i] for i in sorted_indices]


def insertion_sort(players: List[Player], stat: str = "ppg", descending: bool = True) -> List[Player]:
    """
    Sort a list of Player objects by a specified statistic using insertion sort.

    Args:
        players: List of Player objects to sort.
        stat: Statistic to sort by.
        descending: If True, sort in descending order; otherwise ascending.

    Returns:
        A new sorted list of Player objects.

    Raises:
        ValueError: If an invalid stat is provided.
    """
    if stat not in STAT_MAPPING:
        raise ValueError(
            f"Invalid stat '{stat}'. Choose from: {', '.join(STAT_MAPPING.keys())}"
        )

    attr_name = STAT_MAPPING[stat]
    sorted_players = players.copy()

    for i in range(1, len(sorted_players)):
        j = i
        while j > 0:
            current_value = getattr(sorted_players[j], attr_name)
            prev_value = getattr(sorted_players[j - 1], attr_name)

            in_order = current_value <= prev_value if descending else current_value >= prev_value
            if in_order:
                break

            sorted_players[j], sorted_players[j - 1] = sorted_players[j - 1], sorted_players[j]
            j -= 1

    return sorted_players


def percolate_up(heap: list, idx: int, compare) -> None:
    """Move element at idx up until heap order is restored.

    `heap` is a list of (key, Player) tuples. `compare(a, b)` should return
    True if `a` should be ordered above `b` in the heap (e.g. a > b for max-heap).
    """
    while idx > 0:
        parent = (idx - 1) // 2
        if compare(heap[idx][0], heap[parent][0]):
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break


def percolate_down(heap: list, idx: int, size: int, compare) -> None:
    """Move element at idx down until heap order is restored."""
    while True:
        left = 2 * idx + 1
        right = left + 1
        best = idx

        if left < size and compare(heap[left][0], heap[best][0]):
            best = left
        if right < size and compare(heap[right][0], heap[best][0]):
            best = right

        if best == idx:
            break
        heap[idx], heap[best] = heap[best], heap[idx]
        idx = best


def heapify(items: list, compare) -> list:
    """Build a heap from items using percolate_up (insertion style)."""
    heap: list = []
    for item in items:
        heap.append(item)
        percolate_up(heap, len(heap) - 1, compare)
    return heap


def heapsort(players: List[Player], stat: str = "ppg", descending: bool = True) -> List[Player]:
    """
    Heapsort implementation that returns a new list of Player objects sorted by `stat`.
    Uses module-level `percolate_up`, `percolate_down`, and `heapify` helpers.
    """
    if stat not in STAT_MAPPING:
        raise ValueError(
            f"Invalid stat '{stat}'. Choose from: {', '.join(STAT_MAPPING.keys())}"
        )

    attr_name = STAT_MAPPING[stat]

    if descending:
        def compare(a, b):
            return a > b
    else:
        def compare(a, b):
            return a < b

    items = [(getattr(p, attr_name), p) for p in players]
    heap = heapify(items, compare)
    size = len(heap)
    sorted_players: List[Player] = []

    while size > 0:
        root_key, root_player = heap[0]
        # Move last to root and shrink
        heap[0] = heap[size - 1]
        heap.pop()
        size -= 1
        if size > 0:
            percolate_down(heap, 0, size, compare)
        sorted_players.append(root_player)

    return sorted_players
