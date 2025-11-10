"""
Task Module

This module defines the Task class used to represent individual tasks
in the priority queue implementation. Each task contains information
such as task ID, priority, arrival time, and deadline.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a task with priority, timing, and identification information.
    
    Attributes:
        task_id (str): Unique identifier for the task
        priority (int): Priority level (higher values = higher priority)
        arrival_time (float): Time when the task arrives in the system
        deadline (Optional[float]): Deadline for task completion (None if no deadline)
        execution_time (float): Estimated time required to execute the task
        description (str): Optional description of the task
    
    Examples:
        >>> task = Task("T1", priority=10, arrival_time=0.0, deadline=100.0)
        >>> print(task)
        Task(task_id='T1', priority=10, arrival_time=0.0, deadline=100.0, execution_time=1.0, description='')
    """
    
    task_id: str
    priority: int
    arrival_time: float
    deadline: Optional[float] = None
    execution_time: float = 1.0
    description: str = ""
    
    def __lt__(self, other: 'Task') -> bool:
        """
        Compare tasks by priority (for min-heap: lower priority first).
        
        Args:
            other: Another Task object to compare with
            
        Returns:
            bool: True if this task has lower priority than other
        """
        return self.priority < other.priority
    
    def __gt__(self, other: 'Task') -> bool:
        """
        Compare tasks by priority (for max-heap: higher priority first).
        
        Args:
            other: Another Task object to compare with
            
        Returns:
            bool: True if this task has higher priority than other
        """
        return self.priority > other.priority
    
    def __eq__(self, other: 'Task') -> bool:
        """
        Check if two tasks have the same priority.
        
        Args:
            other: Another Task object to compare with
            
        Returns:
            bool: True if tasks have the same priority
        """
        if not isinstance(other, Task):
            return False
        return self.priority == other.priority
    
    def __le__(self, other: 'Task') -> bool:
        """Less than or equal comparison."""
        return self.priority <= other.priority
    
    def __ge__(self, other: 'Task') -> bool:
        """Greater than or equal comparison."""
        return self.priority >= other.priority
    
    def update_priority(self, new_priority: int) -> None:
        """
        Update the priority of the task.
        
        Args:
            new_priority: The new priority value
        """
        self.priority = new_priority
    
    def is_overdue(self, current_time: float) -> bool:
        """
        Check if the task has passed its deadline.
        
        Args:
            current_time: The current time in the system
            
        Returns:
            bool: True if deadline exists and has passed
        """
        if self.deadline is None:
            return False
        return current_time > self.deadline
    
    def time_until_deadline(self, current_time: float) -> Optional[float]:
        """
        Calculate the time remaining until the deadline.
        
        Args:
            current_time: The current time in the system
            
        Returns:
            Optional[float]: Time remaining until deadline, or None if no deadline
        """
        if self.deadline is None:
            return None
        return max(0.0, self.deadline - current_time)

