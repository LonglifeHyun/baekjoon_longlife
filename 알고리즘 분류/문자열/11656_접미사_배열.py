ss = input()
suffix = []
for i,c in enumerate(ss):
    suffix.append(ss[i:len(ss)])

suffix.sort()
for suf in suffix:
    print(suf)
