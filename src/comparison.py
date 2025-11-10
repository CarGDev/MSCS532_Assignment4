"""
Sorting Algorithm Comparison Module

This module provides utilities to empirically compare the performance of
Heapsort with other sorting algorithms (Quicksort and Merge Sort) on
different input sizes and distributions.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import time
import random
from typing import List, Callable, Dict, Tuple
from .heapsort import heapsort


def quicksort(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    """
    Quicksort implementation for comparison.
    
    Time Complexity: O(n log n) average, O(n²) worst case
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
    
    Returns:
        List[int]: Sorted array
    """
    if high is None:
        high = len(arr) - 1
        arr = arr.copy()
    
    # Use iterative approach to avoid recursion depth issues
    stack = [(low, high)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pi = _partition(arr, low, high)
            # Push smaller partition first to reduce stack size
            if pi - low < high - pi:
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))
            else:
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))
    
    return arr


def _partition(arr: List[int], low: int, high: int) -> int:
    """Partition function for Quicksort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort implementation for comparison.
    
    Time Complexity: O(n log n) in all cases
    
    Args:
        arr: Array to sort
    
    Returns:
        List[int]: Sorted array
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merge function for Merge Sort."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def generate_sorted_array(n: int) -> List[int]:
    """Generate a sorted array of size n."""
    return list(range(n))


def generate_reverse_sorted_array(n: int) -> List[int]:
    """Generate a reverse-sorted array of size n."""
    return list(range(n, 0, -1))


def generate_random_array(n: int, seed: int = None) -> List[int]:
    """Generate a random array of size n."""
    if seed is not None:
        random.seed(seed)
    return [random.randint(1, n * 10) for _ in range(n)]


def measure_time(func: Callable, arr: List[int]) -> Tuple[float, List[int]]:
    """
    Measure the execution time of a sorting function.
    
    Args:
        func: The sorting function to measure
        arr: The array to sort
    
    Returns:
        Tuple[float, List[int]]: Execution time in seconds and sorted array
    """
    start_time = time.perf_counter()
    sorted_arr = func(arr)
    end_time = time.perf_counter()
    return end_time - start_time, sorted_arr


def compare_sorting_algorithms(
    sizes: List[int],
    distributions: Dict[str, Callable[[int], List[int]]] = None
) -> Dict[str, Dict[str, List[float]]]:
    """
    Compare Heapsort, Quicksort, and Merge Sort on different input sizes and distributions.
    
    Args:
        sizes: List of input sizes to test
        distributions: Dictionary mapping distribution names to generator functions
    
    Returns:
        Dictionary containing timing results for each algorithm and distribution
    
    Examples:
        >>> results = compare_sorting_algorithms([100, 1000, 10000])
        >>> print(results['heapsort']['random'][0])
    """
    if distributions is None:
        distributions = {
            'sorted': generate_sorted_array,
            'reverse_sorted': generate_reverse_sorted_array,
            'random': generate_random_array
        }
    
    algorithms = {
        'heapsort': lambda arr: heapsort(arr.copy()),
        'quicksort': quicksort,
        'merge_sort': merge_sort
    }
    
    results = {
        algo: {dist: [] for dist in distributions.keys()}
        for algo in algorithms.keys()
    }
    
    for size in sizes:
        print(f"Testing with size {size}...")
        for dist_name, dist_func in distributions.items():
            arr = dist_func(size)
            
            for algo_name, algo_func in algorithms.items():
                time_taken, _ = measure_time(algo_func, arr)
                results[algo_name][dist_name].append(time_taken)
                print(f"  {algo_name} ({dist_name}): {time_taken:.6f}s")
    
    return results


def print_comparison_results(results: Dict[str, Dict[str, List[float]]], sizes: List[int]) -> None:
    """
    Print comparison results in a formatted table.
    
    Args:
        results: Results dictionary from compare_sorting_algorithms
        sizes: List of input sizes that were tested
    """
    print("\n" + "=" * 80)
    print("SORTING ALGORITHM COMPARISON RESULTS")
    print("=" * 80)
    
    distributions = list(next(iter(results.values())).keys())
    
    for dist in distributions:
        print(f"\n{dist.upper().replace('_', ' ')} INPUT:")
        print("-" * 80)
        print(f"{'Size':<10} {'Heapsort':<15} {'Quicksort':<15} {'Merge Sort':<15}")
        print("-" * 80)
        
        for i, size in enumerate(sizes):
            heapsort_time = results['heapsort'][dist][i]
            quicksort_time = results['quicksort'][dist][i]
            merge_sort_time = results['merge_sort'][dist][i]
            
            print(f"{size:<10} {heapsort_time:<15.6f} {quicksort_time:<15.6f} {merge_sort_time:<15.6f}")
        
        print("-" * 80)


def run_comparison(sizes: List[int] = None) -> Dict[str, Dict[str, List[float]]]:
    """
    Run a complete comparison of sorting algorithms.
    
    Args:
        sizes: List of input sizes to test (default: [100, 1000, 10000, 100000])
    
    Returns:
        Dictionary containing timing results
    """
    if sizes is None:
        sizes = [100, 1000, 10000, 100000]
    
    print("Starting sorting algorithm comparison...")
    print(f"Testing sizes: {sizes}")
    print()
    
    results = compare_sorting_algorithms(sizes)
    print_comparison_results(results, sizes)
    
    return results

