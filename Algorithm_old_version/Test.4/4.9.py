n,m = map(int,input().split())
arr = [i for i in range(1, n+1)]
for i in range(m):
    i,j = map(int,input().split())
    i-=1; j-=1
    arr[i:j+1] = arr[i:j+1][::-1]
print(*arr)