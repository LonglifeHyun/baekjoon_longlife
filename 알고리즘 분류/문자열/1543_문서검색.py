import sys

docu = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

search = 0

fst = word[0]
fst_cnt = docu.count(fst)
idx = docu.find(fst)

for _ in range(fst_cnt):
    if docu[idx:idx+len(word)] == word:
        search += 1
        idx = docu.find(fst, idx+len(word))
    else:
        idx = docu.find(fst, idx+1)

    if idx < 0:
        break
    elif not ( (idx+len(word)-1) < len(docu) ):
        break

print(search)