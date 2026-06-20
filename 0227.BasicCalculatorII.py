class Solution:
    def calculate(self, s: str) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        total_sum = 0
        last_num = 0
        current_num = 0
        last_sign = '+'

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            if char in "+-*/" or i == len(s) - 1:
                if last_sign == '+':
                    total_sum += last_num
                    last_num = current_num
                elif last_sign == '-':
                    total_sum += last_num
                    last_num = -current_num
                elif last_sign == '*':
                    last_num = last_num * current_num
                elif last_sign == '/':
                    # 当处理负数时, last_num = -5, current_num = 2, last_num // current_num = -3, int(last_num / current_num) = -2
                    last_num = int(last_num / current_num)
                
                last_sign = char
                current_num = 0

        # 最后不要忘了把待处理的last_num加入total
        total_sum += last_num
        return total_sum

        # stack = []
        # curr_num = 0
        # # 将初始符号设定为+, 比如处理29-时, 会将第一个数29加入stack
        # last_sign = '+'

        # for i in range(len(s)):
        #     char = s[i]

        #     if char.isdigit():
        #         curr_num = curr_num * 10 + int(char)
        #     # 同理, 处理最后一个数时, 也要依照之前的符号
        #     if char in "+-*/" or i == len(s) - 1:
        #         if last_sign == '+':
        #             stack.append(curr_num)
        #         elif last_sign == '-':
        #             stack.append(-curr_num)
        #         elif last_sign == '*':
        #             last_num = stack.pop()
        #             stack.append(last_num * curr_num)
        #         elif last_sign == '/':
        #             last_num = stack.pop()
        #             # 当处理负数时, last_num = -5, curr_num = 2, last_num // curr_num = -3, int(last_num / curr_num) = -2
        #             stack.append((int(last_num / curr_num)))
        #         # 如果是符号, 更新符号, 重置curr_num(如果是最后一个数则无所谓)    
        #         last_sign = char
        #         curr_num = 0
        
        # return sum(stack)

            