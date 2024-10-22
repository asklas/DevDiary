m = int(input())
n = int(input())
not_dic = []
dec = [a for a in range(2, n+1)]
for i in dec:
    count = 2
    while i*count <= n:
        not_dic.append(i*count)
        count += 1
fin_dec = [x for x in dec if x not in not_dic if x >= m]
if len(fin_dec) > 0:
    print(sum(fin_dec))
    print(min(fin_dec))
else:
    print(-1)
