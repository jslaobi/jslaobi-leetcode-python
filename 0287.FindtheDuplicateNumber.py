class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        slow = nums[0]
        fast = nums[nums[0]]

        # 类似检测链表循环, 但是每次不是移动一步,而是移动到nums[slow], 比如nums[0] == 3, 就将slow移动到3, fast进行两次这个操作
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # 放回起点,寻找环的起点
        slow = 0
        
        while slow != fast:
            # 每次移动一下
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
