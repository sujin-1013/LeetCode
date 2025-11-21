class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        n = len(students)
        num_able_eat = 0
        consistant_uable_eat = 0

        while students:
            remained_students = len(students)
            remained_sandwiches = len(sandwiches)

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                num_able_eat += 1
                consistant_uable_eat = 0
            else:
                last_line = students.pop(0)
                students.append(last_line)
                consistant_uable_eat += 1

            if remained_students < consistant_uable_eat:
                break

        return n - num_able_eat         