from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        in_degree = [0] * numCourses
        path = []
        queue = deque()

        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
            in_degree[course] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            curr_course = queue.popleft()
            path.append(curr_course)

            for neighbor in adjacency_list[curr_course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(path) == numCourses:
            return path
        else:
            return []
        