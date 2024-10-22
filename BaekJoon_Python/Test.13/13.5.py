import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (10000 + 1)

for _ in range(n):
    arr[int(input())] += 1
  
for i in range(len(arr)):
    if arr[i] != 0: 
        for _ in range(arr[i]):
            print(i)

"""
계수정렬법
모두 입력받은 리스트 정렬 후 출력 -> 메모리 제한
-> 입력될 수 있는 정수 +1 크기의 리스트 생성
-> 입력받은 정수의 인덱스에 해당하는 요소 +1
-> 리스트를 순회하며 값이 0이 아니라면, 해당 요소의 수만큼 인덱스 출력
"""