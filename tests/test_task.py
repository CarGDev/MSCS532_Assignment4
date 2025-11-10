"""
Test Suite for Task Class

This module contains tests for the Task class, including comparisons,
priority updates, and deadline checking.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import unittest
import sys
import os

# Add parent directory to path to import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task import Task


class TestTask(unittest.TestCase):
    """Test cases for Task class."""
    
    def test_task_creation(self):
        """Test creating a task with all parameters."""
        task = Task(
            task_id="T1",
            priority=10,
            arrival_time=0.0,
            deadline=100.0,
            execution_time=5.0,
            description="Test task"
        )
        self.assertEqual(task.task_id, "T1")
        self.assertEqual(task.priority, 10)
        self.assertEqual(task.arrival_time, 0.0)
        self.assertEqual(task.deadline, 100.0)
        self.assertEqual(task.execution_time, 5.0)
        self.assertEqual(task.description, "Test task")
    
    def test_task_creation_minimal(self):
        """Test creating a task with minimal parameters."""
        task = Task("T1", priority=10, arrival_time=0.0)
        self.assertEqual(task.task_id, "T1")
        self.assertEqual(task.priority, 10)
        self.assertEqual(task.arrival_time, 0.0)
        self.assertIsNone(task.deadline)
        self.assertEqual(task.execution_time, 1.0)
        self.assertEqual(task.description, "")
    
    def test_task_comparison_lt(self):
        """Test less than comparison."""
        task1 = Task("T1", priority=5, arrival_time=0.0)
        task2 = Task("T2", priority=10, arrival_time=1.0)
        self.assertTrue(task1 < task2)
        self.assertFalse(task2 < task1)
    
    def test_task_comparison_gt(self):
        """Test greater than comparison."""
        task1 = Task("T1", priority=10, arrival_time=0.0)
        task2 = Task("T2", priority=5, arrival_time=1.0)
        self.assertTrue(task1 > task2)
        self.assertFalse(task2 > task1)
    
    def test_task_comparison_eq(self):
        """Test equality comparison."""
        task1 = Task("T1", priority=10, arrival_time=0.0)
        task2 = Task("T2", priority=10, arrival_time=1.0)
        task3 = Task("T3", priority=5, arrival_time=2.0)
        self.assertTrue(task1 == task2)
        self.assertFalse(task1 == task3)
    
    def test_task_comparison_le(self):
        """Test less than or equal comparison."""
        task1 = Task("T1", priority=5, arrival_time=0.0)
        task2 = Task("T2", priority=10, arrival_time=1.0)
        task3 = Task("T3", priority=5, arrival_time=2.0)
        self.assertTrue(task1 <= task2)
        self.assertTrue(task1 <= task3)
        self.assertFalse(task2 <= task1)
    
    def test_task_comparison_ge(self):
        """Test greater than or equal comparison."""
        task1 = Task("T1", priority=10, arrival_time=0.0)
        task2 = Task("T2", priority=5, arrival_time=1.0)
        task3 = Task("T3", priority=10, arrival_time=2.0)
        self.assertTrue(task1 >= task2)
        self.assertTrue(task1 >= task3)
        self.assertFalse(task2 >= task1)
    
    def test_update_priority(self):
        """Test updating task priority."""
        task = Task("T1", priority=10, arrival_time=0.0)
        self.assertEqual(task.priority, 10)
        task.update_priority(20)
        self.assertEqual(task.priority, 20)
    
    def test_is_overdue_with_deadline(self):
        """Test checking if task is overdue."""
        task = Task("T1", priority=10, arrival_time=0.0, deadline=100.0)
        self.assertFalse(task.is_overdue(50.0))
        self.assertFalse(task.is_overdue(100.0))
        self.assertTrue(task.is_overdue(150.0))
    
    def test_is_overdue_no_deadline(self):
        """Test checking overdue status for task without deadline."""
        task = Task("T1", priority=10, arrival_time=0.0)
        self.assertFalse(task.is_overdue(1000.0))
    
    def test_time_until_deadline(self):
        """Test calculating time until deadline."""
        task = Task("T1", priority=10, arrival_time=0.0, deadline=100.0)
        self.assertEqual(task.time_until_deadline(50.0), 50.0)
        self.assertEqual(task.time_until_deadline(100.0), 0.0)
        self.assertEqual(task.time_until_deadline(150.0), 0.0)
    
    def test_time_until_deadline_no_deadline(self):
        """Test time until deadline for task without deadline."""
        task = Task("T1", priority=10, arrival_time=0.0)
        self.assertIsNone(task.time_until_deadline(100.0))


if __name__ == '__main__':
    unittest.main()

