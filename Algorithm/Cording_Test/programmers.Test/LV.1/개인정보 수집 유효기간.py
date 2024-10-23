def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    tdy,tdm,tdd = map(int, today.split("."))
    for i in terms:
        name,per = map(str,i.split())
        term_dic[name] = per
    for j in range(len(privacies)):
        date,typ = map(str,privacies[j].split())
        y,m,d = map(int,date.split("."))
        m += int(term_dic[typ])
        while m > 12:
            m = m-12
            y = y+1
        if tdy>y:
            answer.append(j+1)
        elif tdy==y and tdm>m:
            answer.append(j+1)
        elif tdy==y and tdm==m and tdd>=d:
            answer.append(j+1)


    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))