import collections

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        """
        时间复杂度: O(n*k)。
        空间复杂度: O(n*k)。
        """
        groups = collections.defaultdict(list)

        for s in strings:
            diffs = []

            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                diffs.append(diff)
            
            groups[tuple(diffs)].append(s)
        
        return list(groups.values())
