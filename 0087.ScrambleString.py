class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        """字符串分割递归判断是否为扰乱字符串。

        时间复杂度: O(n^4)（带缓存），n 为字符串长度。
        空间复杂度: O(n^3)，用于缓存和递归栈。
        """
        if s1 == s2:
            return True
        
        if len(s1) != len(s2):
            return False
        
        if sorted(s1) != sorted(s2):
            return False
        
        length = len(s1)
        # 从1开始,排除了空字符串""的情况, 比如s1[:0] = "" (empty), s1[0:] = "eat"
        for i in range(1, length):
            # 第一种情况,前后不交换:s1的左侧与s2的左侧对比
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            # 第二种情况,前后交换:s1的左侧与s2的右侧对比
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
            # s1 = "great", s1[:2] = "gr", s1[2:] = "eat", s1[-2:] = "at", s1[:-2] = "gre"
        return False
