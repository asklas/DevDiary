a,b=map(int,input().split())
st=int(input())
et=a*60+b+st
if et<1440:
    h=et//60
    m=et%60
else:
    h=et//60-24
    m=et%60
print(h,m)