user_input_a = input("정수 입력> ")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print('원의 반지름', number_input_a)  # 원의 반지름 13
    print('원의 둘레', 2 * 3.14 * number_input_a)  # 원의 둘레 81.64
    print('원의 넓이', 3.14 * number_input_a * number_input_a)  # 원의 넓이 530.66
else:
    print('정수를 입력하지 않음')
