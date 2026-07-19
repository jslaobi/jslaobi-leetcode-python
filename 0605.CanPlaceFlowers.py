class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        if n == 0:
            return True

        length = len(flowerbed)
        for i in range(length):
            # 找到一个空位置
            if flowerbed[i] == 0:
                empty_left = (i==0) or flowerbed[i-1] == 0
                empty_right = (i==length-1) or flowerbed[i+1] == 0

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
            
            if n <= 0:
                return True
        
        return False