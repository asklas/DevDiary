import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        max_y_r2 = math.floor(math.sqrt(r2**2 - x**2))
        
        if x < r1:
            min_y_r1 = math.ceil(math.sqrt(r1**2 - x**2))
        else:
            min_y_r1 = 0

        answer += (max_y_r2 - min_y_r1 + 1)
    
    return answer * 4