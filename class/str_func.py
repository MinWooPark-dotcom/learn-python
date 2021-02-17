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


students = [
    Student('홍길동', 100, 100, 20, 30),
    Student('김길동', 20, 50, 70, 100),
    Student('이길동', 10, 10, 30, 100)
]

print('이름', '총점', '평균', sep='\t')
for student in students:
    print(str(student))  # str() 함수의 매개변수로 넣으면 student의 __str__() 함수가 호출됨
