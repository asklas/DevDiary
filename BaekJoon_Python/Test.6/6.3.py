star = int(input())
for a in range(star):
    print(" "*(star-1-a)+"*"*a+"*"+"*"*a)
for b in range(1,star):
    print(" "*b+"*"*(star-b-1)+"*"+"*"*(star-b-1))