class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        n = len(heights)
        result = []
        max_height = 0

        # 从右往左遍历, 如果当前建筑物的高度大于max_height, 则说明它可以看到海景
        for i in range(n-1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]

        # 反转结果数组, 因为我们是从右往左遍历的
        return result[::-1]  