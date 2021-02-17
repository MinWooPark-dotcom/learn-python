try:
    number_input_a = int(input('정수 입력>'))
    print('반지름', number_input_a)
    print('둘레', 2 * 3.14 * number_input_a)
    print('넓이', 3.14 * number_input_a * number_input_a)
except Exception as exception:
    # type(exception) <class 'ValueError'>
    print('type(exception)', type(exception))
    # exception invalid literal for int() with base 10: 'jk'
    print('exception', exception)
