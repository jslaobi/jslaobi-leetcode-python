class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        # 按照距离由大到小排序(距离终点近的在前)
        # zip: 将position和speed合并, 例如:
        # names = ["Alice", "Bob", "Charlie"]
        # ages = [25, 30, 35]
        # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for car_position, car_speed in cars:
            time = (target - car_position) / car_speed
            stack.append(time)

            # stack[-1]是本轮新加入的车, stack[-2]是之前领先的车
            # 如果能在终点前追上之前的车,则到达终点的时间一定比之前的车的时间少, 即stack[-1] <= stack[-2]
            # 但是由于不能超过前车, 所以到达终点的时间应该相等. 从stack中pop掉, 完成“合并”
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        
        return len(stack)

