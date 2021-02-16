def print_n_times(value, n=2):
    # n번 반복
    for i in range(n):
        print(value)


# 함수 선언 시 매개변수는 2개인데 호출할 때는 매개변수가 1개임, 이럴 때 기본 매개변수의 기본 값인 2가 들어감
print_n_times('hi')
# hi
# hi
