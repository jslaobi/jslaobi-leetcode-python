class Solution:
    def reverse(self, x: int) -> int:
        """整数反转。

        时间复杂度: O(log|x|)，|x| 为整数的绝对值，迭代次数与数字位数成正比。
        空间复杂度: O(1)，只使用常数级额外变量。
        """
        # 先剥离符号只处理绝对值
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0

        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            #题目要求如此... leetcode会有测试用例来检查这个越界的处理
            if result < -2 ** 31 or result > 2 ** 31 - 1:
                return 0
            x = x // 10
        # 最后再加回符号
        return sign * result