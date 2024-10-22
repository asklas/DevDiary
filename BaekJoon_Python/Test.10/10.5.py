n=int(input())
min_x = 10001
min_y = 10001
max_x = -10001
max_y = -10001
for _ in range(n):
    x,y = map(int,input().split())
    min_x = min(min_x,x)
    min_y = min(min_y,y)
    max_x = max(max_x,x)
    max_y = max(max_y,y)
if n == 1:
    print(0)
elif max_x < 0 and min_y > 0:
    print((min_x-max_x)*(max_y-min_y))
elif min_x > 0 and max_y < 0:
    print((max_x-min_x)*(min_y-max_y))
elif max_x > 0 and max_y > 0:
    print((min_x-max_x)*(min_y-max_y))
else:
    print((max_x-min_x)*(max_y-min_y))