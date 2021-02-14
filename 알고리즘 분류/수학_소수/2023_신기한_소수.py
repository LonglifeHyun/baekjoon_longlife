def is_prime(v):
    for i in range(2, int(v**0.5)+1):
        if v % i ==0:
            return False
    return True

n = int(input())

sz = [[] for _ in range(n+1)]

for i in range(2, 10):
    if is_prime(i):
        sz[1].append(str(i))

for i in range(2,n+1):
    for j in sz[i-1]:
        new_p = j
        for k in range(1,10):
            new_p += str(k)
            if is_prime(int(new_p)):
                sz[i].append(new_p)
            else:
                new_p = j

for _ in sz[len(sz)-1]:
    print(_)
