def solution(n, m, section):
    count = 0
    pr_idx = -1
    for i in section:
        if i > pr_idx+m-1 or pr_idx == -1:
            count += 1
            pr_idx = i
    return count
print(solution(8,4,[2,3,6]))