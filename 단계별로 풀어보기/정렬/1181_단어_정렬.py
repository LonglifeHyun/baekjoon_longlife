# n = int(input())
#
# words = [[] for i in range(51)]       # list 이용
# for i in range(n):
#     tmp = input()
#     words[len(tmp)].append(tmp)
#
#
# for word in words:
#     if len(word) > 0:
#         word_set = set(word)
#         word = list(word_set)
#         word.sort()
#         for w in word:
#             print(w)

n = int(input())

words = [set() for i in range(51)]      # set 이용
for i in range(n):
    tmp = input()
    words[len(tmp)].add(tmp)

for word in words:
    if len(word) > 0:
        word_list = list(word)
        word_list.sort()
        for w in word_list:
            print(w)
