num = int(input())
count = 2
while num != 1:
    while True:
        if num % count == 0:
            num /= count
            print (count)
        else:
            count += 1
            break
    

