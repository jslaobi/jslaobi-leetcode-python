class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)
        # 比如2位数乘2位数的结果需要一个最多4位数组(2+2), 99 * 99 = 9801
        result = [0] * (m + n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                multiplication = int(num1[i]) * int(num2[j])

                # 这里是在模拟相乘时的计算和进位规则, 可以了解一下原理,但是推荐只需要记住这些步骤就好
                p1 = i + j
                p2 = i + j + 1
                total_sum = multiplication + result[p2]

                # 注意一个是=, 一个是+=
                result[p2] = total_sum % 10
                result[p1] += total_sum // 10

        # 最后去掉开头的0, start决定非0的起始位置
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1 

        # map(str,)是把[1,2,3]转换成["1","2","3"]
        return "".join(map(str, result[start:]))
