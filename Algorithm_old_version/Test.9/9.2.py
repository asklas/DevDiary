d_num = []
num = 1
n,k=map(int,input().split())
while len(d_num)!=k:
    if n%num == 0:
        d_num.append(num)
    num += 1
    if num>n:
        break
if k<=len(d_num):
    print(d_num[-1])
else:
    print(0)