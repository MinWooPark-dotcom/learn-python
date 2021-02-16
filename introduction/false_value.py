# falsy한 값 : None, 0, 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)
print("# if 조건문에 0 넣기")
if 0:
    print('0은 True로 변환되지 않아 이 조건문은 실행되지 않는다.')
else:
    print('0은 falsy한 값이기에 해당 조건문이 실행된다.')
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 falsy해서 실행 안 됨")
else:
    print("빈 문자열은 falsy한 값이라서 실행 됨")
