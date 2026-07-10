# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        if not head or not head.next:
            return 
        
        # 第一步, 寻找中间节点
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # 第二步, 反转后半链表
        prev = None
        curr = head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head1 = head
        head2 = prev

        # 第三步, 合并前后链表
        while head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2
        
        