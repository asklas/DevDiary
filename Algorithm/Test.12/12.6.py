sugar = int(input())
count = 0

while sugar > 0:
    if sugar % 5 == 0:
        count += sugar // 5
        sugar = 0
    else:
        sugar -= 3
        count += 1

if sugar == 0:
    print(count)
else:
    print(-1)
