import re 
s = input()
s = re.sub("WUB", " ", s)
s = re.sub("\s+", " ", s).strip()
print(s)