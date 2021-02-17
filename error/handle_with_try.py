try:
    number_input_a = int(input('정수 입력> '))
    print('원의 반지름', number_input_a)  # 원의 반지름 13
    print('원의 둘레', 2 * 3.14 * number_input_a)  # 원의 둘레 81.64
    print('원의 넓이', 3.14 * number_input_a * number_input_a)  # 원의 넓이 530.66
except:
    print('error')
