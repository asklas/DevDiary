subject_count = int(input())
score = list(map(int,input().split()))
new_score = []
for x in range(len(score)):
    new_score.append(score[x]/max(score)*100)
average=int(0)
for a in new_score:
    average += a
print (average/subject_count)