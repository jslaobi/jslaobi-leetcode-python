class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n
        stack = []
        # 从后向前处理高度
        for i in range(n-1, -1, -1):
            visible_count = 0

            # 如果当前的高度比后面的那个人要高, 那么能看到后面的那个人,并且还能继续向后看
            while stack and heights[i] > stack[-1]:
                stack.pop()
                visible_count += 1

            # 如果当前的高度不比后面的那个人高, 那么能看到后面的那个人,但是看不到再之后了
            if stack and heights[i] <= stack[-1]:
                visible_count += 1
            
            result[i] = visible_count

            # 每轮把当前的人加入stack
            stack.append(heights[i])
        
        return result