from tkinter.tix import ROW
import pygame
import button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
LOWER_MARGIN = 100
RIGHT_MARGIN = 16

screen = pygame.display.set_mode((SCREEN_WIDTH + RIGHT_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')

#define game variables
ROWS = 50
COLUMNS = 80
TILE_SIZE = 16
FPS = 60
clock = pygame.time.Clock()

#load images
grass_img = pygame.image.load('textures/background/grass_img.jpg').convert_alpha()
black_img = pygame.image.load('textures/black_img.jpg').convert_alpha()
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

#create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLUMNS
    world_data.append(r)

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
        
#draw grid
def draw_grid():
    #vertical lines
    for c in range(COLUMNS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT))
    for c in range(ROWS + 1): #+2 makes a line along bottom margin
        pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))

#functionf or drawing world tiles
def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                print(tile)
                road_tile = pygame.image.load(f'textures/{tile}.jpg')
                screen.blit(road_tile, (x * TILE_SIZE, y *TILE_SIZE))

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

#create buttons
#make a button list
button_list = []
button_col = 0
button_row = 0

screen.fill(BLACK)
draw_bg()
draw_world()
# draw_grid()
pygame.display.update()

run = True
while run:

    clock.tick(FPS)





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

    if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[2] == 1: #Refreshes display only when a user presses their left or right mouse buttons
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
            #update tile value
            if pygame.mouse.get_pressed()[0] == 1:
                world_data[y][x] = image_index(x, y)
            if pygame.mouse.get_pressed()[2] == 1:
                world_data[y][x] = -1
        draw_bg()
        draw_world()
        # draw_grid()
        pygame.display.update()


pygame.quit()