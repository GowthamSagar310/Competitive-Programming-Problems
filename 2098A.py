from collections import Counter
for _ in range(int(input())):
    s = input()
    c = Counter(s)
    ans = ["9"]
    for i in range(1, 10):
        atleast = 10-i-1
        for num in range(atleast, 10):
            key = str(num)
            if c[key] > 0:
                ans.append(key)
                c[key] -= 1
                if c[key] == 0:
                    del c[key]
                break
    print("".join(ans))
