#!/usr/bin/env python3
"""
Sorting Algorithm Comparison Demonstration

This script demonstrates the empirical comparison of Heapsort,
Quicksort, and Merge Sort on different input sizes and distributions.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.comparison import run_comparison


def main():
    """Run sorting algorithm comparison."""
    print("\n" + "=" * 80)
    print("SORTING ALGORITHM COMPARISON DEMONSTRATION")
    print("Author: Carlos Gutierrez")
    print("Email: cgutierrez44833@ucumberlands.edu")
    print("=" * 80)
    
    # Run comparison with different sizes
    # Note: Large sizes may take significant time
    sizes = [100, 1000, 10000]
    
    print(f"\nComparing Heapsort, Quicksort, and Merge Sort")
    print(f"Input sizes: {sizes}")
    print(f"\nNote: This may take a few moments...\n")
    
    results = run_comparison(sizes=sizes)
    
    print("\n" + "=" * 80)
    print("COMPARISON COMPLETE")
    print("=" * 80)
    print("\nKey Observations:")
    print("1. Heapsort: Consistent O(n log n) performance across all input types")
    print("2. Quicksort: Fastest on average, but degrades on sorted inputs")
    print("3. Merge Sort: Consistent performance, requires O(n) extra space")
    print("\nSee README.md for detailed analysis.\n")


if __name__ == "__main__":
    main()

