class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        stack = []

        for asteroid in asteroids:
            survived = True

            while stack and stack[-1] > 0 and asteroid < 0:
                # 如果当前行星比之前的大,摧毁之前的行星并且继续
                if stack[-1] < abs(asteroid):
                    stack.pop()
                # 如果两者相等,摧毁双方,终止循环
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    survived = False
                    break
                # 如果当前行星比之前的小,摧毁当前行星并且继续(不影响stack)
                else:
                    survived = False
                    break
            
            # 如果当前行星存活,或者stack里没有元素,或者当前行星不是负数,添加到stack里
            if survived == True:
                stack.append(asteroid)
        
        return stack
