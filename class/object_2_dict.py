def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }


students = [
    create_student("홍길동", 100, 20, 30, 50),
    create_student("김길동", 100, 100, 60, 80),
    create_student("이길동", 45, 60, 80, 10),
    create_student("박길동", 100, 100, 100, 100)
]

print("이름", "총점", "평균", sep='\t')
for student in students:
    score_sum = student['korean'] + student['math'] +\
        student['english'] + student['science']
    score_average = score_sum / 4
    print(student['name'], score_sum, score_average, sep='\t')
