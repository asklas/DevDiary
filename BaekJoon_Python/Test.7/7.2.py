rows = 9
cols = 9
max_value = 0

arr = [list(map(int, input().split())) for i in range(rows)]

for i in arr:
    max_value = max(max_value, max(i))

for j in range(rows):
    for k in range(cols):
        if arr[j][k] == max_value:
            print(f"{max_value}\n{j+1} {k+1}")
