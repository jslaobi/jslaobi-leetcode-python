class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        curr_num = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char in "+-":
                result += sign * curr_num
                curr_num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # 如果遇到括号,就先把目前的结果寄存在stack里,然后开始计算括号内的内容
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                # 遇到闭括号, 就完成括号内的计算. 注意之前重置了result, 所以这里的result只是括号内的result
                result += sign * curr_num
                curr_num = 0
                # 把括号前的符号计算进去, 比如括号内结果是5,括号前是-, 就是-5
                result *= stack.pop()
                # 把括号前的旧计算结果也加进去, 因为进括号前将result重置为0了
                result += stack.pop()

        # 最后还要把最后一个数加进去, 比如10+5, 别忘了最后这个+5
        result += sign * curr_num

        return result
