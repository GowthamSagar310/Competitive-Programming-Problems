for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        s = input()
        s_to_t = {}
        t_to_s = {}
        if len(s) != n:
            print("NO")
            continue
        matches = True
        for i, letter in enumerate(s):
            if letter in s_to_t:
                prev_index = s_to_t[letter]
                if prev_index != arr[i]:
                    matches = False
                    break

            if arr[i] in t_to_s:
                prev_letter = t_to_s[arr[i]]
                if prev_letter != letter:
                    matches = False
                    break
            s_to_t[letter] = arr[i]
            t_to_s[arr[i]] = letter

        print("YES" if matches else "NO")