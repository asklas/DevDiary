ex = []
for _ in range(int(10)):
    x = int(input())
    ex.append(x%42)
fin=list(set(ex))
    
print(len(fin))
