class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = { char for char in word if char.islower() }
        # lower_set = set()
        # for char in word:
        #     if char.islower():
        #         lower_set.add(char) 
        upper_set = { char.lower() for char in word if char.isupper() }
        # upper_set = set()
        # for char in word:
        #     if char.isupper():
        #         upper_set.add(char.lower()) 
        
        return len(lower_set & upper_set)