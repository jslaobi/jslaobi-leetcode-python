class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        # 这道题的进阶要求是不允许把整数转成字符串然后用双指针来比较字符，所以我们需要通过%和//来逐位处理整数。
        # 我们通过数学运算，达到x存储整数前半部分，reverse_half存储整数后半部分的反转。然后比较两者。
        # 比如1221， 我们可以处理到x=12， reverse_half=12， 这时就可以比较了。
        reverse_half = 0

        while x > reverse_half:
            # 每次把reverse_half原有的内容进一位（也就是乘以10），同时再把x的最后一位加到reverse_half的末尾，就可以达到拼接的效果
            reverse_half = reverse_half * 10 + x % 10
            # 同时别忘了每次把x的最后一位去掉（也就是整除10）
            x = x // 10
        # 如果整数的长度是偶数，那么就可以直接比较了；如果整数的长度是奇数，要把reverse_half去掉最后一位（也就是整除10）再和x比较
        # 比如12321， 当我们处理到x=12， reverse_half=123时，reverse_half比x多了一位，所以要把reverse_half去掉最后一位（也就是整除10）再和x比较。
        return x == reverse_half or x == reverse_half // 10