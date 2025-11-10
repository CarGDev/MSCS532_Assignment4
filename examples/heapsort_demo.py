#!/usr/bin/env python3
"""
Heapsort Demonstration Script

This script demonstrates the usage of the heapsort implementation
with various examples and use cases.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.heapsort import heapsort, heap_extract_max, heap_insert, _build_max_heap


def demo_basic_sorting():
    """Demonstrate basic heapsort functionality."""
    print("=" * 80)
    print("BASIC HEAPSORT DEMONSTRATION")
    print("=" * 80)
    
    # Example 1: Simple array
    print("\n1. Sorting a simple array:")
    arr = [12, 11, 13, 5, 6, 7]
    print(f"   Original: {arr}")
    sorted_arr = heapsort(arr.copy(), inplace=False)
    print(f"   Sorted:   {sorted_arr}")
    
    # Example 2: Already sorted array
    print("\n2. Sorting an already sorted array:")
    arr = [1, 2, 3, 4, 5]
    print(f"   Original: {arr}")
    sorted_arr = heapsort(arr.copy(), inplace=False)
    print(f"   Sorted:   {sorted_arr}")
    
    # Example 3: Reverse sorted array
    print("\n3. Sorting a reverse-sorted array:")
    arr = [5, 4, 3, 2, 1]
    print(f"   Original: {arr}")
    sorted_arr = heapsort(arr.copy(), inplace=False)
    print(f"   Sorted:   {sorted_arr}")
    
    # Example 4: Array with duplicates
    print("\n4. Sorting an array with duplicate elements:")
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"   Original: {arr}")
    sorted_arr = heapsort(arr.copy(), inplace=False)
    print(f"   Sorted:   {sorted_arr}")
    
    # Example 5: In-place sorting
    print("\n5. In-place sorting:")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"   Before: {arr}")
    heapsort(arr, inplace=True)
    print(f"   After:  {arr}")


def demo_heap_operations():
    """Demonstrate heap utility operations."""
    print("\n" + "=" * 80)
    print("HEAP OPERATIONS DEMONSTRATION")
    print("=" * 80)
    
    # Build max-heap
    print("\n1. Building a max-heap:")
    arr = [4, 10, 3, 5, 1]
    print(f"   Original array: {arr}")
    _build_max_heap(arr)
    print(f"   Max-heap:      {arr}")
    print(f"   Root (max):    {arr[0]}")
    
    # Extract maximum
    print("\n2. Extracting maximum from heap:")
    heap = [10, 5, 3, 4, 1]
    _build_max_heap(heap)
    print(f"   Heap before: {heap}")
    max_val = heap_extract_max(heap)
    print(f"   Extracted:   {max_val}")
    print(f"   Heap after:  {heap}")
    
    # Insert into heap
    print("\n3. Inserting into heap:")
    heap = [10, 5, 3, 4, 1]
    _build_max_heap(heap)
    print(f"   Heap before: {heap}")
    heap_insert(heap, 15)
    print(f"   Inserted 15")
    print(f"   Heap after:  {heap}")
    print(f"   New root:    {heap[0]}")


def demo_custom_key():
    """Demonstrate sorting with custom key function."""
    print("\n" + "=" * 80)
    print("CUSTOM KEY FUNCTION DEMONSTRATION")
    print("=" * 80)
    
    # Sort dictionaries by value
    print("\n1. Sorting dictionaries by 'value' key:")
    arr = [
        {'name': 'Alice', 'value': 30},
        {'name': 'Bob', 'value': 20},
        {'name': 'Charlie', 'value': 40},
        {'name': 'David', 'value': 10}
    ]
    print(f"   Original: {[d['name'] for d in arr]}")
    sorted_arr = heapsort(arr.copy(), key=lambda x: x['value'], inplace=False)
    print(f"   Sorted by value: {[d['name'] for d in sorted_arr]}")
    
    # Sort tuples by second element
    print("\n2. Sorting tuples by second element:")
    arr = [(1, 5), (2, 3), (3, 8), (4, 1)]
    print(f"   Original: {arr}")
    sorted_arr = heapsort(arr.copy(), key=lambda x: x[1], inplace=False)
    print(f"   Sorted:   {sorted_arr}")


def demo_performance():
    """Demonstrate performance on different input sizes."""
    print("\n" + "=" * 80)
    print("PERFORMANCE DEMONSTRATION")
    print("=" * 80)
    
    import time
    import random
    
    sizes = [100, 1000, 10000]
    
    print("\nSorting random arrays of different sizes:")
    print(f"{'Size':<10} {'Time (seconds)':<20} {'Sorted':<10}")
    print("-" * 40)
    
    for size in sizes:
        arr = [random.randint(1, size * 10) for _ in range(size)]
        start = time.perf_counter()
        sorted_arr = heapsort(arr.copy(), inplace=False)
        end = time.perf_counter()
        is_sorted = sorted_arr == sorted(arr)
        print(f"{size:<10} {end - start:<20.6f} {str(is_sorted):<10}")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 80)
    print("HEAPSORT IMPLEMENTATION DEMONSTRATION")
    print("Author: Carlos Gutierrez")
    print("Email: cgutierrez44833@ucumberlands.edu")
    print("=" * 80)
    
    demo_basic_sorting()
    demo_heap_operations()
    demo_custom_key()
    demo_performance()
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()

