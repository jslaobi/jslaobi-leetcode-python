# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        # k可能大于length
        k = k % length

        if k == 0:
            return head
        
        tail.next = head
        # 比如一共7个节点,从后面移动了2个节点到前面,那么新的结尾就是7-2-1=4,从头节点移动4步到达第5个节点
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next
        # 有了新的尾节点, 新的头节点就是下一个
        new_head = new_tail.next
        # 断开循环
        new_tail.next = None

        return new_head
