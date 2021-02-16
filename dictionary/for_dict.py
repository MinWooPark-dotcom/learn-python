# for 반복문: 딕셔너리와 함께 사용하기
# for 키 변수 in 딕셔너리:
#    코드
pets = [
    {'name': '구름', 'age': 5},
    {'name': '하늘', 'age': 5}
]

for key in pets:
    print(key['name'], key['age'], '살')

numbers = [1, 1, 1, 2, 2, 3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
