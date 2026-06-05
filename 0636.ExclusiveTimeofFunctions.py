class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        时间复杂度: O(n)，n 为日志条目数。
        空间复杂度: O(n)。
        """
        # result: 数组里第n个任务的用时
        result = [0] * n
        # stack: 正在运行和等待运行的任务
        stack = []

        for log in logs:
            fn_id, action, timestamp = log.split(":")
            fn_id, timestamp = int(fn_id), int(timestamp)
            # 这里要区分对result和stack的操作
            # 从log里读出的变量名为fn_id, timestamp
            # 从stack里读出的变量名为task_id, task_start_time
            if action == "start":
                if stack:
                    # 当前运行的任务需要暂停,并处理新的任务. 将当前任务运行的时间timestamp - task_start_time 存入result里
                    task_id = stack[-1][0]
                    task_start_time = stack[-1][1]
                    result[task_id] += timestamp - task_start_time
                # 把新任务存到stack顶部
                stack.append([fn_id, timestamp])
            
            else: # 如果action == end

                task_id, task_start_time = stack.pop()
                # 计算所用时间. 比如开始时间3,结束时间5, 总共用了3,4,5 一共3 秒. 所以需要5-3+1=3
                result[task_id] += timestamp - task_start_time + 1
                # 如果stack里还有任务,则会在下一秒自动开始,不要忘了处理
                if stack:
                    stack[-1][1] = timestamp + 1

        return result

