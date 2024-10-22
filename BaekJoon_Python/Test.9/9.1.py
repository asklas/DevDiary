while True:
    user_input = input()
    if user_input == "0 0":
        break
    a,b = map(int,user_input.split())
    if b%a == 0:
        print ("factor")
    elif a%b == 0:
        print("multiple")
    else:
        print("neither")
    
