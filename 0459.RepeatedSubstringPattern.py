class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        n = len(s)

        for i in range(1, n // 2 + 1):
            # 子字符串长度必须能被整长度整除,否则跳过
            if n % i == 0:
                substring = s[:i]

                # 将substring重复n // i次
                if substring * (n // i) == s:
                    return True
        
        return False