class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """时间复杂度: O(n * m * L)。
        空间复杂度: O(n)。
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            # 使用每个单词进行查找
            for word in wordDict:
                word_length = len(word)

                if i >= word_length:
                    # 由于字符串只能由有效单词组成,中间不允许出现无效字符.所以需要检查:
                    # 1. 之前是一个有效单词,或者是字符串起始(dp[0] = True)
                    # 2. 当前的i - word_length: i是一个有效单词
                    if dp[i - word_length] == True and s[i - word_length: i] == word:
                        # 那么就可以把dp[i]设置成True并且继续向后检查
                        dp[i] = True
                        # 由于在当前的i位置找到了一个有效单词,就不需要试其他单词了
                        break
        
        return dp[-1]
            
        # # 转换成set为了获得O(1)的查询速度
        # word_set = set(wordDict)
        # memo = {}

        # def dfs(remaining_string):
        #     if not remaining_string: 
        #         return True
            
        #     if remaining_string in memo:
        #         return memo[remaining_string]
            
        #     for i in range(1, len(remaining_string) + 1):
        #         # 将字符串分为前后两部分
        #         prefix = remaining_string[:i]
        #         suffix = remaining_string[i:]
            
        #         if prefix in word_set and dfs(suffix):
        #             # 理论上这句不需要,因为当是True时会一路返回,直接终结函数并返回True为最终结果
        #             # 但是为了使用这个模版为后面的word break II,这里写这句为了格式统一
        #             memo[remaining_string] = True
        #             return True
        #     # False则不能省,因为还要继续. 这里存False的值节省时间,减少时间复杂度
        #     memo[remaining_string] = False
        #     return False
        
        # return dfs(s)