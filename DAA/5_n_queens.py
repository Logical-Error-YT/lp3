# N-Queens using backtracking; first queen fixed at row 0, column 0
n = int(input("N (>=4 for this fixed placement): "))
board = [[0] * n for _ in range(n)]
board[0][0] = 1
cols, d1, d2 = {0}, {0}, {0}
def solve(r):
    if r == n:
        return True
    for c in range(1 if r == 0 else 0, n):
        if r == 0:
            continue
        if c not in cols and r-c not in d1 and r+c not in d2:
            board[r][c] = 1
            cols.add(c); d1.add(r-c); d2.add(r+c)
            if solve(r+1):
                return True
            board[r][c] = 0
            cols.remove(c); d1.remove(r-c); d2.remove(r+c)
    return False
if solve(1):
    for row in board:
        print(*row)
else:
    print("No solution with first queen fixed at (0, 0).")
