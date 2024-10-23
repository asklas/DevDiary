def solution(board):

    m = [list(i) for i in board]

    sflag = False
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "R":
                si, sj = i, j
                sflag = True
                break
        if sflag:
            break

    def bfs(m, si, sj):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = [(si, sj)]
        v = [[-1] * len(m[0]) for _ in range(len(m))]
        v[si][sj] = 0
        
        while q:
            ci, cj = q.pop(0)
            if m[ci][cj] == "G":
                return v[ci][cj]
            
            for di, dj in directions:
                ni, nj = ci, cj
                while True:
                    ni += di
                    nj += dj
                    if ni < 0 or ni >= len(m) or nj < 0 or nj >= len(m[0]) or m[ni][nj] == 'D':
                        ni -= di
                        nj -= dj
                        break
                
                if v[ni][nj] == -1:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
        
        return -1
    
    answer = bfs(m, si, sj)
    return answer
