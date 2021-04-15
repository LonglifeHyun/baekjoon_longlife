n = int(input())

"""
# 게임이론으로 그냥 푼거. 72ms.
if n%2==0:
    print("CY")
else:
    print("SK")
"""

# dp로 짠 거
N = int(input())

if N >= 3:
    dp = ['' for _ in range(N+1)]

    dp[1] = 'SK'
    dp[2] = 'CY'
    dp[3] = 'SK'

    for i in range(1, N-2):
        if dp[i] == 'SK':
            dp[i+1] = 'CY'
            dp[i+3] = 'CY'
        else:
            dp[i+1] = 'SK'
            dp[i+3] = 'SK'
    print(dp[N])
else:
    if N == 2:
        print('CY')
    else:
        print('SK')