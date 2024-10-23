def hanoi(n, start, end, temp):
    if n == 1:
        return [[start, end]]
    else:
        # 1. n-1개의 원판을 시작 기둥에서 중간 기둥으로 이동
        moves = hanoi(n-1, start, temp, end)
        # 2. 마지막 원판을 시작 기둥에서 목표 기둥으로 이동
        moves.append([start, end])
        # 3. n-1개의 원판을 중간 기둥에서 목표 기둥으로 이동
        moves.extend(hanoi(n-1, temp, end, start))
        return moves

def solution(n):
    return hanoi(n, 1, 3, 2)

# 예시 사용법
n = 4
result = solution(n)
print(result)
