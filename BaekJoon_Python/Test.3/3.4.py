money=int(input())
var=int(input())
for a in range(var):
    a,b=map(int, input().split())
    money-=a*b
if money==0:
    print("Yes")
else:
    print("No")
