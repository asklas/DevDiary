student = []
for i in range(1,int(31)):
    student.append(i)
for a in range(int(28)):
    x = int(input())
    student.remove(x)
print(min(student))
print(max(student))