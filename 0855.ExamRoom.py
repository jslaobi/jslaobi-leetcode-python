import bisect

class ExamRoom:

    def __init__(self, n: int):
        """
        时间复杂度: seat O(n)，leave O(n)。
        空间复杂度: O(n)。
        """
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            # 如果第一个座位有人,max_dist就是0. 如果第一个座位没人,则假设坐在第一个座位. 比如第4个座位有人,则max_dist就是3
            max_dist = self.students[0]
            student = 0

            for i in range(1, len(self.students)):
                prev_student = self.students[i - 1]
                current_student = self.students[i]

                current_dist = (current_student - prev_student) // 2
                if current_dist > max_dist:
                    max_dist = current_dist
                    # 如果找到一个更好的座位, 则更新最大距离,并且把学生放到中间
                    student = prev_student + current_dist

            # 检查最后一个座位
            if self.n - 1 - self.students[-1] > max_dist:
                max_dist = self.n - 1 - self.students[-1]
                student = self.n - 1
            
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)