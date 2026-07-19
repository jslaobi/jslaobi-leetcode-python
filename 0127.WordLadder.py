from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """时间复杂度: O(n * m * 26)。
        空间复杂度: O(n)。
        """
        # 先转化成set, 这样只用O(1)查找时间
        word_set = set(wordList)

        if endWord not in word_set:
            return 0
        

        queue = deque()
        # queue里存放(当前单词,步数). 根据题目描述和示例,其实单词也算作一步,所以初始值是1
        queue.append((beginWord, 1))

        while queue:
            curr_word, steps = queue.popleft()

            if curr_word == endWord:
                return steps
            
            # 尝试替换单词每个位置的字符
            for i in range(len(curr_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = curr_word[:i] + char + curr_word[i+1:]

                    if next_word in word_set:
                        queue.append((next_word, steps + 1))

                        # 加入queue后立刻从word_set中删除这个单词防止重复尝试, 这样就可以省下一个visited数组
                        word_set.remove(next_word)
        
        return 0
