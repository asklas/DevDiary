Test_case = int(input())
check = 0
for a in range(Test_case):
    string = input()
    con_list = []


    for y in range(len(string)):
        x = string[y]
        
        if x not in con_list:
            con_list.append(x)
        elif x in con_list and x == string[y-1]:
            continue
        else:
            check += 1
            break

print(Test_case - check)
