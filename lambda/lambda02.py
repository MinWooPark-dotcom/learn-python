# 람다 : lambda 매개변수 : 리턴값
# def power(x): return x * x
# def under_3(x): return x < 3

list_input_a = [1, 2, 3, 4, 5]

# output_a = map(power, list_input_a)
output_a = map(lambda x: x * x, list_input_a)
print(output_a)  # <map object at 0x104b8f730>
print(list(output_a))  # [1, 4, 9, 16, 25]
print()

# output_b = filter(under_3, list_input_a)
output_b = filter(lambda x: x < 3, list_input_a)
print(output_b)  # <filter object at 0x104b8fa60>
print(list(output_b))  # [1, 2]
