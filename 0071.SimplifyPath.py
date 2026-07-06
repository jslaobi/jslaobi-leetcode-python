class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            # 如果是../,则要向上一级,所以从stack弹出一个元素
            if part == '..':
                if stack:
                    stack.pop()
            # 如果是./或者/, 则无事发生
            elif part == '.' or part == '':
                continue
            # 如果是其他,则当作文件夹名添加进stack
            else:
                stack.append(part)
        
        # '/'.join(stack)不会在开头加'/', 所以要额外写一个
        return '/' + '/'.join(stack)