# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """双指针删除链表倒数第 n 个节点。

        时间复杂度: O(n)，n 为链表长度。
        空间复杂度: O(1)，只使用常数级额外指针空间。
        """
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