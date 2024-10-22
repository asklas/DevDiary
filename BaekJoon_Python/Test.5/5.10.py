def cal(alpha):
    if alpha in ["A", "B", "C"]:
        return 3
    elif alpha in ["D", "E", "F"]:
        return 4
    elif alpha in ["G", "H", "I"]:
        return 5
    elif alpha in ["J", "K", "L"]:
        return 6
    elif alpha in ["M", "N", "O"]:
        return 7
    elif alpha in ["P", "Q", "R", "S"]:
        return 8
    elif alpha in ["T", "U", "V"]:
        return 9
    else:
        return 10

string = input()
time = 0
for a in string:
    time += cal(a)

print(time)
