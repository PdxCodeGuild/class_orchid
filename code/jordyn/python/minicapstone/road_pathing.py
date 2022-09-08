from pickle import FALSE
import random
from re import A
import pygame
import button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
LOWER_MARGIN = 98
RIGHT_MARGIN = 16

screen = pygame.display.set_mode((SCREEN_WIDTH + RIGHT_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')

#define game variables
ROWS = 50
COLUMNS = 80
TILE_SIZE = 16
FPS = 144
clock = pygame.time.Clock()
current_tile = 0

#load images
grass_img = pygame.image.load('textures/background/grass_img.jpg').convert_alpha()
black_img = pygame.image.load('textures/black_img.jpg').convert_alpha()
start_img = pygame.image.load('textures/start_point.jpg').convert_alpha()
end_img = pygame.image.load('textures/end_point.jpg').convert_alpha()

#button images
road_place_img_button = pygame.image.load('textures/15.jpg').convert_alpha()
start_img_button = pygame.image.load('textures/start_point.jpg').convert_alpha()
end_img_button = pygame.image.load('textures/end_point.jpg').convert_alpha()
start_button = pygame.image.load('textures/start_button.jpg').convert_alpha()
road_place_img_button = pygame.transform.scale(road_place_img_button, (TILE_SIZE * 4, TILE_SIZE * 4))
start_img_button = pygame.transform.scale(start_img_button, (TILE_SIZE * 4, TILE_SIZE * 4))
end_img_button = pygame.transform.scale(end_img_button, (TILE_SIZE * 4, TILE_SIZE * 4))

image_list = [road_place_img_button, start_img_button, end_img_button, start_button]
#create buttons
#make a button list
button_list = [] #these do nothing yet
button_row = 0
for i in range(len(image_list)):
    tile_button = button.Button(16 + (80 * button_row), SCREEN_HEIGHT + 16, image_list[i]) #draws buttons in specific spaces
    button_row += 1
    button_list.append(tile_button)

WHITE = (255, 255, 255)
BLACK = (100, 100, 100)

#create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLUMNS
    world_data.append(r)

world_visit = []
for row in range(ROWS):
    r = [False] * COLUMNS
    world_visit.append(r)

#create function for drawing background
def draw_bg():
    column = 0
    row = 0
    while column < SCREEN_HEIGHT:
        screen.blit(grass_img, (row, column))
        row += 16
        if row == SCREEN_WIDTH:
            column += 16
            row = 0
        
#used to remove tiles from world
def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                road_tile = pygame.image.load(f'textures/{tile}.jpg').convert_alpha()
                screen.blit(road_tile, (x * TILE_SIZE, y *TILE_SIZE))

def draw_cardinal(x, y): #Draws and updates tiles around cursor
    tile = world_data[y][x] #current
    if tile >= 0:
        if tile <= 15:
            road_tile = pygame.image.load(f'textures/{tile}.jpg').convert_alpha()
            screen.blit(road_tile, (x * TILE_SIZE, y *TILE_SIZE))

    if tile == -1:
        screen.blit(grass_img, (x * TILE_SIZE, y *TILE_SIZE))
    
    if tile == 16: #places start point
        screen.blit(start_img, (x * TILE_SIZE, y * TILE_SIZE))
    
    if tile == 17: #places end point
        screen.blit(end_img, (x *TILE_SIZE, y * TILE_SIZE))

    if x != 0: #left
        if world_data[y][x-1] >= 0:
            world_data[y][x-1] = image_index(x-1, y)
            tile = world_data[y][x-1]
            if tile <= 15:
                road_tile = pygame.image.load(f'textures/{tile}.jpg').convert_alpha()
                screen.blit(road_tile, ((x - 1) * TILE_SIZE, y *TILE_SIZE))

    if y != 0: #up
        if world_data[y - 1][x] >= 0:
            world_data[y-1][x] = image_index(x, y-1)
            tile = world_data[y-1][x]
            if tile <= 15:
                road_tile = pygame.image.load(f'textures/{tile}.jpg').convert_alpha()
                screen.blit(road_tile, (x * TILE_SIZE, (y-1) *TILE_SIZE))

        
    if x <= (COLUMNS -2): #right
        if world_data[y][x+1] >= 0:
            world_data[y][x+1] = image_index(x+1, y)
            tile = world_data[y][x+1]
            if tile <= 15:
                road_tile = pygame.image.load(f'textures/{tile}.jpg').convert_alpha()
                screen.blit(road_tile, ((x + 1) * TILE_SIZE, y *TILE_SIZE))
    
    if y <= (ROWS -2): #down
        if world_data[y + 1][x] >= 0:
            world_data[y+1][x] = image_index(x, y+1)
            tile = world_data[y+1][x]
            if tile <= 15:
                road_tile = pygame.image.load(f'textures/{tile}.jpg').convert_alpha()
                screen.blit(road_tile, (x * TILE_SIZE, (y+1) *TILE_SIZE))
                
def image_index(x, y):
    '''Returns value based on surrounding road tiles
    West = 1
    North = 2
    East = 4
    South = 8'''
    index = 0
    
    if x != 0: #West
        if world_data[y][x-1] >= 0:
            index += 1

    if y != 0: #North
        if world_data[y - 1][x] >= 0: #Checks if a road exists at north position
            index += 2
        
    if x <= (COLUMNS -2): #East
        if world_data[y][x+1] >= 0:
            index += 4
    
    if y <= (ROWS -2): #South
        if world_data[y + 1][x] >= 0:
            index += 8
    return index


def find_path(): #finds path from green to red
    x, y = find_start()
    stack = [[x,y]]
    world_visit[y][x] = True
    while len(stack) > 0:
        if not world_visit[y][x]:
            world_visit[y][x] = True
            stack.append([x,y])
        a, z = direction(x, y)
        print(stack)
        if a == x and z == y:
            stack.pop()
            if len(stack) > 0:
                x = stack[-1][0]
                y = stack[-1][1]
                print('poppped')
        else:
            if world_data[a][z] == 17:
                print('path found!')
            else:
                x = a
                y = z

def find_start(): #Finds your start point by searching the entire list
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile == 16:
                return x, y
    return 0, 0

def direction(x,y): #Randomises the directions it will search in until one is availble, returning that coordinate value to direct the path finder
    directions = ['left', 'right', 'up', 'down']
    random.shuffle(directions)
    for direc in (directions):
        if direc == 'left':
            if x != 0: #left
                if world_data[y][x-1] >= 0 and world_visit[y][x-1] == False:
                    return x-1, y
        elif direc == 'up':
            if y != 0: #up
                if world_data[y-1][x] >= 0 and world_visit[y-1][x] == False:
                    return x, y-1
        elif direc == 'down':
            if y <= (ROWS -2): #down
                if world_data[y+1][x] >= 0 and world_visit[y+1][x] == False:
                    return x, y+1
        elif direc == 'right':
            if x <= (COLUMNS -2): #right
                if world_data[y][x+1] >= 0 and world_visit[y][x+1] == False:
                    return x+1, y
    return x, y

screen.fill(BLACK)
draw_bg()
pygame.display.update()
runnable = True
run = True
while run:
    clock.tick(FPS)

    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(screen):
            current_tile = button_count

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #add new tiles to screen
    #get mouse position
    pos = pygame.mouse.get_pos()
    x = pos[0] // TILE_SIZE
    y = pos[1] // TILE_SIZE
    #check that coodinates are within tile area

    if current_tile == 3 and runnable == True:
        find_path()
        runnable = False
    elif current_tile != 3:
        runnable = True

    if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[2] == 1: #Refreshes display only when a user presses their left or right mouse buttons
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
            #update tile value
            if pygame.mouse.get_pressed()[0] == 1:
                if current_tile == 0:
                    world_data[y][x] = image_index(x, y)
                    draw_cardinal(x,y)
                elif current_tile == 1:
                    world_data[y][x] = 16
                    draw_cardinal(x,y)
                elif current_tile == 2:
                    world_data[y][x] = 17
                    draw_cardinal(x,y)

            if pygame.mouse.get_pressed()[2] == 1:
                world_data[y][x] = -1
                draw_cardinal(x, y)

    pygame.display.update()

pygame.quit()

#draw grid
# def draw_grid():
#     #vertical lines
#     for c in range(COLUMNS + 1):
#         pygame.draw.line(screen, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
#     for c in range(ROWS + 1): #+2 makes a line along bottom margin
#         pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))