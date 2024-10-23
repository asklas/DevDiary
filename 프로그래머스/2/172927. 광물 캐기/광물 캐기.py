def solution(picks, minerals):
    answer = 0
    max_pic = sum(picks) * 5
    
    if len(minerals) >= max_pic:
        minerals = minerals[:max_pic]

    sep_min = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]

    pick_list = [[block.count("diamond"), block.count("iron"), block.count("stone")] for block in sep_min]
    
    work_list = [[x*1+y*1+z*1,x*5+y*1+z*1,x*25+y*5+z*1] for x,y,z in pick_list]
    
    work_list.sort(key=lambda x: (x[2], x[1], x[0]),reverse = True)
    
    for d,i,s in work_list:
        if picks[0] > 0:
            answer += d
            picks[0] -= 1
        elif picks[1] > 0:
            answer += i
            picks[1] -= 1
        elif picks[2] > 0:
            answer += s
        else:
            break
            

    return answer

