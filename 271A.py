year = int(input())
def all_unique(year):
    return len(set(list(str(year)))) == 4

year += 1
while not all_unique(year):
    year += 1
print(year)