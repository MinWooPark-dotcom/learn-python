# 값으로 제거하기 : remove - 리스트.remove(값)
list_c = [1, 2, 1, 2]
list_c.remove(2)
# [1, 1, 2] => remove함수로 지정한 값이 여러 개라면 가장 먼저 발견되는(왼쪽에 있는) 값 하나만 제거
print(list_c)

# 모두 제거하기 : clear - 리스트.clear()
list_d = [1, 2, 3, 4, 5]
list_d.clear()
print(list_d)  # []
