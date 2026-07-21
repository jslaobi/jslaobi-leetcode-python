from collections import defaultdict, deque
from itertools import groupby

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """时间复杂度: O(m log m + m + n)。
        空间复杂度: O(m + n)。
        """
        # meetings[i] = [xi, yi, timei], 按照会议开始时间排序
        meetings.sort(key=lambda x:x[2])

        know_secret = set()
        # 根据题目描述, Person 0和firstPerson已经知道了秘密
        know_secret.add(0)
        know_secret.add(firstPerson)

        # groupby(meetings, key=lambda x: x[2]): 按照时间将数据分组
        # 示例: meetings = [
        #    [1, 2, 5],  
        #    [3, 4, 5],  
        #    [1, 5, 8], 
        #    [2, 6, 8]  
        #]
        # 分组后: time = 5, group = [ [1, 2, 5], [3, 4, 5], time = 8, group = [ [1, 5, 8], [2, 6, 8] ]

        for time, group in groupby(meetings, key=lambda x:x[2]):
            graph = defaultdict(list)
            people_involved = set()

            for person1, person2, _ in group:
                graph[person1].append(person2)
                graph[person2].append(person1)
                people_involved.add(person1)
                people_involved.add(person2)
            
            queue = deque()
            for person in people_involved:
                if person in know_secret:
                    queue.append(person)
            
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in know_secret:
                        know_secret.add(neighbor)
                        queue.append(neighbor)
        
        return list(know_secret)
