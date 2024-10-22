x, y = map(int, input().split())
board = []
change = []

for _ in range(x):
    board.append(input())

for i in range(x-7):
    for j in range(y-7):
        b_count = 0
        w_count = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0 and board[a][b] != "B":
                    b_count += 1
                elif (a+b) % 2 != 0 and board[a][b] != "W":
                    b_count += 1
                elif (a+b) % 2 == 0 and board[a][b] != "W":
                    w_count += 1
                elif (a+b) % 2 != 0 and board[a][b] != "B":
                    w_count += 1
        change.append(min(b_count, w_count))

result = min(change)
print(result)
