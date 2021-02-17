class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le____(self, value):
        return self.get_sum() <= value.get_sum()


students = [
    Student('홍길동', 100, 100, 20, 30),
    Student('김길동', 20, 50, 70, 100),
    Student('이길동', 10, 10, 30, 100)
]

students_a = Student('홍길동', 100, 100, 20, 30)
students_b = Student('김길동', 20, 50, 70, 100)

print('students_a == students_b', students_a == students_b)
print('students_a != students_b', students_a != students_b)
print('students_a > students_b', students_a > students_b)
print('students_a >= students_b', students_a >= students_b)
print('students_a < students_b', students_a < students_b)
print('students_a <= students_b', students_a <= students_b)

# students_a == students_b False
# students_a != students_b True
# students_a > students_b True
# students_a >= students_b True
# students_a < students_b False
# students_a <= students_b False
