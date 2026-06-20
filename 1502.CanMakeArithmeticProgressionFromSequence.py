class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        min_val = min(arr)
        max_val = max(arr)
        n = len(arr)

        if min_val == max_val:
            return True
        
        # n个数之间有n-1个间距. 比如0,1两个数:间距是(1-0) / (2-1) = 1
        # 这里计算能否被n-1整除,如果不能就表示不存在统一间距
        if (max_val - min_val) % (n - 1) != 0:
            return False
        
        gap = (max_val - min_val) // (n - 1)

        num_set = set(arr)
        # 按照间距计算每一个数,并且检查是否存在于num_set中
        for i in range(n):
            expected_num = min_val + (i * gap)
            if expected_num not in num_set:
                return False
        
        return True