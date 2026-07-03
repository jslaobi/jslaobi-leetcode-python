class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        s_list = list(s)

        stack = []

        for i, char in enumerate(s_list):
            if s_list[i] == '(':
                stack.append(i)
            elif s_list[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''
        
        for i in stack:
            s_list[i] = ''
            
        return "".join(s_list)