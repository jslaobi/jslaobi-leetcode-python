class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度: O(n)，n 为链表长度。
        空间复杂度: O(1)。
        Definition for singly-linked list.
        class ListNode:
        def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev