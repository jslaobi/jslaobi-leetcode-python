class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        result = []

        fizz_buzz_map = {
            3: "Fizz",
            5: "Buzz"
        }

        for i in range(1, n+1):
            curr_string = []

            for divisor, word in fizz_buzz_map.items():
                # 如果能被15整除,那么就能被3和5整除,所以会按照循环输出FizzBuzz,不需要特殊处理
                if i % divisor == 0:
                    curr_string.append(word)
                
            # 如果没输出任何单词,按照题目要求输出index
            if not curr_string:
                curr_string.append(str(i))
            
            result.append("".join(curr_string))
        
        return result