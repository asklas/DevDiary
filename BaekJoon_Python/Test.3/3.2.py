test_case=int(input())
fin=[]
for i in range(test_case):
    x,y=map(int,input().split())
    fin.append(x+y)
print('\n'.join(map(str,fin)))