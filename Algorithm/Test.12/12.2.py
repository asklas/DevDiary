n = int(input())

def get_digit_sum(num):
    return sum(map(int, str(num)))

start_point = max(1, n - len(str(n)) * 9)

for x in range(start_point, n):
    if n == x + get_digit_sum(x):
        print(x)
        break
else:
    print(0)
