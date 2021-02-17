try:
    number_input_a = int(input('정수 입력> '))
    print('원의 반지름:', number_input_a)
    print('원의 둘레', 2 * 3.14 * number_input_a)
    print('원의 넓이', 3.14 * number_input_a * number_input_a)
except:
    print('정수를 입력해야 돼')
else:
    print('예외 없음')
finally:
    print('마지막에 무조건 실행')
