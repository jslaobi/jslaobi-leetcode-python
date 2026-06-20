# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import math
import random

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        def get_matches(word1, word2):
            matches = 0

            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    matches += 1
            
            return matches
        
        candidates = words[:]
        
        # 最多只能猜10次
        for _ in range(10):
            # 为了过leetcode提交,增加随机性. 如果不行就多试几次
            random.shuffle(candidates)
            # best_word记录竞猜的最优解(mini_max最小的数)
            best_word = ""
            mini_max = math.inf
            # 假设每一个单词是secret word
            for guess_word in candidates:
                # 单词的长度是固定的6
                # 创造一个0-6的数组,利用匹配字符数给单词分组,选出符合条件的单词数最多的那个组
                match_counts = [0] * 7

                for target_word in candidates:
                    if guess_word != target_word:
                        matches = get_matches(guess_word, target_word)
                        match_counts[matches] += 1
                current_max_count = max(match_counts)
                if current_max_count < mini_max:
                    mini_max = current_max_count
                    best_word = guess_word
            
            matches = master.guess(best_word)

            if matches == 6:
                return
            # 如果matches不等于6, 则需要根据matches数
            else:
                new_candidates = []
                for word in candidates:
                    if get_matches(word, best_word) == matches:
                        new_candidates.append(word)
            
                candidates = new_candidates
