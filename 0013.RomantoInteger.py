class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        prev_value = 0
        # 从后往前读
        for char in reversed(s):
            curr_value = roman_values[char]
            # 一旦出现IV这样的,都是要从后面的数减去前面的数
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value

            prev_value = curr_value

        return total