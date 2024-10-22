Test_case=int(input())
coin = [25,10,5,1]
for _ in range(Test_case):
    back = []
    cent = int(input())
    for x in coin:
        back.append(str(cent//x))
        cent %= x
    print (" ".join(back))