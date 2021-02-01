import math

t = int(input())
answer = []

for i in range(t):
    ans = 0

    ins = [int(j) for j in input().split()]
    jo = [ins[0],ins[1]]
    baek = [ins[3],ins[4]]
    r1, r2 = ins[2], ins[5]

    if (jo[0]==baek[0] and jo[1]==baek[1]):
        if r1 == r2:
            ans = -1        # 두 원이 일치
        else:
            ans = 0         # 두 원이 중심 일치, 반지름 다름
    else:
        jo2baek = math.sqrt(((jo[0] - baek[0])**2) + ((jo[1] - baek[1])**2))
        # jo2baek = (((jo[0] - baek[0]) ** 2) + ((jo[1] - baek[1]) ** 2))**0.5

        if r1 + jo2baek == r2  or r2 + jo2baek == r1:
            ans = 1         # 두 원이 내접
        elif r1 + jo2baek < r2 or r2 + jo2baek < r1:
            ans = 0         # 한 원이 다른 원 내부에 존재 (중심도 다르고, 내접도 아님)
        elif float(r1+r2) < jo2baek:
            ans = 0         # 두 원이 만나지 않음
        elif float(r1+r2) == jo2baek:
            ans = 1         # 두 원이 외접
        else:
            ans = 2         # 두 원이 교차

    answer.append(ans)

for ans in answer:
    print(ans)