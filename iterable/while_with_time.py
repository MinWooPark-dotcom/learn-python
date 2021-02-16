import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복".format(number))
# 5초 동안 24944676번 반복 2천 4백만..
