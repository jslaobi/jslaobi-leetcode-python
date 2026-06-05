class Solution:
    def countPrimes(self, n: int) -> int:
        """
        时间复杂度: O(n log log n)，n 为输入值。
        空间复杂度: O(n)。
        """
        # 0和1不是质数
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        # 因为接下来要进行平方操作,所以只需要循环到根号n
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # 比如2是质数, 那么2的倍数就都不是质数. 从2*2=4开始,更新所有的倍数比如2*3=6,2*4=8的值为False
                # 从i的平方开始,到n,每隔i个数字更新一次
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return is_prime.count(True)