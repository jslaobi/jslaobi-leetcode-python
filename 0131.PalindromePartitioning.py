class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def dfs(i):
            if i == len(s):
                result.append(path[:])
                return
                
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    path.append(s[i: j+1])
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return result

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] == s[right]:
                left += 1
                right-= 1
            else:
                return False

        return True 