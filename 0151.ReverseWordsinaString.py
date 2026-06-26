class Solution:
    # 例如: "the sky", 第一步去除首位的空格
    def reverseWords(self, s: str) -> str:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        def trim_space(s):
            left = 0
            right = len(s) - 1

            # 去除首尾的空格
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1
            
            output = []
            while left <= right:
                # 如果不是空格,则直接添加到output
                if s[left] != ' ':
                    output.append(s[left])
                # 否则,只有当前一个添加的不是空格的时候,才添加空格
                elif output[-1] != ' ':
                    output.append(s[left])
                left += 1
            return output
        # 第二步,反转所有字符, 成为"yks eht"
        def reverse(word_list, left, right):
            while left < right:
                word_list[left], word_list[right] = word_list[right], word_list[left]
                left += 1
                right -= 1

        # 第三部: 反转每个单词, "sky the"
        def reverse_each_word(word_list):
            n = len(word_list)
            start = 0
            end = 0

            while start < n:
                while end < n and word_list[end] != ' ':
                    end += 1
            
                reverse(word_list, start, end - 1)

                start = end + 1
                end += 1
        
        # 执行上面的三步
        char_list = trim_space(s)
        reverse(char_list, 0, len(char_list) - 1)
        reverse_each_word(char_list)

        return "".join(char_list)