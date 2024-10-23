def solution(friends, gifts):
    answer = 0
    gift = [0 for i in range(len(friends))]
    count = [[0 for i in range(len(friends))] for j in range(len(friends))]        
    for i in gifts:
        a,b = map(str, i.split())
        count[friends.index(a)][friends.index(b)] += 1
    for x in range(len(count)):
        for y in range(len(count)):
            if x==y:
                continue
            elif count[x][y]>count[y][x]:
                gift[x] += 1
            elif count[x][y] == count[y][x]:
                my_gift_score = 0
                others = 0
                for z in range(len(friends)):
                    my_gift_score += count[z][x]
                    others += count[z][y]
                if sum(count[x])-my_gift_score > sum(count[y])-others:
                    gift[x] += 1

    answer = max(gift)
    return answer
print(solution(["muzi", "ryan", "frodo", "neo"],
         ["muzi frodo", "muzi frodo", "ryan muzi",
           "ryan muzi", "ryan muzi", "frodo muzi",
             "frodo ryan", "neo muzi"]))