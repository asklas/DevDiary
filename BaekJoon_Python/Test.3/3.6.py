import sys
test_case=int(input())
for a in range(test_case):
    line = sys.stdin.readline().strip()
    a,b =map(int,line.split())
    print(a+b)

#a,b = map(int,sys.stdin.readline().split()) 으로 사용 가능하다

