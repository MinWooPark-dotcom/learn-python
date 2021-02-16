def power(item):
    return item * item


def under_3(item):
    return item < 3


list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print(output_a)  # <map object at 0x108b98b50>, <map object>를 제너레이터라고 부름
print(list(output_a))  # [1, 4, 9, 16, 25]
print()

output_b = filter(under_3, list_input_a)
print(output_b)  # <filter object at 0x108c05880>, <filter object>를 제너레이터라고 부름
print(list(output_b))  # [1, 2]
