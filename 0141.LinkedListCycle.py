class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        时间复杂度: O(n)，n 为链表长度。
        空间复杂度: O(1)。
        Definition for singly-linked list.
        class ListNode:
        def __init__(self, x):
        self.val = x
        self.next = None
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        # visited = set()
        # curr = head

        # while curr:
        #     if curr in visited:
        #         return True
            
        #     visited.add(curr)
        #     curr = curr.next

        # return False