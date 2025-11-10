#!/usr/bin/env python3
"""
Priority Queue Demonstration Script

This script demonstrates the usage of the priority queue implementation
with various examples and use cases.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.priority_queue import PriorityQueue
from src.task import Task


def demo_basic_operations():
    """Demonstrate basic priority queue operations."""
    print("=" * 80)
    print("BASIC PRIORITY QUEUE OPERATIONS")
    print("=" * 80)
    
    # Create a max-heap priority queue
    pq = PriorityQueue(is_max_heap=True)
    
    print("\n1. Creating and inserting tasks:")
    tasks = [
        Task("T1", priority=10, arrival_time=0.0, description="Task 1"),
        Task("T2", priority=5, arrival_time=1.0, description="Task 2"),
        Task("T3", priority=15, arrival_time=2.0, description="Task 3"),
        Task("T4", priority=20, arrival_time=3.0, description="Task 4"),
        Task("T5", priority=8, arrival_time=4.0, description="Task 5")
    ]
    
    for task in tasks:
        pq.insert(task)
        print(f"   Inserted: {task.task_id} (priority: {task.priority})")
    
    print(f"\n   Queue size: {pq.size()}")
    print(f"   Is empty: {pq.is_empty()}")
    
    # Peek at highest priority
    print("\n2. Peeking at highest priority task:")
    top_task = pq.peek()
    print(f"   Top task: {top_task.task_id} (priority: {top_task.priority})")
    print(f"   Queue size after peek: {pq.size()} (unchanged)")
    
    # Extract tasks in priority order
    print("\n3. Extracting tasks in priority order:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"   Extracted: {task.task_id} (priority: {task.priority})")
    
    print(f"\n   Queue size: {pq.size()}")
    print(f"   Is empty: {pq.is_empty()}")


def demo_min_heap():
    """Demonstrate min-heap priority queue."""
    print("\n" + "=" * 80)
    print("MIN-HEAP PRIORITY QUEUE")
    print("=" * 80)
    
    pq = PriorityQueue(is_max_heap=False)
    
    print("\nInserting tasks into min-heap:")
    tasks = [
        Task("T1", priority=10, arrival_time=0.0),
        Task("T2", priority=5, arrival_time=1.0),
        Task("T3", priority=15, arrival_time=2.0),
        Task("T4", priority=20, arrival_time=3.0),
        Task("T5", priority=8, arrival_time=4.0)
    ]
    
    for task in tasks:
        pq.insert(task)
        print(f"   Inserted: {task.task_id} (priority: {task.priority})")
    
    print("\nExtracting tasks (lowest priority first):")
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"   Extracted: {task.task_id} (priority: {task.priority})")


def demo_key_operations():
    """Demonstrate priority key update operations."""
    print("\n" + "=" * 80)
    print("PRIORITY KEY UPDATE OPERATIONS")
    print("=" * 80)
    
    pq = PriorityQueue(is_max_heap=True)
    
    # Insert tasks
    task1 = Task("T1", priority=10, arrival_time=0.0)
    task2 = Task("T2", priority=20, arrival_time=1.0)
    task3 = Task("T3", priority=15, arrival_time=2.0)
    
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    
    print("\nInitial state:")
    print(f"   Top task: {pq.peek().task_id} (priority: {pq.peek().priority})")
    
    # Increase priority
    print("\n1. Increasing T1's priority from 10 to 25:")
    success = pq.increase_key(task1, 25)
    print(f"   Update successful: {success}")
    print(f"   New priority: {task1.priority}")
    print(f"   Top task: {pq.peek().task_id} (priority: {pq.peek().priority})")
    
    # Decrease priority
    print("\n2. Decreasing T1's priority from 25 to 12:")
    success = pq.decrease_key(task1, 12)
    print(f"   Update successful: {success}")
    print(f"   New priority: {task1.priority}")
    print(f"   Top task: {pq.peek().task_id} (priority: {pq.peek().priority})")


def demo_task_scheduling():
    """Demonstrate task scheduling simulation."""
    print("\n" + "=" * 80)
    print("TASK SCHEDULING SIMULATION")
    print("=" * 80)
    
    pq = PriorityQueue(is_max_heap=True)
    
    # Create tasks with deadlines
    tasks = [
        Task("T1", priority=10, arrival_time=0.0, deadline=100.0, execution_time=5.0),
        Task("T2", priority=15, arrival_time=1.0, deadline=50.0, execution_time=3.0),
        Task("T3", priority=8, arrival_time=2.0, deadline=200.0, execution_time=10.0),
        Task("T4", priority=20, arrival_time=3.0, deadline=30.0, execution_time=2.0),
        Task("T5", priority=12, arrival_time=4.0, deadline=150.0, execution_time=7.0)
    ]
    
    print("\nTasks to schedule:")
    for task in tasks:
        print(f"   {task.task_id}: priority={task.priority}, deadline={task.deadline}, "
              f"execution_time={task.execution_time}")
    
    # Insert all tasks
    for task in tasks:
        pq.insert(task)
    
    print("\nScheduling order (by priority):")
    current_time = 0.0
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"\n   Executing: {task.task_id}")
        print(f"   Priority: {task.priority}")
        print(f"   Start time: {current_time}")
        print(f"   Execution time: {task.execution_time}")
        print(f"   Deadline: {task.deadline}")
        
        # Check if task will meet deadline
        completion_time = current_time + task.execution_time
        if task.deadline and completion_time > task.deadline:
            print(f"   ⚠️  WARNING: Will miss deadline!")
        else:
            print(f"   ✓ Will meet deadline")
        
        current_time = completion_time
    
    print(f"\n   Total completion time: {current_time}")


def demo_large_queue():
    """Demonstrate performance with large queue."""
    print("\n" + "=" * 80)
    print("LARGE QUEUE PERFORMANCE")
    print("=" * 80)
    
    import time
    
    pq = PriorityQueue(is_max_heap=True)
    num_tasks = 10000
    
    print(f"\nInserting {num_tasks} tasks...")
    start = time.perf_counter()
    for i in range(num_tasks):
        priority = (i * 7) % 100  # Vary priorities
        task = Task(f"T{i}", priority=priority, arrival_time=float(i))
        pq.insert(task)
    insert_time = time.perf_counter() - start
    
    print(f"   Insert time: {insert_time:.6f} seconds")
    print(f"   Queue size: {pq.size()}")
    
    print(f"\nExtracting all tasks...")
    start = time.perf_counter()
    count = 0
    prev_priority = float('inf')
    while not pq.is_empty():
        task = pq.extract_max()
        # Verify ordering
        assert task.priority <= prev_priority, "Ordering violated!"
        prev_priority = task.priority
        count += 1
    extract_time = time.perf_counter() - start
    
    print(f"   Extract time: {extract_time:.6f} seconds")
    print(f"   Tasks extracted: {count}")
    print(f"   Ordering verified: ✓")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 80)
    print("PRIORITY QUEUE IMPLEMENTATION DEMONSTRATION")
    print("Author: Carlos Gutierrez")
    print("Email: cgutierrez44833@ucumberlands.edu")
    print("=" * 80)
    
    demo_basic_operations()
    demo_min_heap()
    demo_key_operations()
    demo_task_scheduling()
    demo_large_queue()
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()

