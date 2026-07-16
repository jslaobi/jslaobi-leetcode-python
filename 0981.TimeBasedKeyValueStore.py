from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 注意这里不是=是append, 因为每次添加新的数值
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        history = self.store[key]

        index = bisect.bisect_right(history, timestamp, key=lambda x: x[0])

        # 如果index是0, 则没有比请求的timestamp更早的数据, 返回空字符串
        if index == 0:
            return ""
        
        # 因为是bisect_right, 所以取index - 1
        return history[index - 1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)