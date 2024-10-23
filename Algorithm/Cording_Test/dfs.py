def solution(maps):
    answer = []
    
    def dfs(i, j, visited):
        if 0 <= i < len(maps) and 0 <= j < len(maps[0]) and not visited[i][j]:
            if maps[i][j] != 'X' and visited[i][j] != True:
                food = int(maps[i][j])
                visited[i][j] = True
                food += dfs(i-1, j, visited)
                food += dfs(i, j-1, visited)
                food += dfs(i+1, j, visited)
                food += dfs(i, j+1, visited)
                return food
            else:
                visited[i][j] = True
        return 0
    
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            answer.append(dfs(x, y, visited))
    answer = [_ for _ in answer if _ != 0]
    answer.sort()
    if len(answer) > 0:
        return answer
    else:
        answer.append(-1)
        return answer
