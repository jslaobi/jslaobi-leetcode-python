class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]

        for s in range(1, len(strs)):
            while not strs[s].startswith(prefix):
                prefix = prefix[:-1]
            
            if not prefix:
                return ""
        
        return prefix
