# 소수점 아래 자릿수 지정하기
output_a = "{:15.3f}".format(52.273)  # 15칸을 잡고 소수점을 3자리, 자동으로 반올림
output_b = "{:15.2f}".format(52.273)  # '' 소수점을 2자리, 자동으로 반올림
output_c = "{:15.1f}".format(52.273)  # '' 소수점을 1자리, 자동으로 반올림

print(output_a)  # vvvvvvvvv52.273
print(output_b)  # vvvvvvvvvv52.27
print(output_c)  # vvvvvvvvvvv52.3
