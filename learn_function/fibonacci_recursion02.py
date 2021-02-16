counter = 0


def fibonacci(n):
    print('fibonacci({})를 구합니다.'.format(n))
    global counter  # 함수 외부의 변수를 참조하기 위해
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)

print('fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.'.format(counter))
# fibonacci(10) 계산에 활용된 덧셈 횟수는 109번 입니다.
