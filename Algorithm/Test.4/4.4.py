count = 0
max_num = 0
index = 0
while count < 9:
    count += 1
    a = int(input())
    max_num = max(a,max_num)
    if a == max_num:
        index = count
print(max_num)
print(index)