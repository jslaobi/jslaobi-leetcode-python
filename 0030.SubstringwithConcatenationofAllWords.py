from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        时间复杂度: O(n^2)。
        空间复杂度: O(1)。
        """
        if not s or not words:
            return []
        
        # 根据题目描述,每个单词的长度是相同的
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return []
        
        word_map = Counter(words)
        result = []

        # 我们采取按照每个word而不是每个字符进行检查
        # 但是如果不是从0,而是从1或者2开始的情况该怎么办, 所以我们用一个for循环来解决问题
        # for循环会假定从0到word_len中间的任何起点开始
        for i in range(word_len):
            left = i
            right = i
            curr_map = Counter()
            words_found = 0

            # 每次前进word_len个字符
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_map:
                    curr_map[word] += 1
                    words_found += 1

                    # 如果当前的word数量超过了words里提供的数量, 那么就要减去超量的部分到允许的上限
                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        words_found -= 1
                        left += word_len
                    
                    # 如果找到的word数量等于word_count(words数组里word的个数),则添加到答案
                    if words_found == word_count:
                        result.append(left)

                # 如果word不在word_map里, 则当前子字符串不成立,重置所有计数并从right开始继续寻找
                else:
                    curr_map.clear()
                    words_found = 0
                    left = right
        
        return result

