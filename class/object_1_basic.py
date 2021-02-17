students = [
    {"name": "홍길동", "korean": 100, "math": 30, "english": 100, "science": 100},
    {"name": "김길동", "korean": 10, "math": 100, "english": 60, "science": 100},
    {"name": "이길동", "korean": 100, "math": 10, "english": 100, "science": 20},
    {"name": "박길동", "korean": 100, "math": 100, "english": 70, "science": 50},
]

print('이름', '총점', '평균', sep='\t')

for student in students:
    score_sum = student["korean"] + student["math"] + \
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student['name'], score_sum, score_average, sep='\t')

# 이름    총점    평균
# 홍길동  330     82.5
# 김길동  270     67.5
# 이길동  230     57.5
# 박길동  320     80.0
