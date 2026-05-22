class TrieNode:
    def __init__(self):
        """Trie 求两个数组中最大公共前缀长度。

        时间复杂度: O((n+m) * d)，n 和 m 分别为两个数组长度，d 为字符串平均长度。
        空间复杂度: O(n * d)，用于 Trie 存储。
        """
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, num_str: str) -> None:
        node = self.root
        for char in num_str:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
    def get_longest_prefix_length(self, num_str: str) -> int:
        node = self.root
        length = 0
        for char in num_str:
            if char in node.children:
                length += 1
                node = node.children[char]
            else:
                break
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            trie.insert(str(num))
        
        max_length = 0

        for num in arr2:
            current_length = trie.get_longest_prefix_length(str(num))
            max_length = max(max_length, current_length)
        
        return max_length