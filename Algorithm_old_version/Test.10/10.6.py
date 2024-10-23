tri = ['a', 'b', 'c']
for i in range(3):
    tri[i] = int(input())

a, b, c = tri
if a+b+c != 180:
    print('Error')
elif a==b==c:
    print('Equilateral')
elif a==b or b==c or c==a:
    print('Isosceles')
else:
    print('Scalene')
