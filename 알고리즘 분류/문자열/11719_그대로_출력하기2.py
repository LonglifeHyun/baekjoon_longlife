"""
# 콘솔용
import sys
input = sys.stdin.readline

lst = []
while True:
    try:
        lst.append(input().rstrip())
        print(lst)
        for _ in lst:
            print(_)
    except:
        break

"""

# 서버 제출용
while True:
    try:
        print(input())
    except:
        break