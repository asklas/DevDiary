def solution(name, yearning, photo):
    answer = []

    for j in photo:
        score = 0
        for k in j:
            if k in name:
                score += yearning[name.index(k)]
        answer.append(score)
    return answer