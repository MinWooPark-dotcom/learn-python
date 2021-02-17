from primePy import primes

# upto 메서드 예제
primes_to_10 = primes.upto(10)
print("10까지의 소수 리스트:", primes_to_10)
primes_to_100 = primes.between(100, 1000)
print("100까지의 소수 리스트:", len(primes_to_100))
print()  # 띄어쓰기를 위해서

# 10까지의 소수 리스트: [2, 3, 5, 7]
# 100까지의 소수 리스트: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# first 메서드 예제
first_5_primes = primes.first(5)
print("처음 5개 소수 리스트:", first_5_primes)
first_10_primes = primes.first(10)
print("처음 10개 소수 리스트:", first_10_primes)
print()

# 처음 5개 소수 리스트: [2, 3, 5, 7, 11]
# 처음 10개 소수 리스트: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# check 메서드 예제
print("15는 소수인가요?", primes.check(15))
print("277은 소수인가요?", primes.check(277))
print()

# 15는 소수인가요? False
# 277은 소수인가요? True
