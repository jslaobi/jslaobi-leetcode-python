class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        if len(nums) < 4:
            return False
        
        state = 1

        for i in range(1, len(nums)):
            # 必须是升序或者降序, 不能相等
            if nums[i] == nums[i-1]:
                return False
            
            # state == 1, 如果i没能至少移动一位,则不构成升序,返回False
            if state == 1:
                if nums[i-1] > nums[i]:
                    if i == 1:
                        return False
                    
                    state = 2
            
            # state == 2, 如果nums[i-1] < nums[i]则进入降序, state = 3
            if state == 2:
                if nums[i-1] < nums[i]:
                    state = 3
            
            # state == 3, 如果之后再有降序,则不符合条件,返回False
            if state == 3:
                if nums[i-1] > nums[i]:
                    return False

        # state必须进行到3
        return state == 3