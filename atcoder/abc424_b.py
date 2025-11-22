n, m, k = map(int, input().split())
persons = [0] * n
for _ in range(k):
    person, problem = map(int, input().split())
    persons[person-1] += 1
    if persons[person-1] == m:
        print(str(person), end = " ")