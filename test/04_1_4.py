list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

# result = []

# for list in list_of_list:
#     for el in list:
#         # global result
#         # result = []
#         result.append(el)

# print(result)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

for line in list_of_list:
    for item in line:
        print(item)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9