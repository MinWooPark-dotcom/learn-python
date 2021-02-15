# 의미 없는 소수점
#  제거하기 : 52와 52.0은 자료형이 다르므로 다른 값으로 출력함. 의미없는 0을 제거하기 위해 사용하는 방법
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)  # 52.0
print(output_b)  # 52
