
def solve_n_queens(n):
    def is_safe(row, col):
        return not (cols[col] or diag1[row + col] or diag2[row - col])

    def place_queen(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                cols[col] = diag1[row + col] = diag2[row - col] = True
                place_queen(row + 1)
                board[row][col] = '.'
                cols[col] = diag1[row + col] = diag2[row - col] = False

    result = []
    board = [['.'] * n for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)
    place_queen(0)
    return result

# Example usage:
solutions = solve_n_queens(4)
for sol in solutions:
    for row in sol:
        print(row)
    print()


