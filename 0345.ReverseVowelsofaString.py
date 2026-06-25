class Solution:
    def reverseVowels(self, s: str) -> str:
        # python里不能直接修改字符串,所以要先转换成数组
        char_list = list(s)
        left = 0
        right = len(char_list) - 1
        vowel_set = set("aeiouAEIOU")

        while left < right:
            while left < right and char_list[left] not in vowel_set:
                left += 1
            while left < right and char_list[right] not in vowel_set:
                right -= 1
            
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1

        return "".join(char_list)
                
            