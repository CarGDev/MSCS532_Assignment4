"""
Test Suite for Priority Queue Implementation

This module contains comprehensive tests for the Priority Queue data structure,
including all core operations and edge cases.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import unittest
import sys
import os

# Add parent directory to path to import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.priority_queue import PriorityQueue
from src.task import Task


class TestPriorityQueue(unittest.TestCase):
    """Test cases for Priority Queue implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.pq = PriorityQueue(is_max_heap=True)
    
    def test_initialization(self):
        """Test priority queue initialization."""
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
        self.assertEqual(pq.size(), 0)
        self.assertTrue(pq.is_max_heap)
    
    def test_initialization_min_heap(self):
        """Test min-heap initialization."""
        pq = PriorityQueue(is_max_heap=False)
        self.assertTrue(pq.is_empty())
        self.assertFalse(pq.is_max_heap)
    
    def test_insert_single_task(self):
        """Test inserting a single task."""
        task = Task("T1", priority=10, arrival_time=0.0)
        self.pq.insert(task)
        self.assertFalse(self.pq.is_empty())
        self.assertEqual(self.pq.size(), 1)
    
    def test_insert_multiple_tasks(self):
        """Test inserting multiple tasks."""
        tasks = [
            Task("T1", priority=10, arrival_time=0.0),
            Task("T2", priority=5, arrival_time=1.0),
            Task("T3", priority=15, arrival_time=2.0)
        ]
        for task in tasks:
            self.pq.insert(task)
        self.assertEqual(self.pq.size(), 3)
    
    def test_extract_max_ordering(self):
        """Test that extract_max returns tasks in priority order."""
        tasks = [
            Task("T1", priority=10, arrival_time=0.0),
            Task("T2", priority=5, arrival_time=1.0),
            Task("T3", priority=15, arrival_time=2.0),
            Task("T4", priority=20, arrival_time=3.0)
        ]
        for task in tasks:
            self.pq.insert(task)
        
        # Should extract in descending priority order
        self.assertEqual(self.pq.extract_max().priority, 20)
        self.assertEqual(self.pq.extract_max().priority, 15)
        self.assertEqual(self.pq.extract_max().priority, 10)
        self.assertEqual(self.pq.extract_max().priority, 5)
        self.assertTrue(self.pq.is_empty())
    
    def test_extract_max_empty(self):
        """Test extracting from empty queue raises error."""
        with self.assertRaises(IndexError):
            self.pq.extract_max()
    
    def test_extract_min_ordering(self):
        """Test that extract_min returns tasks in ascending priority order."""
        pq = PriorityQueue(is_max_heap=False)
        tasks = [
            Task("T1", priority=10, arrival_time=0.0),
            Task("T2", priority=5, arrival_time=1.0),
            Task("T3", priority=15, arrival_time=2.0),
            Task("T4", priority=20, arrival_time=3.0)
        ]
        for task in tasks:
            pq.insert(task)
        
        # Should extract in ascending priority order
        self.assertEqual(pq.extract_min().priority, 5)
        self.assertEqual(pq.extract_min().priority, 10)
        self.assertEqual(pq.extract_min().priority, 15)
        self.assertEqual(pq.extract_min().priority, 20)
        self.assertTrue(pq.is_empty())
    
    def test_peek(self):
        """Test peeking at the highest priority task."""
        tasks = [
            Task("T1", priority=10, arrival_time=0.0),
            Task("T2", priority=5, arrival_time=1.0),
            Task("T3", priority=15, arrival_time=2.0)
        ]
        for task in tasks:
            self.pq.insert(task)
        
        peeked = self.pq.peek()
        self.assertEqual(peeked.priority, 15)
        # Peek should not remove the element
        self.assertEqual(self.pq.size(), 3)
    
    def test_peek_empty(self):
        """Test peeking at empty queue returns None."""
        self.assertIsNone(self.pq.peek())
    
    def test_increase_key(self):
        """Test increasing the priority of a task."""
        task = Task("T1", priority=10, arrival_time=0.0)
        self.pq.insert(task)
        self.pq.insert(Task("T2", priority=20, arrival_time=1.0))
        
        # Initially, T2 should be at root
        self.assertEqual(self.pq.peek().priority, 20)
        
        # Increase T1's priority
        success = self.pq.increase_key(task, 25)
        self.assertTrue(success)
        self.assertEqual(task.priority, 25)
        
        # Now T1 should be at root
        self.assertEqual(self.pq.peek().priority, 25)
        self.assertEqual(self.pq.peek().task_id, "T1")
    
    def test_increase_key_not_found(self):
        """Test increasing key of non-existent task."""
        task = Task("T1", priority=10, arrival_time=0.0)
        success = self.pq.increase_key(task, 20)
        self.assertFalse(success)
    
    def test_decrease_key(self):
        """Test decreasing the priority of a task."""
        task = Task("T1", priority=20, arrival_time=0.0)
        self.pq.insert(task)
        self.pq.insert(Task("T2", priority=10, arrival_time=1.0))
        
        # Initially, T1 should be at root
        self.assertEqual(self.pq.peek().priority, 20)
        
        # Decrease T1's priority
        success = self.pq.decrease_key(task, 5)
        self.assertTrue(success)
        self.assertEqual(task.priority, 5)
        
        # Now T2 should be at root
        self.assertEqual(self.pq.peek().priority, 10)
        self.assertEqual(self.pq.peek().task_id, "T2")
    
    def test_decrease_key_not_found(self):
        """Test decreasing key of non-existent task."""
        task = Task("T1", priority=10, arrival_time=0.0)
        success = self.pq.decrease_key(task, 5)
        self.assertFalse(success)
    
    def test_is_empty(self):
        """Test is_empty method."""
        self.assertTrue(self.pq.is_empty())
        self.pq.insert(Task("T1", priority=10, arrival_time=0.0))
        self.assertFalse(self.pq.is_empty())
        self.pq.extract_max()
        self.assertTrue(self.pq.is_empty())
    
    def test_size(self):
        """Test size method."""
        self.assertEqual(self.pq.size(), 0)
        for i in range(5):
            self.pq.insert(Task(f"T{i}", priority=i, arrival_time=float(i)))
            self.assertEqual(self.pq.size(), i + 1)
        
        for i in range(5):
            self.pq.extract_max()
            self.assertEqual(self.pq.size(), 4 - i)
    
    def test_large_queue(self):
        """Test priority queue with many elements."""
        for i in range(1000):
            self.pq.insert(Task(f"T{i}", priority=i, arrival_time=float(i)))
        
        self.assertEqual(self.pq.size(), 1000)
        
        # Extract all and verify ordering
        prev_priority = float('inf')
        while not self.pq.is_empty():
            task = self.pq.extract_max()
            self.assertLessEqual(task.priority, prev_priority)
            prev_priority = task.priority
    
    def test_duplicate_priorities(self):
        """Test handling of tasks with duplicate priorities."""
        tasks = [
            Task("T1", priority=10, arrival_time=0.0),
            Task("T2", priority=10, arrival_time=1.0),
            Task("T3", priority=10, arrival_time=2.0)
        ]
        for task in tasks:
            self.pq.insert(task)
        
        # All should be extractable
        extracted = []
        while not self.pq.is_empty():
            extracted.append(self.pq.extract_max())
        
        self.assertEqual(len(extracted), 3)
        self.assertTrue(all(task.priority == 10 for task in extracted))


if __name__ == '__main__':
    unittest.main()

