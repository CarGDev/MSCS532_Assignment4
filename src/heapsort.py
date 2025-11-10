"""
Heapsort Implementation

This module provides a complete implementation of the Heapsort algorithm
using a max-heap data structure. The implementation includes:
- Max-heap construction
- Heap property maintenance
- In-place sorting with O(n log n) time complexity

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

from typing import List, TypeVar, Callable

T = TypeVar('T')


def _heapify(arr: List[T], n: int, i: int, key: Callable[[T], T] = lambda x: x) -> None:
    """
    Maintain the max-heap property for a subtree rooted at index i.
    
    This function assumes that the subtrees rooted at left and right children
    are already max-heaps, and ensures that the subtree rooted at i is also a max-heap.
    
    Time Complexity: O(log n) where n is the size of the heap
    
    Args:
        arr: The array representing the heap
        n: Size of the heap (may be smaller than len(arr))
        i: Index of the root of the subtree to heapify
        key: Optional function to extract comparison key from elements
    
    Examples:
        >>> arr = [4, 10, 3, 5, 1]
        >>> _heapify(arr, 5, 0)
        >>> arr
        [10, 5, 3, 4, 1]
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index
    
    # Compare root with left child
    if left < n and key(arr[left]) > key(arr[largest]):
        largest = left
    
    # Compare largest with right child
    if right < n and key(arr[right]) > key(arr[largest]):
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest, key)


def _build_max_heap(arr: List[T], key: Callable[[T], T] = lambda x: x) -> None:
    """
    Build a max-heap from an unsorted array.
    
    This function rearranges the array elements to satisfy the max-heap property.
    It starts from the last non-leaf node and works backwards to the root.
    
    Time Complexity: O(n) - linear time despite nested loops
    
    Args:
        arr: The array to convert into a max-heap
        key: Optional function to extract comparison key from elements
    
    Examples:
        >>> arr = [4, 10, 3, 5, 1]
        >>> _build_max_heap(arr)
        >>> arr
        [10, 5, 3, 4, 1]
    """
    n = len(arr)
    # Start from the last non-leaf node and work backwards
    # Last non-leaf node is at index (n // 2) - 1
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i, key)


def heapsort(arr: List[T], key: Callable[[T], T] = lambda x: x, inplace: bool = True) -> List[T]:
    """
    Sort an array using the Heapsort algorithm.
    
    Heapsort is an in-place sorting algorithm with O(n log n) time complexity
    in all cases (worst, average, and best). It works by:
    1. Building a max-heap from the input array
    2. Repeatedly extracting the maximum element and placing it at the end
    3. Reducing the heap size and maintaining the heap property
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(1) for in-place sorting, O(n) if not in-place
    
    Args:
        arr: The array to sort
        key: Optional function to extract comparison key from elements
        inplace: If True, sort in-place (modifies original array). If False, returns a new sorted array.
    
    Returns:
        List[T]: The sorted array (same reference if inplace=True, new list if inplace=False)
    
    Examples:
        >>> arr = [12, 11, 13, 5, 6, 7]
        >>> heapsort(arr)
        [5, 6, 7, 11, 12, 13]
        >>> arr
        [5, 6, 7, 11, 12, 13]
        
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> sorted_arr = heapsort(arr, inplace=False)
        >>> sorted_arr
        [1, 1, 2, 3, 4, 5, 6, 9]
        >>> arr
        [3, 1, 4, 1, 5, 9, 2, 6]
    """
    if not arr:
        return arr
    
    # Create a copy if not sorting in-place
    if not inplace:
        arr = arr.copy()
    
    n = len(arr)
    
    # Step 1: Build max-heap
    _build_max_heap(arr, key)
    
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (maximum) to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Reduce heap size and heapify the root
        _heapify(arr, i, 0, key)
    
    return arr


def heap_extract_max(arr: List[T], key: Callable[[T], T] = lambda x: x) -> T:
    """
    Extract and return the maximum element from a max-heap.
    
    This function removes the maximum element from the heap and maintains
    the heap property. The heap is assumed to be a valid max-heap.
    
    Time Complexity: O(log n)
    
    Args:
        arr: The max-heap array
        key: Optional function to extract comparison key from elements
    
    Returns:
        T: The maximum element
    
    Raises:
        IndexError: If the heap is empty
    
    Examples:
        >>> heap = [10, 5, 3, 4, 1]
        >>> max_val = heap_extract_max(heap)
        >>> max_val
        10
        >>> heap
        [5, 4, 3, 1]
    """
    if not arr:
        raise IndexError("Cannot extract from empty heap")
    
    if len(arr) == 1:
        return arr.pop()
    
    # Store the maximum (root)
    max_val = arr[0]
    
    # Move last element to root
    arr[0] = arr.pop()
    
    # Heapify to maintain heap property
    _heapify(arr, len(arr), 0, key)
    
    return max_val


def heap_insert(arr: List[T], item: T, key: Callable[[T], T] = lambda x: x) -> None:
    """
    Insert an element into a max-heap.
    
    This function adds a new element to the heap and maintains the heap property
    by bubbling up the element if necessary.
    
    Time Complexity: O(log n)
    
    Args:
        arr: The max-heap array
        item: The element to insert
        key: Optional function to extract comparison key from elements
    
    Examples:
        >>> heap = [10, 5, 3, 4, 1]
        >>> heap_insert(heap, 15)
        >>> heap
        [15, 10, 3, 4, 1, 5]
    """
    arr.append(item)
    i = len(arr) - 1
    
    # Bubble up: compare with parent and swap if necessary
    while i > 0:
        parent = (i - 1) // 2
        if key(arr[parent]) >= key(arr[i]):
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent

