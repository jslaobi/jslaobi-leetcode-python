class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = {'a': 0, 'b': 0,'c': 0}
        left = 0
        right = 0
        total_substrings = 0
        n = len(s)

        while right < n:
            counts[s[right]] += 1

            while counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0:
                # 如果找到了一个符合条件的子字符串, 之后所有的子字符串都符合条件,所以可以直接加n - right进结果
                total_substrings += n - right

                # 缩小窗口继续寻找下一个符合条件的子字符串
                counts[s[left]] -= 1
                left +=1
                
            right += 1

        return total_substrings