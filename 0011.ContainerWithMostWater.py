class Solution:
    def maxArea(self, height: List[int]) -> int:
        """双指针求最大水容器。

        时间复杂度: O(n)，n 为高度数组长度。
        空间复杂度: O(1)，只使用常数级额外变量。
        """
        left, right = 0, len(height) - 1
        max_area = 0
        # 从两头开始，不停的寻找最大面积
        while(left < right):
            # 对水的容量是由最短的那根木板决定的
            current_height = min(height[left], height[right])
            area = (right - left) * current_height
            # 比较更新最大面积
            max_area = max(max_area, area)
            
            # 如果右边的木板更短，那么就移动右指针，期待能找到一个更长的木板来增加容量；
            # 反之，如果左边的木板更短，那么就移动左指针，期待能找到一个更长的木板来增加容量。
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area