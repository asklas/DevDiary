row, col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]

for i in range(len(arr)):
    value = list(map(int, input().split()))
    arr[i] = [x + y for x, y in zip(arr[i], value)]

print("\n".join(" ".join(map(str,a))for a in arr))
