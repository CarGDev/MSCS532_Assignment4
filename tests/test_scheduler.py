"""
Test Suite for Task Scheduler Implementation

This module contains comprehensive tests for the task scheduler,
including scheduling algorithms, statistics, and edge cases.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

import unittest
import sys
import os

# Add parent directory to path to import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scheduler import TaskScheduler, SchedulingResult, SchedulingStatistics, simulate_scheduler
from src.task import Task


class TestTaskScheduler(unittest.TestCase):
    """Test cases for TaskScheduler class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.scheduler = TaskScheduler()
    
    def test_basic_scheduling(self):
        """Test basic priority-based scheduling."""
        tasks = [
            Task("T1", priority=10, arrival_time=0.0, execution_time=5.0),
            Task("T2", priority=20, arrival_time=0.0, execution_time=3.0),
            Task("T3", priority=15, arrival_time=0.0, execution_time=4.0),
        ]
        
        results = self.scheduler.schedule_tasks(tasks)
        
        self.assertEqual(len(results), 3)
        # Highest priority should execute first
        self.assertEqual(results[0].task_id, "T2")
        self.assertEqual(results[1].task_id, "T3")
        self.assertEqual(results[2].task_id, "T1")
    
    def test_scheduling_order(self):
        """Test that tasks are scheduled in priority order."""
        tasks = [
            Task("T1", priority=5, arrival_time=0.0, execution_time=1.0),
            Task("T2", priority=10, arrival_time=0.0, execution_time=1.0),
            Task("T3", priority=15, arrival_time=0.0, execution_time=1.0),
        ]
        
        results = self.scheduler.schedule_tasks(tasks)
        
        # Should be in descending priority order
        priorities = [t.priority for t in tasks]
        priorities.sort(reverse=True)
        
        for i, result in enumerate(results):
            # Find the task that matches this result
            task = next(t for t in tasks if t.task_id == result.task_id)
            self.assertEqual(task.priority, priorities[i])
    
    def test_deadline_tracking(self):
        """Test that deadlines are correctly tracked."""
        tasks = [
            Task("T1", priority=20, arrival_time=0.0, deadline=10.0, execution_time=5.0),
            Task("T2", priority=10, arrival_time=0.0, deadline=100.0, execution_time=20.0),
        ]
        
        results = self.scheduler.schedule_tasks(tasks)
        
        # T1 should meet deadline (starts at 0, completes at 5, deadline 10)
        self.assertTrue(results[0].deadline_met)
        
        # T2 should also meet deadline (starts at 5, completes at 25, deadline 100)
        self.assertTrue(results[1].deadline_met)
    
    def test_deadline_missed(self):
        """Test detection of missed deadlines."""
        tasks = [
            Task("T1", priority=20, arrival_time=0.0, deadline=3.0, execution_time=5.0),
        ]
        
        results = self.scheduler.schedule_tasks(tasks)
        
        # Task should miss deadline (completes at 5, deadline is 3)
        self.assertFalse(results[0].deadline_met)
    
    def test_wait_time_calculation(self):
        """Test wait time calculation."""
        tasks = [
            Task("T1", priority=20, arrival_time=0.0, execution_time=5.0),
            Task("T2", priority=10, arrival_time=0.0, execution_time=3.0),
        ]
        
        results = self.scheduler.schedule_tasks(tasks)
        
        # T1 should have no wait time (executes first)
        self.assertEqual(results[0].wait_time, 0.0)
        
        # T2 should wait for T1 to complete
        self.assertEqual(results[1].wait_time, 5.0)
    
    def test_empty_task_list(self):
        """Test scheduling with empty task list."""
        results = self.scheduler.schedule_tasks([])
        self.assertEqual(len(results), 0)
    
    def test_single_task(self):
        """Test scheduling a single task."""
        tasks = [Task("T1", priority=10, arrival_time=0.0, execution_time=5.0)]
        results = self.scheduler.schedule_tasks(tasks)
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].task_id, "T1")
        self.assertEqual(results[0].start_time, 0.0)
        self.assertEqual(results[0].completion_time, 5.0)
        self.assertEqual(results[0].wait_time, 0.0)


class TestSchedulingStatistics(unittest.TestCase):
    """Test cases for scheduling statistics."""
    
    def test_statistics_calculation(self):
        """Test statistics calculation."""
        scheduler = TaskScheduler()
        
        tasks = [
            Task("T1", priority=20, arrival_time=0.0, deadline=10.0, execution_time=5.0),
            Task("T2", priority=10, arrival_time=0.0, deadline=100.0, execution_time=3.0),
        ]
        
        results = scheduler.schedule_tasks(tasks)
        stats = scheduler.get_statistics(results)
        
        self.assertEqual(stats.total_tasks, 2)
        self.assertEqual(stats.completed_tasks, 2)
        self.assertEqual(stats.deadline_met, 2)
        self.assertEqual(stats.deadline_missed, 0)
        self.assertEqual(stats.total_execution_time, 8.0)  # 5 + 3
        self.assertGreater(stats.average_wait_time, 0)
        self.assertGreater(stats.throughput, 0)
    
    def test_statistics_with_missed_deadlines(self):
        """Test statistics with missed deadlines."""
        scheduler = TaskScheduler()
        
        tasks = [
            Task("T1", priority=20, arrival_time=0.0, deadline=3.0, execution_time=5.0),
            Task("T2", priority=10, arrival_time=0.0, deadline=100.0, execution_time=3.0),
        ]
        
        results = scheduler.schedule_tasks(tasks)
        stats = scheduler.get_statistics(results)
        
        self.assertEqual(stats.deadline_met, 1)
        self.assertEqual(stats.deadline_missed, 1)
    
    def test_statistics_empty_results(self):
        """Test statistics with empty results."""
        scheduler = TaskScheduler()
        stats = scheduler.get_statistics([])
        
        self.assertEqual(stats.total_tasks, 0)
        self.assertEqual(stats.completed_tasks, 0)
        self.assertEqual(stats.total_execution_time, 0.0)
        self.assertEqual(stats.average_wait_time, 0.0)
        self.assertEqual(stats.throughput, 0.0)


class TestSimulateScheduler(unittest.TestCase):
    """Test cases for simulate_scheduler convenience function."""
    
    def test_simulate_scheduler(self):
        """Test the simulate_scheduler function."""
        tasks = [
            Task("T1", priority=20, arrival_time=0.0, execution_time=5.0),
            Task("T2", priority=10, arrival_time=0.0, execution_time=3.0),
        ]
        
        stats = simulate_scheduler(tasks, verbose=False)
        
        self.assertEqual(stats.total_tasks, 2)
        self.assertEqual(stats.completed_tasks, 2)


if __name__ == '__main__':
    unittest.main()

