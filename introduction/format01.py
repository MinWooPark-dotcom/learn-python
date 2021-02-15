# 부동 소수점 출력 : {:f}는 소수점 자릿수 디폴트가 6자리
output_a = "{:f}".format(1.234)  # 소수점 세 자리가 더 생김, 총 6자리
output_b = "{:10f}".format(1.234)  # 10칸 만들기
output_c = "{:+10f}".format(1.234)  # 10칸에 부호 추가
output_d = "{:+010f}".format(1.234)  # 10칸에 부호 추가하고 0으로 채우기
output_e = "{:f}".format(123)  # 소수점 여섯 자리가 생김, 총 6자리

# v는 빈칸
print(output_a)  # 1.234000
print(output_b)  # vv1.234000
print(output_c)  # v+1.234000
print(output_d)  # +01.234000
print(output_e)  # 123.000000
