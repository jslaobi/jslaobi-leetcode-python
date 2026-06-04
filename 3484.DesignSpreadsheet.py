class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        # 这里直接删除而不是将值设置为0是为了节省空间
        if cell in self.cells:
            del(self.cells[cell])

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split('+')

        if not left[0].isdigit():
            left = self.cells.get(left, 0)
        
        if not right[0].isdigit():
            right = self.cells.get(right, 0)
        
        return int(left) + int(right)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)