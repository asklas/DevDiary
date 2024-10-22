amount = int(input())
find_list = list(map(int,input().split()))
find_value = int(input())
x = 0
for a in find_list:
    if a==find_value:
        x += 1
print(x)