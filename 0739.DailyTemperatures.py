class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        answer = [0] * n

        stack = []

        for i in range(n):
            # stack里的温度是越来越低的
            # 如果当前的温度比stack最上层的温度高,则弹出并计算答案,然后重复这个过程
            while stack and temperatures[i] > temperatures[stack[-1]]:
                past_index = stack.pop()
                answer[past_index] = i - past_index
            
            # 否则就继续推到stack里
            stack.append(i)
        
        return answer
