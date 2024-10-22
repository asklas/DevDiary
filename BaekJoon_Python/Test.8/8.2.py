a,b=map(int,input().split())
num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tem = []
while a:
    tem.append(num[a%b])
    a//=b
ans=tem[::-1]
print("".join(ans))