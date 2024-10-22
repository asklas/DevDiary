while True:
    Test_case = int(input())
    if Test_case == -1:
        break
    div = []
    for i in range(1,Test_case):
        if Test_case%i == 0:
            div.append(i)
    str_conv = [str(x) for x in div]
    conv = " + ".join(str_conv)
    if sum(div)==Test_case:
        print (f"{Test_case} = {conv}")
    else:
        print(f"{Test_case} is NOT perfect.")