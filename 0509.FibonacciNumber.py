class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        prev2 = 0
        prev1 = 1

        for _ in range(2, n + 1):
            curr = prev1 + prev2

            prev2 = prev1
            prev1 = curr
        
        # 最后一轮循环将curr的值赋值给prev1, 所以prev1就是最后curr的值,所以返回prev1
        return prev1
        
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        
        # return self.fib(n - 1) + self.fib(n - 2)