import sys
input = sys.stdin.readline

arr = []

for i in input().strip():
    arr.append(int(i))

arr.sort(reverse=True)

print("".join(str(j) for j in arr))
