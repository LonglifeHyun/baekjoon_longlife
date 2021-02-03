w1, w2 = input(), input()

cnt = 0

for i in range(ord('a'),ord('z')+1):
    w1_cnt = w1.count(chr(i))
    w2_cnt = w2.count(chr(i))
    if w1_cnt != w2_cnt:
        cnt += max(w1_cnt,w2_cnt) - min(w1_cnt,w2_cnt)

print(cnt)