a, b, c = 300, 60, 10
t = int(input())
cnt_btn_a = t//a
cnt_btn_b = (t%a)//b
cnt_btn_c = ((t%a)%b)//c

if ((t%a)%b)%c == 0:
    print(cnt_btn_a,cnt_btn_b,cnt_btn_c,end=' ')
else:
    print(-1)