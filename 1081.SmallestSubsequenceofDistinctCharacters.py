class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        last_seen = {}
        # 寻找记录每个字符最后出现的位置
        for i, char in enumerate(s):
            last_seen[char] = i
        
        stack = []
        seen = set()

        for i, char in enumerate(s):
            # 如果已经在seen中了(也即已经在stack中), 则认定为重复并跳过
            if char in seen:
                continue
            
            # 如果当前的字符比stack顶部的字符更小,并且当前位置不是将该字符加入stack的最后机会, 则先pop, 后面再加入
            while stack and char < stack[-1] and i < last_seen[stack[-1]]:
                popped_char = stack.pop()
                seen.remove(popped_char)
            
            stack.append(char)
            seen.add(char)
        
        return "".join(stack)
        

