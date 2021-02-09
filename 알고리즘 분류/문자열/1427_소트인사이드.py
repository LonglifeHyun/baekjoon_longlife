n = input()
list_n = [int(i) for i in n]
list_n.sort(reverse=True)
for i in list_n:
    print(i,end="")