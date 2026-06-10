class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 先把所有的酒倒进第一个杯子
        row = [poured]

        # 从第二层(r=1)开始计算到目标query_row层
        for r in range(1, query_row + 1):
            # 比如第二层,r=1, 有r+1=2个杯子
            next_row = [0.0] * (r + 1)

            for c in range(r):
                # 如果当前row的杯子满了,则会流到next_row
                if row[c] > 1.0:
                    excess = row[c] - 1.0
                    # 这里要一个杯子一个杯子的处理,而且要用+=, 而不是层内所有杯子均分. 因为流到每个杯子的量不一样,从题目图示中也可以看到中间的杯子流入的酒多
                    next_row[c] += excess / 2.0
                    next_row[c + 1] += excess / 2.0
            
            row = next_row
        # 杯子最多只能容纳1.0
        return min(1.0, row[query_glass])