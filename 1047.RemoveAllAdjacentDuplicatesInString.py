class Solution:
    def removeDuplicates(self, s: str) -> str:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)