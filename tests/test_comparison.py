"""
Test Suite for Sorting Algorithm Comparison

This module contains tests for the comparison utilities and sorting algorithms.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import unittest
import sys
import os

# Add parent directory to path to import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.comparison import (
    quicksort, merge_sort,
    generate_sorted_array, generate_reverse_sorted_array, generate_random_array
)


class TestSortingAlgorithms(unittest.TestCase):
    """Test cases for sorting algorithm implementations."""
    
    def test_quicksort_empty(self):
        """Test quicksort on empty array."""
        arr = []
        result = quicksort(arr)
        self.assertEqual(result, [])
    
    def test_quicksort_single(self):
        """Test quicksort on single element."""
        arr = [42]
        result = quicksort(arr)
        self.assertEqual(result, [42])
    
    def test_quicksort_sorted(self):
        """Test quicksort on sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_quicksort_reverse(self):
        """Test quicksort on reverse-sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_quicksort_random(self):
        """Test quicksort on random array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = quicksort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_merge_sort_empty(self):
        """Test merge sort on empty array."""
        arr = []
        result = merge_sort(arr)
        self.assertEqual(result, [])
    
    def test_merge_sort_single(self):
        """Test merge sort on single element."""
        arr = [42]
        result = merge_sort(arr)
        self.assertEqual(result, [42])
    
    def test_merge_sort_sorted(self):
        """Test merge sort on sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_merge_sort_reverse(self):
        """Test merge sort on reverse-sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_merge_sort_random(self):
        """Test merge sort on random array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])


class TestArrayGenerators(unittest.TestCase):
    """Test cases for array generator functions."""
    
    def test_generate_sorted_array(self):
        """Test generating sorted array."""
        arr = generate_sorted_array(5)
        self.assertEqual(arr, [0, 1, 2, 3, 4])
        self.assertEqual(len(arr), 5)
    
    def test_generate_reverse_sorted_array(self):
        """Test generating reverse-sorted array."""
        arr = generate_reverse_sorted_array(5)
        self.assertEqual(arr, [5, 4, 3, 2, 1])
        self.assertEqual(len(arr), 5)
    
    def test_generate_random_array(self):
        """Test generating random array."""
        arr = generate_random_array(10, seed=42)
        self.assertEqual(len(arr), 10)
        # With same seed, should get same array
        arr2 = generate_random_array(10, seed=42)
        self.assertEqual(arr, arr2)
    
    def test_generate_random_array_different_seeds(self):
        """Test that different seeds produce different arrays."""
        arr1 = generate_random_array(100, seed=1)
        arr2 = generate_random_array(100, seed=2)
        # Very unlikely to be the same
        self.assertNotEqual(arr1, arr2)


if __name__ == '__main__':
    unittest.main()

