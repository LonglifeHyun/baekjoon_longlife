x, y = map(int, input().split())

fst_z = int((100.0*y)/x)

if fst_z >= 99:
    print(-1)
else:
    num = 0
    low, high = 1, 1000000000
    while low <= high:
        mid = (low+high)//2

        new_z = int((100.0*(y+mid))/(x+mid))
        if new_z > fst_z:
            num = mid
            high = mid - 1
        else:
            low = mid + 1
    print(num)