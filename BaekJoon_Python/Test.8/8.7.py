day,night,height = map(int,input().split())
if (height-day)%(day-night) == 0:
    print((height-day)//(day-night)+1)
else:
    print((height-day)//(day-night)+2)
