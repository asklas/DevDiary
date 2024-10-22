import sys
test_case=int(input())
for n in range(test_case):
    line = sys.stdin.readline().strip()
    a,b =map(int,line.split()) 
    print("Case #{}:".format(n+1), a+b)

