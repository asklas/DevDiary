time = int(input())
def new_string(x,y):
    new = []
    for a in y:
        b = a*int(x)
        new.append(b)
    final_string = "".join(new)
    return final_string
for i in range(time):
    num,string = input().split()
    print(new_string(num,string))