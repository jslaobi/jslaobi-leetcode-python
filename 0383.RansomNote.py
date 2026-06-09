class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        counts = {}

        for char in magazine:
            counts[char] = counts.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in counts or counts[char] == 0:
                return False
            
            counts[char] -= 1
        
        return True