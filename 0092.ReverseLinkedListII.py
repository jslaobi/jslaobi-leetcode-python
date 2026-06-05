class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        时间复杂度: O(n)，n 为链表长度。
        空间复杂度: O(1)。
        Definition for singly-linked list.
        class ListNode:
        def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        for _ in range(left, right):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
            