import collections

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        # 使用滑动窗口, 始终保留两种水果
        left = 0
        max_fruits = 0

        for right, fruit in enumerate(fruits):
            # 将新水果添加进来
            basket[fruit] += 1

            while len(basket) > 2:
                # 使用left指针, 按照添加的顺序依次移除水果, 直到篮子里回到两种水果
                left_fruit = fruits[left]
                basket[left_fruit] -= 1

                # 如果水果数量是0, 则从hashmap中删掉
                if basket[left_fruit] == 0:
                    del basket[left_fruit]

                # left每次都要加1
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits