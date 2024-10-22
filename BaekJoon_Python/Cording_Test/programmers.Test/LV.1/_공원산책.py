def solution(park, routes):
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == "S":
                cor = [x, y]
                break

    dir = {"N": 0, "S": 1, "W": 2, "E": 3}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for move in routes:
        op, n = move.split()
        n = int(n)

        for i in range(n):
            next_x = cor[0] + dx[dir[op]]
            next_y = cor[1] + dy[dir[op]]

            if 0 <= cor[0]+(next_x*n) < len(park) and 0 <= cor[1]+(next_y*n) < len(park[0]) and park[next_x][next_y] != "X":
                cor[0] = next_x
                cor[1] = next_y

    return cor
