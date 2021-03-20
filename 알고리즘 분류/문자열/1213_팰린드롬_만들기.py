from collections import Counter,deque

name = input()

counter = Counter(name)
alphabet = list(counter.keys())
alphabet.sort(reverse=True)

odd_cnt = 0
palindrome = deque()
is_valid = True
for c in alphabet:
    if len(name)%2==0 and counter[c]%2!=0:
        is_valid = False
        break
    elif len(name)%2!=0 and counter[c]%2!=0:
        odd_cnt += 1
        if odd_cnt >= 2:
            is_valid = False
            break

        mid = len(palindrome) // 2
        palindrome.insert(mid,c)
        counter[c] -= 1

    while counter[c] > 0:
        palindrome.append(c)
        palindrome.appendleft(c)
        counter[c] -= 2

if is_valid:
    for pal_c in palindrome:
        print(pal_c,end='')
else:
    print("I'm Sorry Hansoo")


