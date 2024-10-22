num, target = map(int, input().split())
num_list = list(map(int, input().split()))
f_sum = 0

for i in range(num - 2):
    for j in range(i + 1, num - 1):
        for k in range(j + 1, num):
            current_sum = num_list[i] + num_list[j] + num_list[k]
            if current_sum <= target:
                f_sum = max(f_sum, current_sum)

print(f_sum)
