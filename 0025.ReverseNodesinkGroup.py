# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        def go_to_kth(curr):
            steps = 0
            while curr and steps < k:
                curr = curr.next
                steps += 1
            return curr

        dummy = ListNode(0)
        dummy.next = head

        # prev_group_dummy是在当前的k个元素之前的节点
        prev_group_dummy = dummy

        while True:
            kth_node = go_to_kth(prev_group_dummy)
            # 如果当前没有k个节点, 则直接返回
            if not kth_node:
                break
            
            next_group_head = kth_node.next

            prev = next_group_head
            curr = prev_group_dummy.next

            while curr != next_group_head:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group_dummy.next
            prev_group_dummy.next = kth_node
            prev_group_dummy = temp

        return dummy.next

