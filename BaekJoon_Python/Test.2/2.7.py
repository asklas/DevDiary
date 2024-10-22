dice=list(map(int,input().split()))
dup=[]
for a in dice:
    if a not in dup:
        dup.append(a)
    else:
        val=a
if len(dup)==1:
    print(10000+val*1000)
elif len(dup)==2:
    print(1000+val*100)
else:
    print(max(dice)*100)

    