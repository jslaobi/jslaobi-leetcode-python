class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(left_bias: bool) -> int:
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    # 先把当前找到的最合适的位置记录下来
                    index = mid
                    # 因为有重复数字,所以要继续向左或者向右搜索
                    if left_bias == True:
                        right = mid - 1
                    else:
                        left = mid +1
            return index
        
        left = binary_search(True)
        right = binary_search(False)

        return [left, right]