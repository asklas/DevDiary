x = int(input())
count = 1
max_num = 0
temp = 0

while x > max_num:
    max_num += count
    count += 1
target = max_num-x
for i in range(count-1):
    temp += i
find_area = max_num-temp
if x == 1:
    print("1/1")
elif find_area%2 == 0:
    print ("{}/{}".format(find_area-target,target+1))
else:
    print ("{}/{}".format(target+1,find_area-target))
