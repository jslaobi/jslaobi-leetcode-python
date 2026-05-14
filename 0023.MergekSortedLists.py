# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """优先队列合并 k 条链表。

        时间复杂度: O(N log k)，N 为所有链表节点总数，k 为链表数量。
        空间复杂度: O(k)，堆中最多保存 k 个节点。
        """
        dummy = ListNode(0)
        curr = dummy
        min_heap = []

        # 这里是把每个链表的头节点加入,而不是把所有节点都加入,以节省空间和时间
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))

        while min_heap:
            val, i, l = heapq.heappop(min_heap)

            curr.next = ListNode(val)
            curr = curr.next
            # 因为之前加入的是链表的头节点,所以每次弹出后,需要把这个链表的下一个节点重新加入
            if l.next:
                heapq.heappush(min_heap, (l.next.val, i, l.next))

        return dummy.next