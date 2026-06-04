class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def getWaviness(num: int):
            s = str(num)
            waviness = 0
            if len(s) < 3:
                return waviness
            
            for i in range(1, len(s) - 1):
                if s[i - 1] < s[i] and s[i] > s[i+1]:
                    waviness += 1
                elif s[i - 1] > s[i] and s[i] < s[i+1]:
                    waviness += 1
            
            return waviness

        total_waviness = 0
        for i in range(num1, num2 + 1):
            total_waviness += getWaviness(i)
        
        return total_waviness