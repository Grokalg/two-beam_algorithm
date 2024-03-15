import pygame
import sys

def click(source, ways):
    global start_ways, finish_ways
    if source == 1:
        start_ways = ways
    if source == 2:
        finish_ways = ways

class SelectButton1():
    alreadyPressed = False

    def __init__(self, x, y, width, height, buttonText='Button', ways=[]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ways = ways
        self.alreadyPressed = False

        self.fillColors = {
            'normal': 'orange',
            'hover': 'darkorange',
            'pressed': 'orangered',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def clear(self):
        SelectButton1.alreadyPressed = False
        self.alreadyPressed = False
        game_screen.blit(self.buttonSurface, self.buttonRect)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0] and not SelectButton1.alreadyPressed:
                self.buttonSurface.fill(self.fillColors['pressed'])
                click(1, self.ways)
                SelectButton1.alreadyPressed = True
                self.alreadyPressed = True
        if self.alreadyPressed:
            self.buttonSurface.fill(self.fillColors['pressed'])

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        game_screen.blit(self.buttonSurface, self.buttonRect)

class SelectButton2():
    alreadyPressed = False

    def __init__(self, x, y, width, height, buttonText='Button', ways=[]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alreadyPressed = False
        self.ways = ways

        self.fillColors = {
            'normal': 'orange',
            'hover': 'darkorange',
            'pressed': 'orangered',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def clear(self):
        SelectButton2.alreadyPressed = False
        self.alreadyPressed = False
        game_screen.blit(self.buttonSurface, self.buttonRect)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0] and not SelectButton2.alreadyPressed:
                self.buttonSurface.fill(self.fillColors['pressed'])
                click(2, self.ways)
                SelectButton2.alreadyPressed = True
                self.alreadyPressed = True
        if self.alreadyPressed:
            self.buttonSurface.fill(self.fillColors['pressed'])

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        game_screen.blit(self.buttonSurface, self.buttonRect)

class ConfigureButton():
    def __init__(self, x, y, width, height, buttonText='Старт', onclickFunction=None):
        self.x = x
        self.y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.alreadyPressed = False

        self.fillColors = {
            'normal': 'orange',
            'hover': 'darkorange',
            'pressed': 'orangered',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0] and SelectButton1.alreadyPressed and SelectButton2.alreadyPressed:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.onclickFunction()
        if self.alreadyPressed:
            self.buttonSurface.fill(self.fillColors['pressed'])

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        game_screen.blit(self.buttonSurface, self.buttonRect)

class WorkSpace():
    def __init__(self, x, y, width, height, start, finish, cols, rows, grid, TILE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.workSurface = pygame.Surface((self.width, self.height))
        self.workSurface.fill((2, 92, 15))
        self.workRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.cols, self.rows = cols, rows
        self.TILE = TILE
        self.grid = grid
        self.start = [i * self.TILE for i in start] + [self.TILE, self.TILE]
        self.finish = [i * self.TILE for i in finish] + [self.TILE, self.TILE]
        objects.append(self)

    def clear(self):
        self.draw_grid()
        game_screen.blit(self.workSurface, self.workRect)

    def get_rect(self):
        return self.x * self.TILE + 1, self.y * self.TILE + 1, self.TILE - 2, self.TILE - 2

    def draw_grid(self):
        for self.y, self.rows in enumerate(self.grid):
            for self.x, col in enumerate(self.rows):
                if col:
                    pygame.draw.rect(self.workSurface, pygame.Color('darkorange'), self.get_rect(),
                                     border_radius=self.TILE // 5)
        pygame.draw.rect(self.workSurface, pygame.Color('red'), self.start,
                         border_radius=self.TILE // 5)
        pygame.draw.rect(self.workSurface, pygame.Color('red'), self.finish,
                         border_radius=self.TILE // 5)

    def process(self):
        self.draw_grid()
        game_screen.blit(self.workSurface, self.workRect)

class Point():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.workRect = pygame.Rect(40, 40, 600, 500)
        self.WorkSpace = MainWorkSpace
        self.color = color
        objects.append(self)

    def get_rect(self):
        return self.x * TILE + 1, self.y * TILE + 1, TILE - 2, TILE - 2

    def process(self):
        pygame.draw.rect(self.WorkSpace.workSurface, self.color, self.get_rect(),
                         border_radius=TILE // 5)
        game_screen.blit(self.WorkSpace.workSurface, self.workRect)


def get_next_nodes(x, y, way):
    if 0 <= x + way[0] < cols and -rows < y + way[1] <= 0 and grid[-(y + way[1])][x + way[0]] != 1:
        return [x + way[0], y + way[1]]
    else:
        return False

def find_way(deque, deque3, deque4):
    if len(deque) <= 1:
        next_node = get_next_nodes(deque[0][0], deque[0][1], start_ways[0])
    else:
        if deque[-1] in deque3 or deque[-1] in deque4:
            return False
        else:
            next_node = get_next_nodes(deque[-1][0], deque[-1][1], start_ways[0])
            if next_node is False:
                next_node = get_next_nodes(deque[-1][0], deque[-1][1], start_ways[1])
            if next_node is False:
                next_node = get_next_nodes(deque[-2][0], deque[-2][1], start_ways[0])
    if next_node is False:
        return False
    else:
        try:
            deque.append(next_node)
            Point(next_node[0], -next_node[1], pygame.Color((212, 208, 140)))
            find_way(deque)
        except TypeError:
            return deque

def find_way2(deque, deque3, deque4):
    if len(deque) <= 1:
        next_node = get_next_nodes(deque[0][0], deque[0][1], start_ways[1])
    else:
        if deque[-1] in deque3 or deque[-1] in deque4:
            return False
        else:
            next_node = get_next_nodes(deque[-1][0], deque[-1][1], start_ways[1])
            if next_node is False:
                next_node = get_next_nodes(deque[-1][0], deque[-1][1], start_ways[0])
            if next_node is False:
                next_node = get_next_nodes(deque[-2][0], deque[-2][1], start_ways[1])
    if next_node is False:
        return False
    else:
        try:
            deque.append(next_node)
            Point(next_node[0], -next_node[1], pygame.Color((212, 208, 140)))
            find_way2(deque)
        except TypeError:
            return deque

def find_way3(deque, deque1, deque2):
    if len(deque) <= 1:
        next_node = get_next_nodes(deque[0][0], deque[0][1], finish_ways[0])
    else:
        if deque[-1] in deque1 or deque[-1] in deque2:
            return False
        else:
            next_node = get_next_nodes(deque[-1][0], deque[-1][1], finish_ways[0])
            if next_node is False:
                next_node = get_next_nodes(deque[-1][0], deque[-1][1], finish_ways[1])
            if next_node is False:
                next_node = get_next_nodes(deque[-2][0], deque[-2][1], finish_ways[0])
    if next_node is False:
        return False
    else:
        try:
            deque.append(next_node)
            Point(next_node[0], -next_node[1], pygame.Color("yellow"))
            find_way(deque)
        except TypeError:
            return deque

def find_way4(deque, deque1, deque2):
    if len(deque) <= 1:
        next_node = get_next_nodes(deque[0][0], deque[0][1], finish_ways[1])
    else:
        if deque[-1] in deque1 or deque[-1] in deque2:
            return False
        else:
            next_node = get_next_nodes(deque[-1][0], deque[-1][1], finish_ways[1])
            if next_node is False:
                next_node = get_next_nodes(deque[-1][0], deque[-1][1], finish_ways[0])
            if next_node is False:
                next_node = get_next_nodes(deque[-2][0], deque[-2][1], finish_ways[1])
    if next_node is False:
        return False
    else:
        try:
            deque.append(next_node)
            Point(next_node[0], -next_node[1], pygame.Color("yellow"))
            find_way(deque)
        except TypeError:
            return deque

def ReadFile():
    grid = [[0 for j in range(12)] for i in range(10)]
    numbers = []
    start = []
    finish = []
    with open("Labirint.txt", 'r') as f:
        lines = f.readlines()
        for element in lines[0]:
            try:
                numbers.append(int(element))
            except ValueError:
                continue
        for j in range(0, 12):
            grid[0][j] = numbers[j]
        for i in range(1, 10):
            for j in range(0, 12):
                if j == 0:
                    l = 12*i
                    grid[i][j] = numbers[l]
                else:
                    l+=1
                    grid[i][j] = numbers[l]
        start.append(int(lines[1]))
        start.append(int(lines[2]))
        finish.append(int(lines[3]))
        finish.append(int(lines[4]))
    return grid, start, finish

def Download(data):
    with open("Result.txt", 'w') as f:
        print(data, file=f)

def FormationResultWay():
    deques1 = []
    deques2 = []
    result = []
    deques1.append(deque1)
    deques1.append(deque2)
    deques2.append(deque3)
    deques2.append(deque4)
    for i in range(0, 2):
        for j in range(0, 2):
            if deques1[i][-1] == deques2[j][-1]:
                result = deques1[i][:-1] + deques2[j][::-1]
                break
    return result

def StartEmitting():
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    while True:
        if find_way(deque1, deque3, deque4) is False and flag1 < 1:
            flag1 += 1
        if find_way2(deque2, deque3, deque4) is False and flag2 < 1:
            flag2 += 1
        if find_way3(deque3, deque1, deque2) is False and flag3 < 1:
            flag3 += 1
        if find_way4(deque4, deque1, deque2) is False and flag4 < 1:
            flag4 += 1
        if flag1 >= 1 and flag2 >= 1 and flag3 >= 1 and flag4 >= 1:
            Download(FormationResultWay())
            break

def ClearWorkspace():
    global start, finish, start_ways, finish_ways, deque1, deque2, deque3, deque4, buttons, MainWorkSpace
    start_ways = [[1, 0], [0, -1]]
    finish_ways = [[-1, 0], [0, 1]]
    deque1 = [[start[0], -start[1]]]
    deque2 = [[start[0], -start[1]]]
    deque3 = [[finish[0], -finish[1]]]
    deque4 = [[finish[0], -finish[1]]]
    for button in buttons:
        button.clear()
    MainWorkSpace = WorkSpace(40, 40, 600, 500, start, finish, cols, rows, grid, TILE)

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
game_screen = pygame.display.set_mode((900, 610))
font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Vekhtev")
objects = []

cols = 12
rows = 10
TILE = 50
grid, start, finish = ReadFile()
start_ways = [[1, 0], [0, -1]]
finish_ways = [[-1, 0], [0, 1]]
deque1 = [[start[0], -start[1]]]
deque2 = [[start[0], -start[1]]]
deque3 = [[finish[0], -finish[1]]]
deque4 = [[finish[0], -finish[1]]]
buttons = []

buttons.append(SelectButton1(700, 40, 150, 50, 'Вверх-вправо', [[1, 0], [0, 1]]))
buttons.append(SelectButton1(700, 100, 150, 50, 'Вправо-вниз', [[1, 0], [0, -1]]))
buttons.append(SelectButton1(700, 160, 150, 50, 'Вниз-влево', [[-1, 0], [0, -1]]))
buttons.append(SelectButton1(700, 220, 150, 50, 'Влево-вверх', [[-1, 0], [0, 1]]))
buttons.append(SelectButton2(700, 310, 150, 50, 'Вверх-вправо', [[1, 0], [0, 1]]))
buttons.append(SelectButton2(700, 370, 150, 50, 'Вправо-вниз', [[1, 0], [0, -1]]))
buttons.append(SelectButton2(700, 430, 150, 50, 'Вниз-влево', [[-1, 0], [0, -1]]))
buttons.append(SelectButton2(700, 490, 150, 50, 'Влево-вверх', [[-1, 0], [0, 1]]))
MainWorkSpace = WorkSpace(40, 40, 600, 500, start, finish, cols, rows, grid, TILE)

ConfigureButton(700, 550, 150, 50, 'Старт', StartEmitting)
ConfigureButton(490, 550, 150, 50, 'Сброс', ClearWorkspace)

while True:
    game_screen.fill((34, 112, 45))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)
