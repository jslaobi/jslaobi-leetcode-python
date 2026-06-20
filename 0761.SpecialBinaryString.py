class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        时间复杂度: O(2^n)，
        空间复杂度: O(n)。
        """
        count = 0
        i = 0
        result = []

        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            # 当1和0的数量相等,我们就找到一个符合条件的子字符串
            # 但是, 我们还要继续探索里面是否有更小的符合条件的子字符串. 比如11100100, 我们要找到"101100",最后要找到["10", "1100"]
            if count == 0:
                # 这里要做一个backtrack
                # 从首尾各剥除一个1和一个0
                inner_string = s[i + 1: j]
                # 然后再递归寻找更小的符合条件子字符串
                processed_inner = self.makeLargestSpecial(inner_string)
                result.append('1'+processed_inner+'0')
                i = j + 1
        # 比如["10", "1100"],要排序成["1100", "10"]
        result.sort(reverse=True)

        # 最后返回"110010"
        return "".join(result)