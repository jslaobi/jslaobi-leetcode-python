from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        freq = Counter(s)

        # # 题目不会出现无效的组合,所以不需要检查
        # odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        # if odd_count > 1:
        #     return ""

        first_half = []
        mid_char = ''

        for char in "abcdefghijklmnopqrstuvwxyz":
            if freq[char] > 0:
                if freq[char] % 2 != 0:
                    mid_char = char
                
                # 如果出现5次, 则5//2=2, 添加两次
                first_half.append(char * (freq[char] // 2))
        
        first_half_str = "".join(first_half)

        return first_half_str + mid_char + first_half_str[::-1]
