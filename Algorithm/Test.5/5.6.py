find_string = input()
index_list = []
def find_index(string,target):
    for index,char in enumerate(string):
        if char == target:
            return(index)
    return -1
for alphabet in range (97,123):
    index_list.append(find_index(find_string,chr(alphabet)))
final = " ".join(str(index) for index in index_list)
print(final)
