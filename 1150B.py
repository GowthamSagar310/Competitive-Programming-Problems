n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))

def solve(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                if (
                    (i-1 >= 0 and board[i-1][j] == ".") and 
                    (i+1 < n and board[i+1][j] == ".") and 
                    (j-1 >= 0 and board[i][j-1] == ".") and 
                    (j+1 < n and board[i][j+1] == ".")
                ):
                    board[i][j] = "#"
                    board[i-1][j] = "#"
                    board[i+1][j] = "#"
                    board[i][j-1] = "#"
                    board[i][j+1] = "#"
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                return False
    return True

print("YES" if solve(board) else "NO")