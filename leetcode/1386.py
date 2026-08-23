n = 4
seats = [[2,10],[3,1],[1,2],[2,2],[3,5],[4,1],[4,9],[2,7]]

def solve(n, seats):
    seats.sort()
    i = 0
    prev_row = 0
    groups = 0
    while i < len(seats):
        s_row , _ = seats[i]
        if s_row == prev_row:
            present = set()
            j = i
            while j < len(seats) and seats[j][0] == s_row:
                present.add(seats[j][1])
                j += 1
            first = all(v not in present for v in [2, 3, 4, 5])
            second = all(v not in present for v in [4, 5, 6, 7])
            third = all(v not in present for v in [6, 7, 8, 9])
            if first:
                groups += 1
                if third:
                    groups += 1
            elif second:
                groups += 1
            elif third:
                groups += 1
            i = j
        else:
            empty_rows = (s_row - prev_row - 1)
            groups += 2 * empty_rows
            prev_row = s_row

    if n != seats[-1][0]:
        empty_rows = (n - seats[-1][0])
        groups += 2 * empty_rows
    return groups
print(solve(n, seats))