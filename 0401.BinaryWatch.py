class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        时间复杂度: O(1)。
        空间复杂度: O(1)。
        """
        # 对于每个LED, 我们选择on或者off,使用backtrack来解
        leds = [8,4,2,1,32,16,8,4,2,1]
        result = []
        curr_path = []

        def backtrack(start_index: int):
            if len(curr_path) == turnedOn:
                hours = 0
                minutes = 0

                for i in curr_path:
                    if i < 4:
                        hours += leds[i]
                    else:
                        minutes += leds[i]
                # 如果出现越界的数字,则不能添加  
                # 如果分钟是个位数,在前面添加0 
                if hours < 12 and minutes < 60:
                    result.append(f"{hours}:{minutes:02d}")

            for i in range(start_index, 10):
                curr_path.append(i)
                backtrack(i + 1)
                curr_path.pop()

        backtrack(0)
        
        return result
            
