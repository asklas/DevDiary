a,b=map(int,input().split())
ary=input().split()
fin = []
for x in ary:
    if int(x) < b:
        fin.append(x)
print (" ".join(fin))