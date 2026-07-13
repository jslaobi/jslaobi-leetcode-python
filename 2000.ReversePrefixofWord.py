class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        # 1. 寻找ch的位置,找到后退出循环,因为取的是第一次出现的位置
        index = -1
        for i, char in enumerate(word):
            if char == ch:
                index = i
                break

        if index == -1:
            return word

        word_list = list(word)
        # 2. 双指针反转字符串
        left = 0 
        right = index
        while left < right:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left += 1
            right -= 1
        
        return "".join(word_list)
