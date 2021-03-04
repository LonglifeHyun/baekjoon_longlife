import sys

def has_he(crds,crd,l,h):
    if h < l:
        return [-1, False]

    mid = (h+l)//2

    if crds[mid] == crd:
        return [mid, True]

    elif crds[mid] < crd:
        return has_he(crds,crd,mid+1,h)

    elif crds[mid] > crd:
        return has_he(crds,crd,l,mid-1)



n = int(input())
sang_cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
d_cards = list(map(int, sys.stdin.readline().rstrip().split()))

sang_cards.sort()

dd_cards = []
for i,card in enumerate(d_cards):
    dd_cards.append((card,i))       # card: 카드에 적힌 정수, i: 해당 카드의 인덱스
# print(dd_cards)

dd_cards.sort(key=lambda x: x[0])
# print(dd_cards)

left_bound = 0

answer = []
for card in dd_cards:
    new_left, ans = has_he(sang_cards,card[0],left_bound,len(sang_cards)-1)
    if new_left != -1:
        left_bound = new_left
    answer.append((ans,card[1]))

answer.sort(key=lambda x: x[1])

for ans in answer:
    if ans[0] == True:
        print("1",end=' ')
    else:
        print("0",end=' ')
