import sys

def make_primes():
    is_prime = [True for _ in range(1000+1)]
    is_prime[0], is_prime[1] = False, False
    primes = []

    for i in range(2,len(is_prime)):
        if is_prime[i] == True:
            primes.append(i)
            for j in range(i+1,len(is_prime)):
                if is_prime[j] == True and j%i==0:
                    is_prime[j] = False
    return primes


n = int(input())
nums = [int(i) for i in sys.stdin.readline().rstrip().split()]

primes = make_primes()

cnt = 0
for num in nums:
    if num in primes:
        cnt += 1
print(cnt)
