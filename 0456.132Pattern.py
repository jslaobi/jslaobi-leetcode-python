import math

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        stack = []

        two = -math.inf

        for i in range(n-1, -1, -1):
            curr_num = nums[i]

            # 如果当前数字小于two, 则我们找到了“1”，直接成功！
            if curr_num < two:
                return True
            
            # stack里存的其实是【未来可能成为“2”的候选人】。
            # 如果当前的数(curr_num)大于栈顶，说明当前的数可以扮演“3”！
            # 我们用这个“3”去不断pop栈里的候选人，把能找到的最大的数正式册封为“2”(赋值给two)。
            while stack and curr_num > stack[-1]:
                two = stack.pop()
                
            # 无论刚才发生了什么，当前的数处理完后，都要进栈。
            # 因为继续往左走的话，它也有可能成为别人眼里的“2”。
            stack.append(curr_num)

        return False
