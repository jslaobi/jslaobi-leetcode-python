# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """合并两个已排序链表。

        时间复杂度: O(m+n)，m,n 为两个链表长度。
        空间复杂度: O(1)，只使用常数级指针空间。
        """
        curr = ListNode(0)
        dummy = curr

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1:
            curr.next = list1
            list1 = list1.next

        if list2:
            curr.next = list2
            list2 = list2.next
        
        return dummy.next
            