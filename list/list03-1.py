list_slicing = [0, 1, 2, 3, 4, 5, 6]
list_slicing2 = [0, 1, 2, 3, 4, 5, 6]
# del 리스트명[인덱스], 인덱스 범위 지정 가능
del list_slicing[3:6]  # 3부터 6전까지 삭제 : 3~5
print(list_slicing)  # [0, 1, 2, 6]
# 왼쪽 모두 제거
del list_slicing[:3]  # start 미설정 시 자동으로 0으로 설정(왼쪽 모두 제거) : 0~2
print(list_slicing)  # 6
# 오른쪽 모두 제거
del list_slicing2[3:]  # end 미설정 시 자동으로 끝까지 제거(오른쪽 모두 제거) 3~끝까지
print(list_slicing2)  # [0,1,2]
