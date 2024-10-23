def solution(bandage, health, attacks):
    answer = 0
    count = 0
    max_health = health
    for time in range(attacks[0][0],(attacks[-1][0])+1):
        if time == attacks[0][0]:
            health -= attacks[0][1]
            count = 0
            if health <= 0:
                return -1
            del attacks[0]
            if attacks == []:
                break
        else:
            health += bandage[1]
            count += 1
        if count == bandage[0]:
            health += bandage[2]
            count = 0
        if health>max_health:
            health = max_health
    answer = health
    return answer
print(solution([5,1,5],30,[[2,10],[9,15],[10,5],[11,5]]))