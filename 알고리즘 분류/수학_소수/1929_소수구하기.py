def make_primes(num):
    che = [True for _ in range(num+1)]
    che[0], che[1] = False, False
    for i in range(2, len(che)):
        if che[i] == True:
            for j in range(i+i,len(che),i):
                che[j] = False
    return che

m, n = map(int, input().split())
is_prime = make_primes(n)
for i in range(m, n+1):
    if is_prime[i]:
        print(i)