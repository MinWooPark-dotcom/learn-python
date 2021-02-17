import random

# random(): 0.0 <= x < 1.0 사이의 float를 리턴
print(random.random())  # 0.36286472075087683

# uniform(min, max): 지정한 범위 사이의 float를 리턴
print(random.uniform(10, 20))  # 11.897634576525968

# randrange(): 지정한 범위의 int를 리턴
print(random.randrange(10))  # 9

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택
print(random.choice([1, 2, 3, 4, 5]))  # 5

# shuffle(list): 리스트의 요소들을 랜덤하게 섞음
print(random.shuffle([1, 2, 3, 4, 5]))  # None

# sample(list,k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
print(random.sample([1, 2, 3, 4, 5], k=2))  # [3,2]
