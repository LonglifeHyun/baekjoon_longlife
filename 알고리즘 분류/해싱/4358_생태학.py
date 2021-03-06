import fileinput
from collections import defaultdict

alls = fileinput.input()

total = 0
tr_num = defaultdict(int)
tr_name = []

for line in alls:
    # print(line.rstrip('\n'))
    tr_num[line.rstrip('\n')] += 1
    total += 1
# print(tr_num)

tr_name = list(tr_num.keys())
tr_name.sort()

# for tr in tr_name:
#     print(tr + ' ' + str(round((tr_num[tr] * 100) / total, 4)) + '\n', end='')
#     이거 틀린 이유를 모르겠다. 문제 이상한 듯.
# print('--------------------')
for tr in tr_name:
    print(tr, '%.5f' % (tr_num[tr] / total * 100))