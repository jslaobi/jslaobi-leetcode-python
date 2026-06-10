class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)

        i = 0
        j = 0

        while i < n or j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            
            if i == n and j == n:
                return True
            
            if i == n or j == n:
                return False
            
            if start[i] != result[j]:
                return False
            # 如果是L,则只能往左移动, i小于j说明当前L已经在更左边了, 再怎么向左移动也无法匹配
            if start[i] == 'L' and i < j:
                return False
            # 如果是R,则只能往右移动, j小于i说明当前R已经在更右边了, 再怎么向右移动也无法匹配
            if start[i] == 'R' and j < i:
                return False
            
            i += 1
            j += 1
        
        return True
