# 사용자 입력: input(), 명령 프롬프트에서 사용자로부터 데이터를 입력받을 때 사용

input_value = input('여기 명령프롬프트에서 값을 입력하면 문자열 형태로 리턴해줌')  # abc
print(input_value)  # abc, 리턴되는 값은 무조건 문자열 자료형

# 문자열 -> 숫자로 바꾸기 (cast) : input() 함수의 입력 자료형은 항상 문자열이기 때문에 문자열을 숫자로 변환해야 숫자 연산에 활용 가능. 영어로는 cast라고 함.

int_value = int(input_value)
print(type(int_value))  # <class 'int'>

float_value = float(input_value)
print(type(float_value))  # <class 'float'>

print(type(input_value))  # <class 'str'>

int_to_str = str(int_value)
print(type(int_to_str))  # <class 'str'>

# swap

a = input('a입력')  # is a
b = input('b입력')  # is b

print(a, b)  # is a is b
[a, b] = [b, a]
print(a, b)  # is b is a
