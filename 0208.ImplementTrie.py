class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """时间复杂度: O(m)。
        空间复杂度: O(m)。
        """
        curr = self.root
        
        for char in word:
            # 如果char不存在,就在children里添加char并且设为新TrieNode
            if char not in curr.children:
                curr.children[char] = TrieNode()

            #移动到curr.children[char]
            curr = curr.children[char]
        
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """时间复杂度: O(m)。
        空间复杂度: O(1)。
        """
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        # app和apple不一样
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """时间复杂度: O(m)。
        空间复杂度: O(1)。
        """
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)