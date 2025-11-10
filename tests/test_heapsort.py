"""
Test Suite for Heapsort Implementation

This module contains comprehensive tests for the heapsort algorithm,
including edge cases, different data types, and correctness verification.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import unittest
import sys
import os

# Add parent directory to path to import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.heapsort import heapsort, heap_extract_max, heap_insert, _build_max_heap, _heapify


class TestHeapsort(unittest.TestCase):
    """Test cases for heapsort function."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        arr = []
        result = heapsort(arr)
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Test sorting an array with a single element."""
        arr = [42]
        result = heapsort(arr)
        self.assertEqual(result, [42])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = heapsort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse-sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = heapsort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_random_array(self):
        """Test sorting a random array."""
        arr = [12, 11, 13, 5, 6, 7]
        result = heapsort(arr)
        self.assertEqual(result, [5, 6, 7, 11, 12, 13])
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = heapsort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        arr = [-5, -2, -8, 1, 3, -1]
        result = heapsort(arr)
        self.assertEqual(result, [-8, -5, -2, -1, 1, 3])
    
    def test_large_array(self):
        """Test sorting a large array."""
        arr = list(range(1000, 0, -1))
        result = heapsort(arr)
        self.assertEqual(result, list(range(1, 1001)))
    
    def test_inplace_sorting(self):
        """Test that inplace sorting modifies the original array."""
        arr = [3, 1, 4, 1, 5]
        original_id = id(arr)
        result = heapsort(arr, inplace=True)
        self.assertEqual(id(result), original_id)
        self.assertEqual(arr, [1, 1, 3, 4, 5])
    
    def test_not_inplace_sorting(self):
        """Test that non-inplace sorting doesn't modify the original array."""
        arr = [3, 1, 4, 1, 5]
        original_arr = arr.copy()
        result = heapsort(arr, inplace=False)
        self.assertNotEqual(id(result), id(arr))
        self.assertEqual(arr, original_arr)
        self.assertEqual(result, [1, 1, 3, 4, 5])
    
    def test_custom_key_function(self):
        """Test sorting with a custom key function."""
        arr = [{'value': 3}, {'value': 1}, {'value': 4}]
        result = heapsort(arr, key=lambda x: x['value'], inplace=False)
        self.assertEqual([x['value'] for x in result], [1, 3, 4])


class TestHeapOperations(unittest.TestCase):
    """Test cases for heap utility functions."""
    
    def test_heapify(self):
        """Test the heapify function."""
        arr = [4, 10, 3, 5, 1]
        _heapify(arr, 5, 0)
        # After heapify, root should be the maximum
        self.assertEqual(arr[0], 10)
    
    def test_build_max_heap(self):
        """Test building a max-heap from an array."""
        arr = [4, 10, 3, 5, 1]
        _build_max_heap(arr)
        # Root should be maximum
        self.assertEqual(arr[0], 10)
        # Verify heap property: parent >= children
        for i in range(len(arr)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(arr):
                self.assertGreaterEqual(arr[i], arr[left])
            if right < len(arr):
                self.assertGreaterEqual(arr[i], arr[right])
    
    def test_heap_extract_max(self):
        """Test extracting maximum from a heap."""
        heap = [10, 5, 3, 4, 1]
        _build_max_heap(heap)
        max_val = heap_extract_max(heap)
        self.assertEqual(max_val, 10)
        self.assertEqual(len(heap), 4)
        # Verify heap property is maintained
        self.assertEqual(heap[0], 5)
    
    def test_heap_extract_max_empty(self):
        """Test extracting from an empty heap raises error."""
        heap = []
        with self.assertRaises(IndexError):
            heap_extract_max(heap)
    
    def test_heap_insert(self):
        """Test inserting into a heap."""
        heap = [10, 5, 3, 4, 1]
        _build_max_heap(heap)
        heap_insert(heap, 15)
        # New maximum should be at root
        self.assertEqual(heap[0], 15)
        # Verify heap property
        for i in range(len(heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(heap):
                self.assertGreaterEqual(heap[i], heap[left])
            if right < len(heap):
                self.assertGreaterEqual(heap[i], heap[right])


if __name__ == '__main__':
    unittest.main()

