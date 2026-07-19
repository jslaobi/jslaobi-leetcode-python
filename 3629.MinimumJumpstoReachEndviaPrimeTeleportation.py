class Solution:
    def minJumps(self, nums: List[int]) -> int:
        """时间复杂度: O(n + V log V)。
        空间复杂度: O(n + V)。
        """
        n = len(nums)

        if n <= 1:
            return 0

        max_value = max(nums)

        # Smallest Prime Factor (SPF) - 最小质因数 is the lowest prime number that divides that integer without a remainder. For example, the SPF of (15) is (3).
        # 示例: max_value = 10, spf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        spf = list(range(max_value + 1))
        # 如果max_value小于2, 则找不到这样的质数,跳过计算
        if max_value >= 2:
            # 从2到max_value的平方根
            for i in range(2, int(max_value ** 0.5) + 1):
                # 如果spf[i] == i, i是质数
                if spf[i] == i:
                    # 从i的平方开始到max_value,示例: i=2, 从2x2开始每次递进2. 比如2x2, 2x3... 
                    # 将他们的spf[j]都设置为2, 比如spf[4] = 2, spf[6] = 2...
                    for j in range(i*i, max_value+1, i):
                        if spf[j] == j:
                            spf[j] = i
            
        # buckets示例:
        # nums = [8, 7, 14, 21, 6]
        # buckets = {
        #     2: [0, 2, 4],   可以整除2的数的index
        #     3: [3, 4]       可以整除3的数的index
        # }
        buckets = collections.defaultdict(list)
        for i, value in enumerate(nums):
            if value < 2:
                continue
            
            x = value
            while x > 1:
                # 示例 i = 7, x = 24
                # 示例 p = spf[24] = 2
                p = spf[x]
                # 示例 buckets[2].append(7)
                buckets[p].append(i)
                # 这里处理完了2, 我们要把所有的2都移除, 所以只要x % 2 == 0, 我们就继续从x中整除2,直到只剩下3, x=3
                # 之后继续循环, p = spf[3], buckets[3].append(7)
                while x % p == 0:
                    x //= p

        
        queue = deque()
        # 加入index 0
        queue.append(0)
        visited = [False] * n
        visited[0] = True
        jumps = 0

        while queue:
            for i in range(len(queue)):
                curr_index = queue.popleft()
                if curr_index == n - 1:
                    return jumps
                # 选项1: Adjacent Step, 前后移动1
                for next_index in (curr_index - 1, curr_index + 1):
                    if 0 <= next_index < n and not visited[next_index]:
                        visited[next_index] = True
                        queue.append(next_index)
                
                # 选项2: Prime Teleportation, 传送
                value = nums[curr_index]

                # 如果spf[value] == val, 则value是质数,可传送
                if value >= 2 and spf[value] == value:
                    if value in buckets:
                        for next_index in buckets[value]:
                            if not visited[next_index]:
                                visited[next_index] = True
                                queue.append(next_index)
                        # 在BFS里, 第一次接触buckets[value]就是最短路径, 所以删除掉避免以后再试,因为后面不可能出现更短的路径, 避免超时
                        del buckets[value]

            jumps += 1
        
        return -1
                


