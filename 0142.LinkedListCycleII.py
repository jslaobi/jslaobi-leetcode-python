class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
                
        return None

        # visited = set()
        # curr = head

        # while curr:
        #     if curr in visited:
        #         return curr
            
        #     visited.add(curr)
        #     curr = curr.next
        
        # return None