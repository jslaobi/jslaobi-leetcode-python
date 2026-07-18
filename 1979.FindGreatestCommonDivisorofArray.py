class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        min_num = min(nums)
        max_num = max(nums)

        def compute_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return compute_gcd(min_num, max_num)