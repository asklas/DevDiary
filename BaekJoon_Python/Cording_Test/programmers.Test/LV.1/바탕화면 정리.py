def solution(wallpaper):
    answer = []
    lx = "X"
    ly = "X"
    mx = 0
    my = 0
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            if lx == "X":
                lx = i
            else:
                lx = min(lx,i)
            mx = max(mx,i)
            for j in range(len(wallpaper[i])):
                if wallpaper[i][j] == "#":
                    if ly == "X":
                        ly = j
                    else:
                        ly = min(ly,j)
                    my = max(my,j)
    answer.append(lx)
    answer.append(ly)
    answer.append(mx+1)
    answer.append(my+1)
    return answer
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))