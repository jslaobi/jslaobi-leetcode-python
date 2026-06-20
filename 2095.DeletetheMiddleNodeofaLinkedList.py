# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        # 如果只有一个节点, 删除后也为None
        if not head or not head.next:
            return None

        slow = head
        # 这里找到不是中间节点, 而是要让slow停在中间节点的前一个节点然后通过slow.next = slow.next.next删除中间节点. 
        # 所以不能fast = head, 而是需要让fast先走一个循环, 也就是两步. 
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return head
        