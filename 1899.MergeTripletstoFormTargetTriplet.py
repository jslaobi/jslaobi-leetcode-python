class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        # 我们找的不是三数之和等于target,而是三个数完全于target的三个数相等
        # 任何大于target的数都不符合条件,直接去掉. 小于target的数可以用于合并,但是最终我们我们要找的,就是1,2,3号位是否有traget的3个数
        found_x = False
        found_y = False
        found_z = False

        x, y, z = target

        for a, b, c in triplets:
            # 这一步很关键, 检查当前triplet是否小于等于target. 如果任何一个数大于,即使有符合条件的,也不能采用
            if a <= x and b <= y and c <= z:
                if a == x:
                    found_x = True
                if b == y:
                    found_y = True
                if c == z:
                    found_z = True
        
        return found_x and found_y and found_z

