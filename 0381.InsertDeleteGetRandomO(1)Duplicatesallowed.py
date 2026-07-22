from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        # 使用一个array和一个hashmap, map的key是数值,value是数值所出现的所有位置,存为一个set
        self.vals = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        # 因为添加的值在最后,所以index是len(self.vals) - 1
        self.indices[val].add(len(self.vals) - 1)

        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        
        # 弹出index列表中的一个,作为要删除的index
        remove_index = self.indices[val].pop()

        # 取最后一个元素的val和index,跟要删除的元素交换
        last_val = self.vals[-1]
        last_index = len(self.vals) - 1

        # 将最后一个元素的数值放到要删除的元素, 然后删除最后一个元素
        self.vals[remove_index] = last_val

        # 更新hashmap
        self.indices[last_val].add(remove_index)
        self.indices[last_val].remove(last_index)
        
        self.vals.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()