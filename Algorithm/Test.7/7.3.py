row = 5
arr = []
word = [str(input()) for a in range(row)]
max_col = max(len(w) for w in word)

for i in range(max_col):
    for j in range(row):
        if i < len(word[j]):
            arr.append(word[j][i])

print("".join(arr))
