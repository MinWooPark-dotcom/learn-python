list_a = [0, 1, 2, 3, 4, 5]
list_slicing = [0, 1, 2, 3, 4, 5, 6]
# del 리스트명[인덱스], 인덱스 범위 지정 가능
del list_a[1]
print(list_a)  # [0,2,3,4,5]
# 리스트명.pop(인덱스)
list_a.pop(2)
print(list_a)  # [0,2,4,5]
# pop함수에 인자 입력 안했을 시, 자동으로 -1 들어가는 것으로 취급
list_a.pop()  # == list_a.pop(-1)
print(list_a)  # [0,2,4]
