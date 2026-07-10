from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        char_counts = Counter(s)
        result = []

        for char in order:
            if char in char_counts:
                result.append(char * char_counts[char])
                # 删除使用过的元素, 剩下的元素都是order中没有的元素
                del char_counts[char]
        
        for char in char_counts:
            result.append(char * char_counts[char])
        
        return "".join(result)