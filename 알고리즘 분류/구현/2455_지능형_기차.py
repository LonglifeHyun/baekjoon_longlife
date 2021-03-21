max_man = 0
train = 0
for _ in range(4):
    off, on = map(int, input().split())
    train -= off
    if max_man < train:
        max_man = train
    train += on
    if max_man < train:
        max_man = train
print(max_man)