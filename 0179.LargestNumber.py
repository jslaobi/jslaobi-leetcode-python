class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        nums_str = [str(num) for num in nums]

        def compare(x, y):
            if x + y > y + x:
                return -1 # x应该在y的前面
            elif x + y < y + x:
                return 1 # y应该在x的前面
            else:
                return 0
        
        nums_str.sort(key=cmp_to_key(compare))

        largest_num = "".join(nums_str)

        if largest_num[0] == '0':
            return "0"
        
        return largest_num