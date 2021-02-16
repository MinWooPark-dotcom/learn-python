number = input("정수 입력>")
print(type(number))  # <class 'str'>
number = int(number)

if number > 0:
    print('양수')
elif number < 0:
    print('음수')
else:
    print('0입니다.')
