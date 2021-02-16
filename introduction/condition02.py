number = input('정수 입력>')
last_character = number[-1]

if last_character in '02468':
    print('짝수')
else:
    print('홀수')
