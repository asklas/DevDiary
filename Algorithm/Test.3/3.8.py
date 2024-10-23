import sys
test_case=int(input())
for n in range(test_case):
    a,b = map(int,sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(n+1,a,b,a+b))

