a,b=map(int,input().split())
basket=[]
for x in range(a):
    basket.append(0)
for y in range(b):
    i,j,k=map(int,input().split())
    for z in range(i,j+1):
        basket[z-1]=int(k)
basket=[str(item) for item in basket]
print(" ".join(basket))
