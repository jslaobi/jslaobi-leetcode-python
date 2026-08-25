from collections import defaultdict
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        char_map = defaultdict(int)
        max_length = 0
        while right < len(s):
            right_char = s[right]
            char_map[right_char] += 1

            while char_map[right_char] > 2:
                left_char = s[left]
                char_map[left_char] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length
            

