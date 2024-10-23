qua = int(input())
num = list(map(int, input().split()))
for i in num:
    div_n = 2
    if i == 1:
        qua -= 1
    while div_n < i:
        if i%div_n == 0:
            qua -= 1
            break
        div_n += 1
print (qua)