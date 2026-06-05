class TextEditor:

    def __init__(self):
        """
        时间复杂度: addText/deleteText/cursorLeft/cursorRight O(k)，k 为操作字符数。
        空间复杂度: O(n)，n 为当前文本长度。
        """
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(list(text))

    def deleteText(self, k: int) -> int:
        chars = 0
        if k > 0 and len(self.left) > 0:
            chars = min(k, len(self.left))
            del self.left[-chars:]
        return chars
    
    def cursorLeft(self, k: int) -> str:
        if k > 0 and len(self.left) > 0:
            chars = min(k, len(self.left))
            # 比如cursor, left = "cur" right = "ros", 因为stack每次弹出最右边的元素
            #  self.left[-2:] = ur, reversed之后就是ru, right.extend之后就是left = "c", right = "rosru"
            self.right.extend(reversed(self.left[-chars:]))
            del self.left[-chars:]
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        if k > 0 and len(self.right) > 0:
            chars = min(k, len(self.right))
            # 比如cursor, left = "cur" right = "ros", 因为stack每次弹出最右边的元素
            #  self.right[-2:] = os, reversed之后就是so, left.extend之后就是left = "curso", right = "r"
            self.left.extend(reversed(self.right[-chars:]))
            del self.right[-chars:]

        return "".join(self.left[-10:])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)