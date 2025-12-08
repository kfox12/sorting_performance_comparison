"""Unit tests for sorting algorithms."""

import unittest

from .player import Player
from .sorting_algorithms import numpy_sort, insertion_sort, heapsort


class TestNumpySort(unittest.TestCase):
    """Tests for numpy_sort algorithm."""

    def setUp(self):
        """Create small test player lists."""
        self.players = [
            Player("Alice", "LAL", points_per_game=25.0, assists_per_game=5.0, blocks_per_game=1.0),
            Player("Bob", "GSW", points_per_game=20.0, assists_per_game=8.0, blocks_per_game=0.5),
            Player("Charlie", "BOS", points_per_game=30.0, assists_per_game=3.0, blocks_per_game=2.0),
        ]

    def test_numpy_sort_by_ppg_descending(self):
        """Test numpy_sort sorts by ppg in descending order."""
        result = numpy_sort(self.players, stat="ppg", descending=True)
        expected_order = ["Charlie", "Alice", "Bob"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)

    def test_numpy_sort_by_ppg_ascending(self):
        """Test numpy_sort sorts by ppg in ascending order."""
        result = numpy_sort(self.players, stat="ppg", descending=False)
        expected_order = ["Bob", "Alice", "Charlie"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)

    def test_numpy_sort_by_apg_descending(self):
        """Test numpy_sort sorts by assists per game in descending order."""
        result = numpy_sort(self.players, stat="apg", descending=True)
        expected_order = ["Bob", "Alice", "Charlie"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)


class TestInsertionSort(unittest.TestCase):
    """Tests for insertion_sort algorithm."""

    def setUp(self):
        """Create small test player lists."""
        self.players = [
            Player("Alice", "LAL", points_per_game=25.0, assists_per_game=5.0, blocks_per_game=1.0),
            Player("Bob", "GSW", points_per_game=20.0, assists_per_game=8.0, blocks_per_game=0.5),
            Player("Charlie", "BOS", points_per_game=30.0, assists_per_game=3.0, blocks_per_game=2.0),
        ]

    def test_insertion_sort_by_ppg_descending(self):
        """Test insertion_sort sorts by ppg in descending order."""
        result = insertion_sort(self.players, stat="ppg", descending=True)
        expected_order = ["Charlie", "Alice", "Bob"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)

    def test_insertion_sort_by_bpg_descending(self):
        """Test insertion_sort sorts by blocks per game in descending order."""
        result = insertion_sort(self.players, stat="bpg", descending=True)
        expected_order = ["Charlie", "Alice", "Bob"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)

    def test_insertion_sort_by_apg_ascending(self):
        """Test insertion_sort sorts by assists per game in ascending order."""
        result = insertion_sort(self.players, stat="apg", descending=False)
        expected_order = ["Charlie", "Alice", "Bob"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)


class TestHeapsort(unittest.TestCase):
    """Tests for heapsort algorithm."""

    def setUp(self):
        """Create small test player lists."""
        self.players = [
            Player("Alice", "LAL", points_per_game=25.0, assists_per_game=5.0, blocks_per_game=1.0),
            Player("Bob", "GSW", points_per_game=20.0, assists_per_game=8.0, blocks_per_game=0.5),
            Player("Charlie", "BOS", points_per_game=30.0, assists_per_game=3.0, blocks_per_game=2.0),
        ]

    def test_heapsort_by_ppg_descending(self):
        """Test heapsort sorts by ppg in descending order."""
        result = heapsort(self.players, stat="ppg", descending=True)
        expected_order = ["Charlie", "Alice", "Bob"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)

    def test_heapsort_by_bpg_ascending(self):
        """Test heapsort sorts by blocks per game in ascending order."""
        result = heapsort(self.players, stat="bpg", descending=False)
        expected_order = ["Bob", "Alice", "Charlie"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)

    def test_heapsort_by_apg_descending(self):
        """Test heapsort sorts by assists per game in descending order."""
        result = heapsort(self.players, stat="apg", descending=True)
        expected_order = ["Bob", "Alice", "Charlie"]
        actual_order = [p.name for p in result]
        self.assertEqual(expected_order, actual_order)


if __name__ == "__main__":
    unittest.main()
