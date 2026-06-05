class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        """
        时间复杂度: O(n log n)，n 为小行星数量。
        空间复杂度: O(1)。
        """
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False
            else:
                mass += asteroid
        
        return True