def solution(sequence, k):
    cum_sum = [0]
    for num in sequence:
        cum_sum.append(cum_sum[-1] + num)
        
    min_length = float('inf')
    result = None
    
    left = right = 0
    while left < len(cum_sum):
        while right < len(cum_sum) and cum_sum[right] - cum_sum[left] <= k:
            if cum_sum[right] - cum_sum[left] == k:
                if right - left < min_length:
                    min_length = right - left
                    result = [left, right - 1]
                break
            right += 1
        left += 1
    
    return result
