from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        时间复杂度: O(n)，
        空间复杂度: O(n)。
        """
        # 示例: { 0: [1, 2], 1: [3], 2: [3] }, 0号课程解锁1,2号课程. 1号和2号课程解锁3号课程
        adjacency_list = defaultdict(list)

        # 示例: [0, 1, 1, 2], 0号课程有0个prerequisite, 1号课程有1个,3号课程有2个
        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            # 把course添加到prerequisite里
            adjacency_list[prerequisite].append(course)
            in_degree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            # 首先可以处理那些不需要prerequisite的课
            if in_degree[i] == 0:
                queue.append(i)
        
        result = 0
        while queue:
            curr_course = queue.popleft()
            result += 1

            # 寻找以当前为prerequisite的课并且在in_degree里减1. 注意这里不能简单的完全解锁这些课程, 因为一个课程可能有多个prerequisite
            for neighbor in adjacency_list[curr_course]:
                in_degree[neighbor] -= 1

                # 只有当in_degree是0时, 才能完全解锁这个课程,并加入queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result == numCourses


