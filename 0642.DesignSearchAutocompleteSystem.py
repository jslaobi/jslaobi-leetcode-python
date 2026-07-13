from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.sentence = ""

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        """时间复杂度: O(total_chars)。
        空间复杂度: O(total_chars)。
        """
        self.root = TrieNode()
        self.counts = {}
        self.current_prefix = ""
        self.current_node = self.root
        
        # Populate the initial historical data
        for i in range(len(sentences)):
            self.counts[sentences[i]] = times[i]
            self._add_to_trie(sentences[i])

    def _add_to_trie(self, sentence: str) -> None:
        """Helper to insert a sentence into the Trie."""
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.sentence = sentence

    def input(self, c: str) -> List[str]:
        # Case 1: The user finished typing the sentence
        if c == '#':
            # Update frequency
            self.counts[self.current_prefix] = self.counts.get(self.current_prefix, 0) + 1
            # Add to Trie (if it's already there, this is harmless)
            self._add_to_trie(self.current_prefix)
            
            # Reset states for the next search query
            self.current_prefix = ""
            self.current_node = self.root
            return []
        
        # Case 2: The user is actively typing
        self.current_prefix += c
        
        # Move our Trie pointer down one level
        if self.current_node and c in self.current_node.children:
            self.current_node = self.current_node.children[c]
        else:
            # The user typed a character that doesn't match any historical prefix
            self.current_node = None
            return []
            
        # Case 3: Fetch all possible completions from this node
        completions = []
        self._dfs(self.current_node, completions)
        
        # Sort by frequency (descending: -self.counts[x]) and then ASCII (ascending: x)
        completions.sort(key=lambda x: (-self.counts[x], x))
        
        # Return the top 3
        return completions[:3]

    def _dfs(self, node: TrieNode, completions: List[str]) -> None:
        """Helper to find all sentences in the subtree of the current node."""
        if not node:
            return
        
        if node.is_end:
            completions.append(node.sentence)
            
        for char in node.children:
            self._dfs(node.children[char], completions)