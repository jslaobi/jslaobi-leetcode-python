class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # 在结尾存储当前word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """时间复杂度: O(m * n * 4^L)。
        空间复杂度: O(total_chars)。
        """
        root = TrieNode()
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

            node.word = word
        
        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent.children[char]

            # 如果不是None,则说明到了结尾,将word加入结果
            if curr_node.word is not None:
                result.append(curr_node.word)
                # 然后将它设置为None, 防止重复
                curr_node.word = None
            
            # backtrack三部曲: 设置为#防止重复访问,向四周探索,恢复成原来的字符
            board[r][c] = '#'

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] in curr_node.children:
                    # 这里传的不是curr_node.children[board[nr][nc]], 因为我们要传parent而不是当前node
                    dfs(nr, nc, curr_node)
            
            board[r][c] = char


        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        
        return result

            