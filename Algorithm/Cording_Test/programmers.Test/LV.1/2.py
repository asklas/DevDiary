def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    hidden = []
    for x, y in zip(arr1, arr2):
        map1.append(bin(x)[2:].zfill(n))
        map2.append(bin(y)[2:].zfill(n))
    for i, j in zip(map1, map2):
        for k, l in zip(i, j):
            if k == '1' or l == '1':
                hidden.append('#')
            else:
                hidden.append(' ')
    pre_answer = [hidden[m:m + n] for m in range(0, len(hidden), n)]
    for o in pre_answer:
        answer.append("".join(o))
    return answer

