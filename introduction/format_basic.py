# format() : 숫자를 문자열로 변환, 중괄호를 포함한 문자열 뒤에 마침표를 찍고 format 함수를 사용, 중괄호 개수와 매개변수의 개수는 반드시 일치해야 함
str_to_num = "{}".format(10)
print(str_to_num)  # 10
print(type(str_to_num))  # <class 'str'>

format_a = "{} {} {}".format(1, '문자열', True)
print(format_a)  # 1 문자열 True => 숫자 이외의 자료형도 적용 가능
print(type(format_a))  # <class 'str'>

# 정수
only_integer = "{:d}".format(10)  # {:d} : int 자료형 정수를 출력하겠다는 뜻
print(only_integer)

# 특정 칸에 출력
specific_space = "{:5d}".format(10)  # {:xd} : x칸 띄고 int 자료형 정수를 출력하겠다는 뜻
print(specific_space)

# 빈칸을 0으로 채우기
# 5칸을 잡고 뒤에서부터 10넣고 앞의 빈 곳을 0으로 채움
fill_blanks_zero_positive = "{:05d}".format(10)

# 부호가 있을 땐 맨 앞자리를 부호로 채우고 위와 동일
fill_blanks_zero_negative = "{:05d}".format(-10)

print(fill_blanks_zero_positive)
print(fill_blanks_zero_negative)

# 기호 붙여 출력하기
output_positive = "{:+d}".format(10)
output_negative = "{:+d}".format(-10)
output_blank = "{: d}".format(10)
output_blank_negative = "{: d}".format(-10)

print(output_positive)  # +10
print(output_negative)  # -10
print(output_blank)  # 10
print(output_blank_negative)  # -10

print()

output_a = "{:+5d}".format(10)
output_b = "{:+5d}".format(-10)
output_c = "{:5d}".format(-10)  # '+'없이 {:5d} 가능
output_d = "{:=+5d}".format(10)  # 기호와 공백을 조합할 때는 = 기호를 앞에 붙일 수 있음
output_e = "{:=+5d}".format(-10)  # '+'없이 {:=5d} 가능
output_f = "{:+05d}".format(10)
output_g = "{:+05d}".format(-10)  # '+'없이 가능

# v는 빈칸
print(output_a)  # vv+52
print(output_b)  # vv-52
print(output_c)  # vv-52
print(output_d)  # +vv10
print(output_e)  # -vv10
print(output_f)  # +0010
print(output_g)  # -0010
