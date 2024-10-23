import re
cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
ori = input()
pattern = "|".join(re.escape(s) for s in cro)
modified = re.sub(pattern,"a",ori)
print(len(modified))
