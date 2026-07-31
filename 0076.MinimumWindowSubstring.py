from collections import Counter, defaultdict
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """时间复杂度: O(n + m)。
        空间复杂度: O(k)。
        """
        if not t or not s:
            return ""
        

        t_count = Counter(t)
        
        unique_chars = len(t_count)

        valid_count = 0

        window_counts = defaultdict(int)

        # (window_length, left_pointer, right_pointer)
        result = (math.inf, None, None)

        left = 0
        right = 0

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            # 如果目前窗口的char出现次数与t里的出现次数相等, valid_count += 1
            if char in t_count and t_count[char] == window_counts[char]:
                valid_count += 1

            # 如果目前统计到的符合条件字符个数和unique_chars相等,则完全符合条件,缩小窗口试图寻找更小的窗口size
            while left <= right and valid_count == unique_chars:
                # result[0]是window_length
                if (right - left + 1) < result[0]:
                    result = ((right - left + 1), left, right)

                left_char = s[left]
                window_counts[left_char] -= 1

                # 检查如果left_char在t_count里,同时移除后导致window_counts小于t_count,更新valid_count的值,并且下次while循环会自动跳出
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    valid_count -= 1
                
                left += 1

            right += 1

        if result[0] == math.inf:
            return ""
        else:
            # result[1]是left, result[2]是right
            return s[result[1]: result[2]+1]
