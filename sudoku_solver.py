# SUDOKU SOLVER
def in_3x3(r, c, n, grid):
    a = r // 3 * 3
    b = c // 3 * 3
    return n in [grid[i][c] for i, c in zip([a] * 3 + [a + 1] * 3 + [a + 2] * 3, [b, b + 1, b + 2] * 3)]


def in_row(r, n, grid):
    return n in grid[r]


def in_column(c, n, grid):
    return n in [i[c] for i in grid]


def issafe(n, r, c, grid):
    return not in_3x3(r, c, n, grid) and not in_row(r, n, grid) and not in_column(c, n, grid)


def print_grid(grid):
    for a in range(9):
        for b in range(9):
            print(grid[a][b], end=" ")
            if (b + 1) % 3 == 0 and b != 8:
                print(" |", end=" ")
        if (a + 1) % 3 == 0 and a != 8:
            print("\n-----------------------")
        else:
            print()


def find_empty_space(grid):
    for a in grid:
        for b in a:
            if b == 0:
                return [grid.index(a), a.index(b)]
    return False


def initiate_dict(grid):
    d = {}
    for a in range(9):
        for b in range(9):
            if grid[a][b] == 0:
                d[(a, b)] = 0
    return d
