import random

class RandomizedSet:

    def __init__(self):
        # 将值对应的index存在hashmap里
        self.val_to_index = {}
        # 将真正的值存在数组里,这样随机取数就可以达到O(1)
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        remove_index = self.val_to_index[val]
        last_value = self.values[-1]

        # 为了删除时不需要挪动删除元素之后的所有元素,我们先将要删除的元素和最后一个元素互换,然后删除最后一个元素
        # 实际上也不需要互换, 只需要把要删除的元素的index的值更新为最后一个元素,然后删除最后一个元素即可
        self.values[remove_index] = last_value
        # 同理更新hashmap
        self.val_to_index[last_value] = remove_index

        # 删除最后一个元素
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()