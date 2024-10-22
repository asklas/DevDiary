x=[]
y=[]
for _ in range(3):
    i,j = map(int,input().split())
    x.append(i)
    y.append(j)
fin_x = [str(a) for a in x if x.count(a) == 1]
fin_y = [str(b) for b in y if y.count(b) == 1]
q = "".join(fin_x)
w = "".join(fin_y)
print(q,w)
