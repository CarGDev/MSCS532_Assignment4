"""
Priority Queue Implementation

This module implements a Priority Queue data structure using a binary heap.
The implementation supports both max-heap (highest priority first) and
min-heap (lowest priority first) configurations.

The priority queue is implemented using a Python list to represent the binary heap,
which provides efficient access to parent and child nodes through index calculations.

Author: Carlos Gutierrez
Email: cgutierrez44833@ucumberlands.edu
"""

from typing import List, Optional, TypeVar, Callable
from .task import Task

T = TypeVar('T')


class PriorityQueue:
    """
    A Priority Queue implementation using a binary heap.
    
    This class supports both max-heap and min-heap configurations. By default,
    it uses a max-heap where higher priority values are extracted first.
    
    The heap is implemented using a list, where for a node at index i:
    - Parent is at index (i-1)//2
    - Left child is at index 2*i+1
    - Right child is at index 2*i+2
    
    Attributes:
        heap (List[T]): The list representing the binary heap
        is_max_heap (bool): True for max-heap, False for min-heap
        key (Callable): Function to extract priority/comparison key
    
    Time Complexity Analysis:
        - insert(): O(log n) - bubble up operation
        - extract_max()/extract_min(): O(log n) - heapify operation
        - increase_key()/decrease_key(): O(log n) - bubble up/down
        - is_empty(): O(1) - constant time check
        - peek(): O(1) - constant time access to root
    
    Space Complexity: O(n) where n is the number of elements
    
    Examples:
        >>> pq = PriorityQueue()
        >>> pq.insert(Task("T1", priority=10, arrival_time=0.0))
        >>> pq.insert(Task("T2", priority=5, arrival_time=1.0))
        >>> pq.insert(Task("T3", priority=15, arrival_time=2.0))
        >>> task = pq.extract_max()
        >>> task.task_id
        'T3'
    """
    
    def __init__(self, is_max_heap: bool = True, key: Optional[Callable[[T], int]] = None):
        """
        Initialize an empty priority queue.
        
        Args:
            is_max_heap: If True, use max-heap (higher priority first).
                        If False, use min-heap (lower priority first).
            key: Optional function to extract priority from elements.
                 If None, elements are compared directly.
        
        Examples:
            >>> pq = PriorityQueue(is_max_heap=True)
            >>> pq.is_empty()
            True
        """
        self.heap: List[T] = []
        self.is_max_heap = is_max_heap
        self.key = key if key is not None else (lambda x: x.priority if isinstance(x, Task) else x)
    
    def _compare(self, a: T, b: T) -> bool:
        """
        Compare two elements based on heap type.
        
        Args:
            a: First element
            b: Second element
        
        Returns:
            bool: True if a should be above b in the heap
        """
        val_a = self.key(a)
        val_b = self.key(b)
        if self.is_max_heap:
            return val_a > val_b
        else:
            return val_a < val_b
    
    def _heapify_up(self, index: int) -> None:
        """
        Maintain heap property by bubbling up an element.
        
        Time Complexity: O(log n)
        
        Args:
            index: Index of the element to bubble up
        """
        while index > 0:
            parent = (index - 1) // 2
            if self._compare(self.heap[index], self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    
    def _heapify_down(self, index: int) -> None:
        """
        Maintain heap property by bubbling down an element.
        
        Time Complexity: O(log n)
        
        Args:
            index: Index of the element to bubble down
        """
        n = len(self.heap)
        while True:
            largest_or_smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            # Compare with left child
            if left < n and self._compare(self.heap[left], self.heap[largest_or_smallest]):
                largest_or_smallest = left
            
            # Compare with right child
            if right < n and self._compare(self.heap[right], self.heap[largest_or_smallest]):
                largest_or_smallest = right
            
            # If element is in correct position, stop
            if largest_or_smallest == index:
                break
            
            # Swap and continue
            self.heap[index], self.heap[largest_or_smallest] = \
                self.heap[largest_or_smallest], self.heap[index]
            index = largest_or_smallest
    
    def insert(self, item: T) -> None:
        """
        Insert an item into the priority queue.
        
        The item is added to the end of the heap and then bubbled up
        to maintain the heap property.
        
        Time Complexity: O(log n) where n is the number of elements
        
        Args:
            item: The item to insert
        
        Examples:
            >>> pq = PriorityQueue()
            >>> pq.insert(Task("T1", priority=10, arrival_time=0.0))
            >>> pq.size()
            1
        """
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self) -> T:
        """
        Extract and return the item with the highest priority (max-heap).
        
        This operation removes the root of the heap, replaces it with the
        last element, and maintains the heap property.
        
        Time Complexity: O(log n)
        
        Returns:
            T: The item with the highest priority
        
        Raises:
            IndexError: If the priority queue is empty
        
        Examples:
            >>> pq = PriorityQueue()
            >>> pq.insert(Task("T1", priority=10, arrival_time=0.0))
            >>> pq.insert(Task("T2", priority=5, arrival_time=1.0))
            >>> task = pq.extract_max()
            >>> task.priority
            10
        """
        if self.is_empty():
            raise IndexError("Cannot extract from empty priority queue")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return root
    
    def extract_min(self) -> T:
        """
        Extract and return the item with the lowest priority (min-heap).
        
        This operation removes the root of the heap, replaces it with the
        last element, and maintains the heap property.
        
        Time Complexity: O(log n)
        
        Returns:
            T: The item with the lowest priority
        
        Raises:
            IndexError: If the priority queue is empty
        
        Examples:
            >>> pq = PriorityQueue(is_max_heap=False)
            >>> pq.insert(Task("T1", priority=10, arrival_time=0.0))
            >>> pq.insert(Task("T2", priority=5, arrival_time=1.0))
            >>> task = pq.extract_min()
            >>> task.priority
            5
        """
        if self.is_empty():
            raise IndexError("Cannot extract from empty priority queue")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return root
    
    def increase_key(self, item: T, new_priority: int) -> bool:
        """
        Increase the priority of an existing item in the priority queue.
        
        This operation finds the item, updates its priority, and bubbles it up
        if necessary to maintain the heap property.
        
        Time Complexity: O(n) to find the item + O(log n) to bubble up = O(n)
        Note: This could be optimized to O(log n) with a hash map for O(1) lookup
        
        Args:
            item: The item whose priority should be increased
            new_priority: The new priority value
        
        Returns:
            bool: True if the item was found and updated, False otherwise
        
        Examples:
            >>> pq = PriorityQueue()
            >>> task = Task("T1", priority=10, arrival_time=0.0)
            >>> pq.insert(task)
            >>> pq.increase_key(task, 20)
            True
            >>> task.priority
            20
        """
        # Find the item in the heap
        try:
            index = self.heap.index(item)
        except ValueError:
            return False
        
        # Update priority
        if isinstance(item, Task):
            item.update_priority(new_priority)
        
        # Bubble up if necessary
        self._heapify_up(index)
        return True
    
    def decrease_key(self, item: T, new_priority: int) -> bool:
        """
        Decrease the priority of an existing item in the priority queue.
        
        This operation finds the item, updates its priority, and bubbles it down
        if necessary to maintain the heap property.
        
        Time Complexity: O(n) to find the item + O(log n) to bubble down = O(n)
        Note: This could be optimized to O(log n) with a hash map for O(1) lookup
        
        Args:
            item: The item whose priority should be decreased
            new_priority: The new priority value
        
        Returns:
            bool: True if the item was found and updated, False otherwise
        
        Examples:
            >>> pq = PriorityQueue()
            >>> task = Task("T1", priority=20, arrival_time=0.0)
            >>> pq.insert(task)
            >>> pq.decrease_key(task, 10)
            True
            >>> task.priority
            10
        """
        # Find the item in the heap
        try:
            index = self.heap.index(item)
        except ValueError:
            return False
        
        # Update priority
        if isinstance(item, Task):
            item.update_priority(new_priority)
        
        # Bubble down if necessary
        self._heapify_down(index)
        return True
    
    def is_empty(self) -> bool:
        """
        Check if the priority queue is empty.
        
        Time Complexity: O(1)
        
        Returns:
            bool: True if the priority queue is empty, False otherwise
        
        Examples:
            >>> pq = PriorityQueue()
            >>> pq.is_empty()
            True
            >>> pq.insert(Task("T1", priority=10, arrival_time=0.0))
            >>> pq.is_empty()
            False
        """
        return len(self.heap) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the priority queue.
        
        Time Complexity: O(1)
        
        Returns:
            int: The number of items in the priority queue
        
        Examples:
            >>> pq = PriorityQueue()
            >>> pq.size()
            0
            >>> pq.insert(Task("T1", priority=10, arrival_time=0.0))
            >>> pq.size()
            1
        """
        return len(self.heap)
    
    def peek(self) -> Optional[T]:
        """
        Get the highest (or lowest) priority item without removing it.
        
        Time Complexity: O(1)
        
        Returns:
            Optional[T]: The root item, or None if the queue is empty
        
        Examples:
            >>> pq = PriorityQueue()
            >>> pq.insert(Task("T1", priority=10, arrival_time=0.0))
            >>> task = pq.peek()
            >>> task.task_id
            'T1'
        """
        if self.is_empty():
            return None
        return self.heap[0]
    
    def __str__(self) -> str:
        """String representation of the priority queue."""
        return f"PriorityQueue(size={self.size()}, is_max_heap={self.is_max_heap})"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return self.__str__()

