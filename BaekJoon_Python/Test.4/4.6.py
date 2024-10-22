a,b=map(int,input().split())
basket=[]
temp = int(0)
for x in range(a):
    basket.append(x+1)

for y in range(b):
    i,j=map(int,input().split())
    basket[j-1],basket [i-1] = basket [i-1],basket [j-1]
basket=[str(item) for item in basket]
print(" ".join(basket))

