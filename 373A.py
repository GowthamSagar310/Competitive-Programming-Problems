k = int(input())
board = []
for _ in range(4):
    board.append(input())

freq = [0] * 10
for i in range(4):
    for j in range(4):
        if board[i][j].isnumeric():
            freq[int(board[i][j])] += 1

def solve(freq):
    for val in freq:
        if val > 0:
            if val > 2 * k:
                return False
    return True
print("YES" if solve(freq) else "NO")