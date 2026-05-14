# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """交换链表中的节点对。

        时间复杂度: O(n)，其中 n 是链表节点数。每个节点最多访问一次。
        空间复杂度: O(1)，只使用常数级额外指针空间。
        """
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr.next and curr.next.next:
            n1 = curr.next
            n2 = curr.next.next
            # 三部曲,硬记住就好
            curr.next = n2
            n1.next = n2.next
            n2.next = n1

            # 向前移动,准备处理下一组
            curr = n1

        return dummy.next
