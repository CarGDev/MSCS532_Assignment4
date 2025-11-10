#!/usr/bin/env python3
"""
Generate Performance Comparison Plots

This script generates visualization plots comparing Heapsort, Quicksort,
and Merge Sort performance on different input sizes and distributions.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.comparison import compare_sorting_algorithms


def generate_performance_plots():
    """Generate performance comparison plots."""
    print("Generating performance comparison plots...")
    
    # Test sizes - using smaller sizes for faster generation
    sizes = [100, 500, 1000, 5000, 10000]
    
    print("Running performance comparisons...")
    results = compare_sorting_algorithms(sizes)
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract data for plotting
    algorithms = ['heapsort', 'quicksort', 'merge_sort']
    distributions = ['sorted', 'reverse_sorted', 'random']
    
    # Create figure with subplots
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Sorting Algorithm Performance Comparison', fontsize=16, fontweight='bold')
    
    colors = {
        'heapsort': '#2E86AB',
        'quicksort': '#A23B72',
        'merge_sort': '#F18F01'
    }
    
    markers = {
        'heapsort': 'o',
        'quicksort': 's',
        'merge_sort': '^'
    }
    
    for idx, dist in enumerate(distributions):
        ax = axes[idx]
        
        for algo in algorithms:
            times = results[algo][dist]
            ax.plot(sizes, times, 
                   marker=markers[algo], 
                   color=colors[algo],
                   linewidth=2,
                   markersize=8,
                   label=algo.replace('_', ' ').title())
        
        ax.set_xlabel('Input Size (n)', fontsize=12)
        ax.set_ylabel('Time (seconds)', fontsize=12)
        ax.set_title(f'{dist.replace("_", " ").title()} Input', fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=10)
        ax.set_xscale('log')
        ax.set_yscale('log')
    
    plt.tight_layout()
    plot_path = os.path.join(output_dir, 'sorting_comparison.png')
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    print(f"Saved plot to: {plot_path}")
    plt.close()
    
    # Create a combined comparison plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    x = np.arange(len(sizes))
    width = 0.25
    
    for i, algo in enumerate(algorithms):
        # Use random distribution for comparison
        times = results[algo]['random']
        ax.bar(x + i * width, times, width, 
              label=algo.replace('_', ' ').title(),
              color=colors[algo],
              alpha=0.8)
    
    ax.set_xlabel('Input Size (n)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Time (seconds)', fontsize=12, fontweight='bold')
    ax.set_title('Sorting Algorithm Performance on Random Input', fontsize=14, fontweight='bold')
    ax.set_xticks(x + width)
    ax.set_xticklabels([str(s) for s in sizes])
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    bar_plot_path = os.path.join(output_dir, 'sorting_comparison_bar.png')
    plt.savefig(bar_plot_path, dpi=300, bbox_inches='tight')
    print(f"Saved bar chart to: {bar_plot_path}")
    plt.close()
    
    # Create a line plot showing all distributions for each algorithm
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Algorithm Performance Across Different Input Distributions', fontsize=16, fontweight='bold')
    
    for idx, algo in enumerate(algorithms):
        ax = axes[idx]
        
        for dist in distributions:
            times = results[algo][dist]
            ax.plot(sizes, times,
                   marker='o',
                   linewidth=2,
                   markersize=6,
                   label=dist.replace('_', ' ').title())
        
        ax.set_xlabel('Input Size (n)', fontsize=12)
        ax.set_ylabel('Time (seconds)', fontsize=12)
        ax.set_title(f'{algo.replace("_", " ").title()} Performance', fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=10)
        ax.set_xscale('log')
        ax.set_yscale('log')
    
    plt.tight_layout()
    algo_dist_plot_path = os.path.join(output_dir, 'algorithm_distributions.png')
    plt.savefig(algo_dist_plot_path, dpi=300, bbox_inches='tight')
    print(f"Saved algorithm distribution plot to: {algo_dist_plot_path}")
    plt.close()
    
    print("\nAll plots generated successfully!")
    return {
        'comparison': plot_path,
        'bar_chart': bar_plot_path,
        'distributions': algo_dist_plot_path
    }


if __name__ == "__main__":
    try:
        generate_performance_plots()
    except ImportError:
        print("Error: matplotlib is required for generating plots.")
        print("Install it with: pip install matplotlib")
        sys.exit(1)

