n = int(input())

cards = [_ for _ in range(n,0,-1)]

while len(cards)>1:
    print(cards[-1],end=" ")
    del cards[-1]
    cards.insert(0,cards[-1])
    del cards[-1]

print(cards[0])