for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = [0] * 26
    res = []
    for val in arr:
        for i in range(26):
            if freq[i] == val:
                freq[i] += 1
                # res += chr(i + ord('a')) TLE
                res.append(chr(i + ord('a')))
                break
    print("".join(res))

    