a=input()
test = a.upper()
find={}
for x in test:
    if x in find:
        find[x] += 1
    else:
        find[x] = int(1)
max_value = max(find.values())
count_max_values = sum(value == max_value for value in find.values())
final_key = [key for key,value in find.items() if value == max_value]
if count_max_values == 1:
    print("".join(final_key))
else:
    print("?")