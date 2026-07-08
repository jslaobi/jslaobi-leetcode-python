class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        时间复杂度: O(n*m)。
        空间复杂度: O(1)。
        """
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            # 如果是字符, 则需要严格相等
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                
                i += 1
                j += 1
            # 如果是数字,注意要获取多位数的情况
            else:
                # 题目要求,不允许有leading 0
                if abbr[j] == '0':
                    return False


                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                # i指针向前移动num个字符
                i += num
        
        # 最后两个指针都必须到达结尾才算相符
        return i == len(word) and j == len(abbr)