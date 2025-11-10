#!/usr/bin/env python3
"""
Task Scheduler Simulation Demonstration

This script demonstrates the task scheduler implementation using the priority queue.
It shows various scheduling scenarios and analyzes the results.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scheduler import TaskScheduler, simulate_scheduler
from src.task import Task


def demo_basic_scheduling():
    """Demonstrate basic priority-based scheduling."""
    print("=" * 80)
    print("BASIC PRIORITY-BASED SCHEDULING")
    print("=" * 80)
    
    scheduler = TaskScheduler()
    
    # Create tasks with different priorities
    tasks = [
        Task("T1", priority=10, arrival_time=0.0, execution_time=5.0, description="Low priority task"),
        Task("T2", priority=30, arrival_time=0.0, execution_time=3.0, description="High priority task"),
        Task("T3", priority=20, arrival_time=0.0, execution_time=4.0, description="Medium priority task"),
        Task("T4", priority=15, arrival_time=0.0, execution_time=2.0, description="Medium-low priority task"),
    ]
    
    print("\nTasks to schedule (in priority order):")
    for task in sorted(tasks, key=lambda t: t.priority, reverse=True):
        print(f"  {task.task_id}: priority={task.priority}, execution_time={task.execution_time}")
    
    results = scheduler.schedule_tasks(tasks)
    scheduler.print_schedule(results)


def demo_deadline_scheduling():
    """Demonstrate scheduling with deadlines."""
    print("\n" + "=" * 80)
    print("SCHEDULING WITH DEADLINES")
    print("=" * 80)
    
    scheduler = TaskScheduler()
    
    # Create tasks with deadlines
    tasks = [
        Task("T1", priority=10, arrival_time=0.0, deadline=100.0, execution_time=5.0),
        Task("T2", priority=20, arrival_time=0.0, deadline=30.0, execution_time=3.0),
        Task("T3", priority=15, arrival_time=0.0, deadline=50.0, execution_time=10.0),
        Task("T4", priority=25, arrival_time=0.0, deadline=20.0, execution_time=2.0),
        Task("T5", priority=12, arrival_time=0.0, deadline=150.0, execution_time=7.0),
    ]
    
    print("\nTasks with deadlines:")
    for task in tasks:
        print(f"  {task.task_id}: priority={task.priority}, deadline={task.deadline}, "
              f"execution_time={task.execution_time}")
    
    results = scheduler.schedule_tasks(tasks)
    scheduler.print_schedule(results)


def demo_large_workload():
    """Demonstrate scheduling a large number of tasks."""
    print("\n" + "=" * 80)
    print("LARGE WORKLOAD SCHEDULING")
    print("=" * 80)
    
    import random
    
    # Generate random tasks
    num_tasks = 50
    tasks = []
    random.seed(42)  # For reproducibility
    
    for i in range(num_tasks):
        priority = random.randint(1, 100)
        execution_time = random.uniform(0.5, 10.0)
        deadline = random.uniform(10.0, 200.0)
        tasks.append(
            Task(f"T{i+1}", priority=priority, arrival_time=0.0, 
                 deadline=deadline, execution_time=execution_time)
        )
    
    print(f"\nScheduling {num_tasks} tasks...")
    stats = simulate_scheduler(tasks, verbose=False)
    
    print(f"\nScheduling Statistics:")
    print(f"  Total tasks: {stats.total_tasks}")
    print(f"  Completed: {stats.completed_tasks}")
    print(f"  Deadline met: {stats.deadline_met} ({stats.deadline_met/stats.total_tasks*100:.1f}%)")
    print(f"  Deadline missed: {stats.deadline_missed} ({stats.deadline_missed/stats.total_tasks*100:.1f}%)")
    print(f"  Total execution time: {stats.total_execution_time:.2f}")
    print(f"  Average wait time: {stats.average_wait_time:.2f}")
    print(f"  Throughput: {stats.throughput:.2f} tasks/time unit")


def demo_priority_vs_deadline():
    """Compare priority-based vs deadline-based scheduling."""
    print("\n" + "=" * 80)
    print("PRIORITY-BASED vs DEADLINE-AWARE SCHEDULING")
    print("=" * 80)
    
    # Create tasks where high priority tasks have tight deadlines
    tasks = [
        Task("T1", priority=30, arrival_time=0.0, deadline=15.0, execution_time=10.0),
        Task("T2", priority=20, arrival_time=0.0, deadline=50.0, execution_time=5.0),
        Task("T3", priority=10, arrival_time=0.0, deadline=100.0, execution_time=3.0),
    ]
    
    print("\nScenario: High priority task (T1) has tight deadline")
    print("Tasks:")
    for task in tasks:
        print(f"  {task.task_id}: priority={task.priority}, deadline={task.deadline}, "
              f"execution_time={task.execution_time}")
    
    # Priority-based scheduling
    scheduler = TaskScheduler()
    results = scheduler.schedule_tasks(tasks)
    
    print("\nPriority-based scheduling (highest priority first):")
    scheduler.print_schedule(results)
    
    # Note: This demonstrates that pure priority scheduling may miss deadlines
    # A more sophisticated scheduler could use deadline-aware priority adjustment


def main():
    """Run all scheduler demonstrations."""
    print("\n" + "=" * 80)
    print("TASK SCHEDULER SIMULATION DEMONSTRATION")
    print("Author: Carlos Gutierrez")
    print("Email: cgutierrez44833@ucumberlands.edu")
    print("=" * 80)
    
    demo_basic_scheduling()
    demo_deadline_scheduling()
    demo_large_workload()
    demo_priority_vs_deadline()
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)
    print("\nKey Observations:")
    print("1. Priority-based scheduling ensures high-priority tasks execute first")
    print("2. Pure priority scheduling may miss deadlines for lower-priority tasks")
    print("3. The scheduler efficiently handles large workloads using O(n log n) algorithm")
    print("4. Statistics provide insights into scheduling performance")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()

