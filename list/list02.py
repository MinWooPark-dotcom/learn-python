# Declear list
list_a = [1, 2, 3]


# 리스트 뒤에 요소 추가
list_a.append(4)
list_a.append(5)
print(list_a)  # [1, 2, 3, 4, 5], 원본에서 바뀜 => mutable

list_a.insert(1, 10)  # 1번 째에 10넣고 기존 요소들 뒤로 미룸
print(list_a)  # [1, 10, 2, 3, 4, 5]

# 한 번에 여러 요소를 추가하고 싶을 때 - extend()
list_a.extend(['a', 'b', 'c'])
print(list_a)  # [1, 10, 2, 3, 4, 5, 'a', 'b', 'c']
