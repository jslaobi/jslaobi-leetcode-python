# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """链表逐位相加。

        时间复杂度: O(max(m,n))，m,n 为两条链表长度。
        空间复杂度: O(1)，只使用常数级额外指针空间（返回结果链表不计入额外空间）。
        """
        curr = ListNode(0)
        dummy = curr
        carry = 0
        while l1 or l2 or carry:
            # 一定不要忘了curr， l1， l2都要在每一步结束后移动到next
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next