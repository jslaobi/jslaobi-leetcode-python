class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        stack = []

        for token in tokens:
            if token in "+-*/":
                # pop出两个数进行运算
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)   
                # 不能用//, 因为如果是负数就会得到错误答案                        
                elif token == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]