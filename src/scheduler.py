"""
Task Scheduler Simulation

This module implements a task scheduler using the priority queue data structure.
The scheduler demonstrates how priority queues can be used for task scheduling
in operating systems, job queues, and other scheduling applications.

The scheduler supports:
- Priority-based scheduling (highest priority first)
- Deadline monitoring
- Execution time tracking
- Scheduling statistics and analysis

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from .priority_queue import PriorityQueue
from .task import Task


@dataclass
class SchedulingResult:
    """
    Represents the result of scheduling a task.
    
    Attributes:
        task_id (str): ID of the scheduled task
        start_time (float): Time when task execution started
        completion_time (float): Time when task execution completed
        deadline_met (bool): Whether the task met its deadline
        wait_time (float): Time the task waited before execution
    """
    task_id: str
    start_time: float
    completion_time: float
    deadline_met: bool
    wait_time: float


@dataclass
class SchedulingStatistics:
    """
    Statistics from a scheduling simulation.
    
    Attributes:
        total_tasks (int): Total number of tasks scheduled
        completed_tasks (int): Number of tasks that completed
        deadline_met (int): Number of tasks that met their deadlines
        deadline_missed (int): Number of tasks that missed their deadlines
        total_execution_time (float): Total time spent executing tasks
        average_wait_time (float): Average wait time for all tasks
        throughput (float): Tasks completed per unit time
    """
    total_tasks: int
    completed_tasks: int
    deadline_met: int
    deadline_missed: int
    total_execution_time: float
    average_wait_time: float
    throughput: float


class TaskScheduler:
    """
    A priority-based task scheduler using a priority queue.
    
    This scheduler implements a priority-based scheduling algorithm where
    tasks with higher priority are executed first. The scheduler maintains
    a priority queue and executes tasks in priority order.
    
    Time Complexity Analysis:
        - schedule_tasks(): O(n log n) where n is the number of tasks
          - Inserting n tasks: O(n log n)
          - Extracting n tasks: O(n log n)
        - Space Complexity: O(n) for the priority queue
    
    Examples:
        >>> scheduler = TaskScheduler()
        >>> tasks = [
        ...     Task("T1", priority=10, arrival_time=0.0, deadline=100.0, execution_time=5.0),
        ...     Task("T2", priority=20, arrival_time=0.0, deadline=50.0, execution_time=3.0)
        ... ]
        >>> results = scheduler.schedule_tasks(tasks)
        >>> print(f"Scheduled {len(results)} tasks")
        Scheduled 2 tasks
    """
    
    def __init__(self):
        """Initialize an empty task scheduler."""
        self.priority_queue = PriorityQueue(is_max_heap=True)
        self.current_time = 0.0
    
    def schedule_tasks(self, tasks: List[Task]) -> List[SchedulingResult]:
        """
        Schedule and execute a list of tasks based on priority.
        
        This method implements a priority-based scheduling algorithm:
        1. All tasks are inserted into the priority queue
        2. Tasks are extracted and executed in priority order
        3. Execution times and deadlines are tracked
        
        Time Complexity: O(n log n) where n is the number of tasks
        - Inserting n tasks: O(n log n)
        - Extracting n tasks: O(n log n)
        
        Args:
            tasks: List of tasks to schedule
        
        Returns:
            List[SchedulingResult]: Results of scheduling each task
        
        Examples:
            >>> scheduler = TaskScheduler()
            >>> tasks = [
            ...     Task("T1", priority=10, arrival_time=0.0, execution_time=5.0),
            ...     Task("T2", priority=20, arrival_time=0.0, execution_time=3.0)
            ... ]
            >>> results = scheduler.schedule_tasks(tasks)
            >>> results[0].task_id
            'T2'
        """
        # Reset scheduler state
        self.priority_queue = PriorityQueue(is_max_heap=True)
        self.current_time = 0.0
        results: List[SchedulingResult] = []
        
        # Insert all tasks into priority queue
        # Time Complexity: O(n log n) for n insertions
        for task in tasks:
            self.priority_queue.insert(task)
        
        # Execute tasks in priority order
        # Time Complexity: O(n log n) for n extractions
        while not self.priority_queue.is_empty():
            task = self.priority_queue.extract_max()
            
            # Calculate scheduling metrics
            start_time = self.current_time
            wait_time = start_time - task.arrival_time
            completion_time = start_time + task.execution_time
            
            # Check if deadline is met
            deadline_met = True
            if task.deadline is not None:
                deadline_met = completion_time <= task.deadline
            
            # Create result
            result = SchedulingResult(
                task_id=task.task_id,
                start_time=start_time,
                completion_time=completion_time,
                deadline_met=deadline_met,
                wait_time=wait_time
            )
            results.append(result)
            
            # Update current time
            self.current_time = completion_time
        
        return results
    
    def get_statistics(self, results: List[SchedulingResult]) -> SchedulingStatistics:
        """
        Calculate scheduling statistics from results.
        
        Time Complexity: O(n) where n is the number of results
        
        Args:
            results: List of scheduling results
        
        Returns:
            SchedulingStatistics: Calculated statistics
        """
        if not results:
            return SchedulingStatistics(
                total_tasks=0,
                completed_tasks=0,
                deadline_met=0,
                deadline_missed=0,
                total_execution_time=0.0,
                average_wait_time=0.0,
                throughput=0.0
            )
        
        total_tasks = len(results)
        completed_tasks = len(results)
        deadline_met = sum(1 for r in results if r.deadline_met)
        deadline_missed = total_tasks - deadline_met
        
        total_execution_time = max(r.completion_time for r in results) if results else 0.0
        average_wait_time = sum(r.wait_time for r in results) / total_tasks if total_tasks > 0 else 0.0
        throughput = completed_tasks / total_execution_time if total_execution_time > 0 else 0.0
        
        return SchedulingStatistics(
            total_tasks=total_tasks,
            completed_tasks=completed_tasks,
            deadline_met=deadline_met,
            deadline_missed=deadline_missed,
            total_execution_time=total_execution_time,
            average_wait_time=average_wait_time,
            throughput=throughput
        )
    
    def print_schedule(self, results: List[SchedulingResult]) -> None:
        """
        Print a formatted schedule of task execution.
        
        Args:
            results: List of scheduling results to display
        """
        print("\n" + "=" * 80)
        print("TASK SCHEDULING RESULTS")
        print("=" * 80)
        print(f"{'Task ID':<10} {'Start':<12} {'Completion':<12} {'Wait':<12} {'Deadline':<10}")
        print("-" * 80)
        
        for result in results:
            deadline_status = "✓ Met" if result.deadline_met else "✗ Missed"
            print(f"{result.task_id:<10} {result.start_time:<12.2f} "
                  f"{result.completion_time:<12.2f} {result.wait_time:<12.2f} {deadline_status:<10}")
        
        print("-" * 80)
        
        # Print statistics
        stats = self.get_statistics(results)
        print(f"\nStatistics:")
        print(f"  Total tasks: {stats.total_tasks}")
        print(f"  Completed: {stats.completed_tasks}")
        print(f"  Deadline met: {stats.deadline_met}")
        print(f"  Deadline missed: {stats.deadline_missed}")
        print(f"  Total execution time: {stats.total_execution_time:.2f}")
        print(f"  Average wait time: {stats.average_wait_time:.2f}")
        print(f"  Throughput: {stats.throughput:.2f} tasks/time unit")
        print("=" * 80)


def simulate_scheduler(tasks: List[Task], verbose: bool = True) -> SchedulingStatistics:
    """
    Simulate a task scheduler with the given tasks.
    
    This is a convenience function that creates a scheduler, schedules tasks,
    and returns statistics.
    
    Time Complexity: O(n log n) where n is the number of tasks
    
    Args:
        tasks: List of tasks to schedule
        verbose: If True, print the schedule
    
    Returns:
        SchedulingStatistics: Statistics from the simulation
    
    Examples:
        >>> tasks = [
        ...     Task("T1", priority=10, arrival_time=0.0, deadline=100.0, execution_time=5.0),
        ...     Task("T2", priority=20, arrival_time=0.0, deadline=50.0, execution_time=3.0)
        ... ]
        >>> stats = simulate_scheduler(tasks, verbose=False)
        >>> stats.total_tasks
        2
    """
    scheduler = TaskScheduler()
    results = scheduler.schedule_tasks(tasks)
    
    if verbose:
        scheduler.print_schedule(results)
    
    return scheduler.get_statistics(results)

