class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mappings = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for char in s:
            # 如果是开括号，，就把对应的闭括号放入，方便将来比较
            if char in mappings:
                stack.append(mappings[char])
            else:
                # 如果是闭括号，首先检查stack不为空（应对[")"]这种情况），然后对比检查是否是匹配的闭括号
                if not stack or stack.pop() != char:
                    return False
        # 如果遍历完了stack还不为空，说明有多余的开括号    
        if len(stack) != 0:
            return False
        
        return True
