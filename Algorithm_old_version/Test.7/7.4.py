paper = int(input())
check_area = [list(map(int, input().split())) for _ in range(paper)]

max_x = max(x for x, _ in check_area) + 10
max_y = max(y for _, y in check_area) + 10

area = [[0] * max_x for _ in range(max_y)]

for i, j in check_area:
    for xx in range(i, i + 10):
        for yy in range(j, j + 10):
            area[yy][xx] = 1

total_sum = sum(row.count(1) for row in area)

print(total_sum)
