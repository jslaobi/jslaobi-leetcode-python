from collections import deque, Counter

class FirstUnique:
    def __init__(self, nums: list[int]):
        self.counts = Counter(nums)
        self.queue = deque(nums)
    
    def showFirstUnique(self) -> int:
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.popleft()
        
        if self.queue:
            return self.queue[0]
        
        return -1
    
    def add(self, value: int) -> None:
        self.counts[value] += 1
        self.queue.append(value)


# class Node:
#     # A standard Doubly Linked List Node
#     def __init__(self, val=0):
#         self.val = val
#         self.prev = None
#         self.next = None

# class FirstUnique:

#     def __init__(self, nums: list[int]):
#         # 1. Initialize the DLL with Dummy Head and Tail
#         self.head = Node()
#         self.tail = Node()
#         self.head.next = self.tail
#         self.tail.prev = self.head
        
#         # 2. Initialize the HashMap
#         # Maps integer -> Node (if unique) OR False (if duplicate)
#         self.nodes = {} 
        
#         # 3. Process the initial numbers
#         for num in nums:
#             self.add(num)

#     # Helper function to remove a node from the DLL in O(1) time
#     def _remove(self, node: Node) -> None:
#         prev_node = node.prev
#         next_node = node.next
#         prev_node.next = next_node
#         next_node.prev = prev_node

#     # Helper function to append a node to the end of the DLL in O(1) time
#     def _append(self, node: Node) -> None:
#         prev_node = self.tail.prev
#         prev_node.next = node
#         node.prev = prev_node
#         node.next = self.tail
#         self.tail.prev = node

#     def showFirstUnique(self) -> int:
#         # If there is a node between head and tail, return the first one
#         if self.head.next != self.tail:
#             return self.head.next.val
        
#         # The DLL is empty (no unique numbers)
#         return -1

#     def add(self, value: int) -> None:
#         if value not in self.nodes:
#             # Case 1: First time seeing this number.
#             # Create a node, add it to the DLL, and save the reference in the map.
#             new_node = Node(value)
#             self._append(new_node)
#             self.nodes[value] = new_node
            
#         elif self.nodes[value]:
#             # Case 2: Second time seeing this number.
#             # It's currently in the DLL. We must remove it and mark it as False.
#             self._remove(self.nodes[value])
#             self.nodes[value] = False
            
#         # Case 3: We have seen this number 3 or more times.
#         # self.nodes[value] is False. We do nothing at all!