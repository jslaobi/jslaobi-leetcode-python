class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """回溯生成电话号码字母组合。

        时间复杂度: O(4^n * n)，n 为输入数字长度，最坏情况下每个数字映射 4 个字母。
        空间复杂度: O(n)，递归调用栈深度和当前构造字符串长度。
        """
        if not digits:
            return []
        
        result = []
        mappings = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, current_str):
            # 如果当前字符串的长度达到了输入数字的长度，说明我们已经找到了一种组合，可以将其加入结果列表中
            if len(current_str) == len(digits):
                result.append(current_str)
                return
            
            # 否则的话，我们继续往下探索，首先获取当前数字对应的字母
            # 比如输入数字是"1234"，当我们处理到数字"3"的时候(digit等于3）
            # 我们就需要获取数字"3"对应的字母"def"（letters等于"def"）
            digit = digits[index]
            letters = mappings[digit]

            # 然后我们遍历这些字母，对于每一个字母，我们都将其添加到当前字符串中，并继续递归地处理下一个数字
            for letter in letters:
                backtrack(index + 1, current_str + letter)
        
        backtrack(0, "")
        return result