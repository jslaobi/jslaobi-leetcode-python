import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # small是max_heap, large是min_heap, 这样我们可以取small的顶部,或者small的顶部和large的顶部的平均值,来计算median
        small = []
        large = []
        
        delayed = defaultdict(int)
        result = []

        # 第一个window
        for i in range(k):
            # 如果比small里最大的值要小, 先push到small里
            if not small or nums[i] < -small[0]:
                heapq.heappush(small, -nums[i])
            else:
                heapq.heappush(large, nums[i])
            
            # 然后再平衡, 最多允许small比large的长度大1
            if len(small) > len(large) + 1:
                heapq.heappush(large, -heapq.heappop(small))
            # 同时还要检查如果large的长度大于small,也要再平衡
            elif len(large) > len(small):
                heapq.heappush(small, -heapq.heappop(large))
        
        def get_median():
            if k % 2 == 1:
                return -small[0]
            else:
                return (-small[0] + large[0]) / 2.0
        
        result.append(get_median())
    
        # 上面是第一个窗口, 接下来滑动窗口
        for i in range(k, len(nums)):
            out_num = nums[i - k]
            in_num = nums[i]

            delayed[out_num] += 1

            # 如果balance小于0, 应该向small再平衡并添加, 大于0向large再平衡并添加
            balance = 0

            # 1. 根据out_num更新balance
            if out_num <= -small[0]:
                balance -= 1
            else:
                balance += 1
            
            # 2. 处理in_num
            if small and in_num <= -small[0]:
                balance += 1
                heapq.heappush(small, -in_num)
            else:
                balance -= 1
                heapq.heappush(large, in_num)
            
            # 3. 根据balance重新平衡
            if balance < 0:
                heapq.heappush(small, -heapq.heappop(large))
            elif balance > 0:
                heapq.heappush(large, -heapq.heappop(small))

            # 4. 如果delayed里有任何元素, 从相应的heap中清理掉
            while small and delayed[-small[0]] > 0:
                delayed[-small[0]] -= 1
                heapq.heappop(small)
                
            while large and delayed[large[0]] > 0:
                delayed[large[0]] -= 1
                heapq.heappop(large)
            
            # 5. 计算median, 添加到result
            result.append(get_median())
        
        return result

