class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度: O(n^2)，n 为链表长度。
        空间复杂度: O(1)。
        Definition for singly-linked list.
        class ListNode:
        def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-5001)
        dummy.next = head
        last_sorted = head
        curr = head.next

        while curr:
            if last_sorted.val <= curr.val:
                curr = curr.next
                last_sorted = last_sorted.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = last_sorted.next
        return dummy.next