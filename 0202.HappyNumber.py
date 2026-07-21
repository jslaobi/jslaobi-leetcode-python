class Solution:
    def isHappy(self, n: int) -> bool:
        """时间复杂度: O(k)。
        空间复杂度: O(k)。
        """
        def get_next(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                num = num // 10

                # 把每一位数字的平方加起来
                total_sum += digit ** 2
            
            return total_sum
        
        seen = set()

        # 过程到1停止, 所以n不能是1. 同时要使用一个set来避免死循环
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1