class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []

        for i, word in enumerate(words):
            # 如果首字符是元音
            if word[0] in vowels:
                goat_word = word + "ma"
            # 如果不是元音
            else:
                goat_word = word[1:] + word[0] + "ma"
            
            goat_word += 'a' * (i + 1)

            result.append(goat_word)
        
        return " ".join(result)


