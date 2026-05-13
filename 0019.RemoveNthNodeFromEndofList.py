# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 当遇到需要删除头节点的情况时，我们就需要创建一个dummy
        # 这样无论删除哪个节点，我们都可以通过dummy.next来返回新的头节点
        dummy = ListNode(0)
        dummy.next = head
        n1 = dummy
        n2 = dummy

        for i in range(n):
            n2 = n2.next
        
        # 使用while n2.next在处理空链表或者只有一个节点的情况比while n2更安全
        while n2.next:
            n1 = n1.next
            n2 = n2.next
        
        n1.next = n1.next.next
        return dummy.next