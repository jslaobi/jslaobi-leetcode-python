class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
            时间复杂度: O(n)。
            空间复杂度: O(1)。
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        # 当mid与high相遇时,还需要再处理一次,那个数字可能是0,1,2,所以这里用<=
        while mid <= high:
            # 3种数字: 0,1,2
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        

