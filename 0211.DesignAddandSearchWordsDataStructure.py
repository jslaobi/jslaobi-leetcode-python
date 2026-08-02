class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """时间复杂度: O(m)。
        空间复杂度: O(m)。
        """
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        """时间复杂度: O(Σ)（最坏情况为 O(m * 26^k)）。
        空间复杂度: O(m)。
        """

        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            char = word[index]

            # 如果是., 搜索所有的children
            if char == '.':
                # 这里要取所有的node, 所以是node.children.values()
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])
        
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)