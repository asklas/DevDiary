def solution(keymap, targets):
    answer = []
    index = []
    for number in range(len(targets)):
        click = 0
        for target in targets[number]:
            avail = True
            for check in keymap:
                if target in check:
                    index.append(check.find(target)+1)
            if index == []:
                answer.append(-1)
                avail = False
                break
            else:
                click += min([i for i in index if i != 0])
                index = []
        if avail == False:
            break
        else:
            answer.append(click)          
    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))