class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""

        for char in s:
            # 如果是数字,就用继续将当前的数字一点点完整的读取出来, 然后存到current_num
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            # 如果是[, 就把当前的current_string和current_num暂存到stack里, 然后重新开始,处理更内一层
            elif char == '[':
                stack.append((current_string, current_num))
                current_num = 0
                current_string = ""
            # 如果是], 就证明当前一层已经处理完毕, 将当前值与stack里的值拼接
            elif char == ']':
                last_string, last_num = stack.pop()
                current_string = last_string + (current_string * last_num)
            # 如果是字母, 就添加到current_string
            else:
                current_string += char
        
        return current_string