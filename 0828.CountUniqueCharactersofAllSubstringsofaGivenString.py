from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        时间复杂度: O(n)，n 为字符串长度。
        空间复杂度: O(1)。
        """
        index_map = defaultdict(list)

        for i in range(len(s)):
            index_map[s[i]].append(i)
        
        total_count = 0
        n = len(s)

        for char, indices in index_map.items():
            # 例如AXYZA, indices = [0,4], padded_indices = [-1, 0, 4, 5]
            padded_indices = [-1] + indices +[n]

            for i in range(1, len(padded_indices) - 1):
                # 对于第一个A, left_count = 0-(-1) = 1, right_count = 4-0 = 4: 1 * 4 = 4个子字符串:A, AX, AXY, AXYZ
                # 再举一个例子: XAYZA. left_count = 1-(-1) = 2, right_count = 4-1 = 3: 2 * 3 = 6个子字符串: XA, XAY, XAYZ, A, AY, AYZ
                left_count = padded_indices[i] - padded_indices[i - 1]
                right_count = padded_indices[i + 1] - padded_indices[i]
                total_count += (left_count * right_count)
            
        
        return total_count