room_num = int(input())

if room_num == 1:
    moves = 1
else:
    count = 1 
    while room_num > 1 + 3 * count * (count - 1):
        count += 1
    moves = count

print(moves)
