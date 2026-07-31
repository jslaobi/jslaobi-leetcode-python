class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        max_area = 0
        # stack里的高度只能升序
        stack = []

        for i, h in enumerate(heights):
            start = i

            # 如果stack顶端的柱子比当前的高,则不满足stack升序的条件
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                # 因为stack里是升序的, 所以计算面积时可以用当前高度当作最低高度计算,乘以(i - index)
                max_area = max(max_area, height * (i - index))

                # 当前的这个短柱子的高度,也可以向前延伸来计算面积. 比如stack里是5,6, 新来的是2. 2最短,可以用来乘以5,6,2的宽
                # 把当前的index(原来5所在的index)记录给start, 然后推到stack里,将来会被用来index计算宽度(i - index)
                start = index

            stack.append((start, h))
        
        # 最后stack里可能还有一些剩余的柱子, 因为stack是升序, 所以用(len(heights) - i)作为宽度
        for i, height in stack:
            max_area = max(max_area, height * (len(heights) - i))

        return max_area



