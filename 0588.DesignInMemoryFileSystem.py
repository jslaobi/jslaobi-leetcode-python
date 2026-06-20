class TrieNode:
    def __init__(self):
        """
        时间复杂度: O(n log n)，
        空间复杂度: O(1)。
        """
        self.children = {}
        self.is_file = False
        self.content = ""

class FileSystem:
    def __init__(self):
        # The root directory "/"
        self.root = TrieNode()

    def ls(self, path: str) -> list[str]:
        node = self.root

        if path != "/":
            parts = path.split("/")
            for part in parts[1:]:
                node = node.children[part]

        if node.is_file:
           file_name = path.split("/")[-1]
           return [file_name]
       
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        parts = path.split("/")

        for part in parts[1:]:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        parts = filePath.split("/")

        for part in parts[1:]:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]

        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        parts = filePath.split("/")

        for part in parts[1:]:
            node = node.children[part]

        return node.content