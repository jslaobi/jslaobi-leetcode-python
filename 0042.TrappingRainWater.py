class Solution:
    def trap(self, height: List[int]) -> int:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        total = 0

        while left < right:
            # 雨水容量由较小的边决定
            if height[left] < height[right]:
                # 如果当前的高度比最大值高则存不下雨水
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                
                right -= 1
        
        return total