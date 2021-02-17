class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print('{}번 째 학생이 생성됨'.format(Student.count))


students = [
    Student('김길동', 100, 100, 20, 30),
    Student('이길동', 100, 100, 90, 30),
    Student('박길동', 100, 100, 20, 50)
]

print()
# print('총 학생 수'.format(Student.count)) 왜 안되지?
