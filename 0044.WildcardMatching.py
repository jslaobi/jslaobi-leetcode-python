class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        s_index = 0
        p_index = 0
        star_index = -1
        temp_s_index = -1

        while s_index < s_len:
            # 第一种情况, 两个字符相等或者p当前字符是?
            if p_index < p_len and (s[s_index] == p[p_index] or p[p_index] == '?'):
                s_index += 1
                p_index += 1
            # 第二种情况, p当前字符是*, 假定* match0个字符
            elif p_index < p_len and p[p_index] == '*':
                # 记录当前s和p的指针的位置
                star_index = p_index
                temp_s_index = s_index
                # 由于假定* match0个字符, 只向前移动p_index
                p_index += 1
            # 第三种情况, 当前字符不匹配, 之前假定了* match0个字符, 现在逐渐向前移动temp_s_index, 检查*匹配一个或者多个字符的可能性
            elif star_index != -1:
                temp_s_index += 1
                # 重新设置s_index和p_index, 防止越界
                s_index = temp_s_index
                p_index = star_index + 1
            else:
                return False
        
        # 最后检查结尾的*
        while p_index < p_len and p[p_index] == '*':
            p_index += 1
        
        return p_index == p_len

                
        