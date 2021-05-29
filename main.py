import requests
import json
from sudoku_solver import *
from menus import *
from time import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return f"Time Lapsed = {int(hours)}:{int(mins)}:{int(sec)}"


def sudoku_solver(grid, lvl):
    try:
        t = initiate_dict(grid)
        seen = []
        while True:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    sys.exit()
            sp = find_empty_space(grid)
            if sp:
                r = sp[0]
                c = sp[1]
                for n in range(t[(r, c)] + 1, 10):
                    if issafe(n, r, c, grid):
                        grid[r][c] = n
                        seen.append((r, c))
                        screen.fill((255, 255, 255))
                        display_grid(grid, seen, lvl=lvl)
                        pygame.display.update()
                        pygame.time.wait(200)
                        t[(r, c)] = n
                        break
                else:
                    t[(r, c)] = 0
                    screen.fill((255, 255, 255))
                    display_grid(grid, seen, (seen[-1][0], seen[-1][1]), lvl=lvl)
                    pygame.display.update()
                    pygame.time.wait(200)
                    grid[seen[-1][0]][seen[-1][1]] = 0
                    del seen[-1]
                    if (r, c) in seen:
                        seen.remove((r, c))
            else:
                print_grid(grid)
                return seen
    except IndexError:
        print("Impossible!")


def display_grid(grid, lis=None, r=(), lvl=""):
    if lis is None:
        lis = []
    for j in range(9):
        for i in range(9):
            pygame.draw.rect(screen, (242, 227, 220), pygame.Rect(80 + 50*i, 80 + 50*j, 50, 50))
            pygame.draw.rect(screen, (180, 180, 180), pygame.Rect(80 + 50*i, 80 + 50*j, 50, 50), width=1)
    for j in range(3):
        for i in range(3):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(80 + 150 * i, 80 + 150 * j, 150, 150), width=1)

    for i in range(9):
        for j in range(9):
            if (i, j) == r:
                text = font1.render(str(grid[i][j]), True, red)
                screen.blit(text, (98 + j * 50, 95 + 50 * i))
            elif (i, j) in lis:
                text = font1.render(str(grid[i][j]), True, green)
                screen.blit(text, (98 + j * 50, 95 + 50 * i))
            else:
                if grid[i][j] != 0:
                    text = font1.render(str(grid[i][j]), True, blue)
                    screen.blit(text, (98 + j * 50, 95 + 50 * i))

    font = pygame.font.Font("OdibeeSans-Regular.ttf", 25)
    text = font.render(lvl, True, (0, 0, 0))

    screen.blit(text, (450, 20))

                  
if __name__ == '__main__':
    pygame.init()
    
    blue = (0, 0, 128)
    green = (0, 255, 0)
    red = (255, 0, 0)
    
    font1 = pygame.font.Font('freesansbold.ttf', 25)
    font2 = pygame.font.Font("OdibeeSans-Regular.ttf", 25)
    
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Sudoku - Backtracking Algorithm Visualizer')
    screen.fill((255, 255, 255))

    d = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    txt = font2.render("New Game", True, (255, 255, 255))
    ng = False
    a = []
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 <= mouse[0] <= 370 and 10 <= mouse[1] <= 60:
                    level = difficulty(screen, font2)
                    if level:
                        ng = True
        
        if ng:
            d = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            size = 9

            sudoku_data = requests.get(f"http://www.cs.utep.edu/cheon/ws/sudoku/new/?size={size}&level={level}")

            sudoku = json.loads(sudoku_data.text)

            for x in sudoku['squares']:
                d[x["x"]][x["y"]] = x["value"]

            screen.fill((255, 255, 255))

            lvls = {1: 'Easy', 2: "Medium", 3: "Hard"}

            display_grid(d, lvl=lvls[level])
            pygame.display.update()
            pygame.time.wait(1000)
            init_t = time()
            a = sudoku_solver(d, lvls[level])
            print(time_convert(time() - init_t))
            pygame.time.wait(100)
            ng = False

        screen.fill((255, 255, 255))
        display_grid(d, a)

        if 220 <= mouse[0] <= 370 and 10 <= mouse[1] <= 60:
            pygame.draw.rect(screen, (104, 104, 104), pygame.Rect(220, 10, 150, 50), border_radius=5)
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(220, 10, 150, 50), border_radius=5)

        screen.blit(txt, (250, 20))

        pygame.display.update()
