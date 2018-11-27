# --------------------------------------------------------------------------------------------------------
# SNAKES AND LADDERS
# CMPUT 396 - Assignment 5
# November 27, 2018
# ------------------------------------------
# Authors: Imtiaz Raqib
#          Vanessa Peng
# ------------------------------------------
# Language: Python with Pygame module
# --------------------------------------------------------------------------------------------------------


# IMPORTS ---------------------------------
import pygame
import random
import time
#------------------------------------------

# Window Variables
(width, height) = (1200, 800) # Width and Height of the board
res = 70
margin = 10

# Color variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
# ------ GRID COLORS ------
green = (46, 139, 87)
pastelRed = (255, 107, 107)
yellow = (255, 159, 67)
cyan = (10, 189, 227)
blue = (95, 39, 205)

gridColors = [green, pastelRed, yellow, cyan, blue]

# Intializing pygame and Game State ---------------------------------------
pygame.init()
# -------------------------------------------------------------------------

# Image variables
# Cursor pointer ----------------------------------------------------------
point_img = pygame.image.load('pointer.png')
point_img = pygame.transform.scale(point_img, (24, 24))
curs_rect = point_img.get_rect() # get image space, rectangle ulc, lrc coordinates
curs_rect.centerx = (width//2 - 65)
curs_rect.centery = (height//2 + 50)
# -------------------------------------------------------------------------

# Board  ------------------------------------------------------------------
board = pygame.image.load('board.jpg')
board = pygame.transform.scale(board, (800, 800))
board_rect = board.get_rect() # get image space, rectangle ulc, lrc coordinates

# -------------------------------------------------------------------------

# Press Enter  ------------------------------------------------------------
prs_ent = pygame.image.load('roll.png')
prs_ent = pygame.transform.scale(prs_ent, (300, 100))
ent_rect = prs_ent.get_rect() # get image space, rectangle ulc, lrc coordinates
ent_rect.centerx = (1000)
ent_rect.centery = (250)

# -------------------------------------------------------------------------

# Player Tokens  ----------------------------------------------------------
player = pygame.image.load('player.png')
player = pygame.transform.scale(player, (120, 75))
player_rect = player.get_rect()
comp = pygame.image.load('comp.png')
comp = pygame.transform.scale(comp, (120, 75))
comp_rect = comp.get_rect()
# -------------------------------------------------------------------------

# How To Play -------------------------------------------------------------
howtoPlay = pygame.image.load('howtoplay.png')
htp_rect = howtoPlay.get_rect() # get image space, rectangle ulc, lrc coordinates
htp_rect.centerx = (width//2)
htp_rect.centery = (height//2)
# -------------------------------------------------------------------------

# Snakes and Ladders Header -----------------------------------------------
snl_header = pygame.image.load('snlHeader.png')
snl_header = pygame.transform.scale(snl_header, (300, 110))
snlH_rect = snl_header.get_rect() # get image space, rectangle ulc, lrc coordinates
snlH_rect.centerx = (width//2)
snlH_rect.centery = (height//2 - 50)
# -------------------------------------------------------------------------

# Text Types
largeText = pygame.font.Font('freesansbold.ttf', 42)
smallText = pygame.font.Font('freesansbold.ttf', 24)

# Setting up the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snakes and Ladders")
clock = pygame.time.Clock()
pygame.display.flip()

# This is to erase the cursor UI position when moving from PLAY to QUIT and vv
bg = pygame.Surface(screen.get_size())
bg.fill(white)

# Creating a rect out of the text to make easier to position
def text_objects(text, font, g_color):
    textSurface = font.render(text, True, g_color)
    return textSurface, textSurface.get_rect()

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(column)  # Append a cell

# The Main Menu
def game_intro():

    screen.fill(white) #Setting bg color

    # The Text for main menu
    #TextSurf, TextRect = text_objects("Snakes and Ladders", largeText, black)
    TextSurf_p, TextRect_p = text_objects("Play", smallText, black)
    TextSurf_q, TextRect_q = text_objects("Quit", smallText, black)
    TextSurf_h, TextRect_h = text_objects("Press H to see How to play", smallText, red)

    #TextRect.center = ((width//2),(height//2 - 50))
    TextRect_p.center = ((width//2),(height//2 + 50))
    TextRect_q.center = ((width//2),(height//2 + 90))
    TextRect_h.center = ((width//2),(height//2 + 200))

    #screen.blit(TextSurf, TextRect)
    screen.blit(TextSurf_p, TextRect_p)
    screen.blit(TextSurf_q, TextRect_q)
    screen.blit(TextSurf_h, TextRect_h)

    # The UI indicator for PLAY and QUIT
    screen.blit(point_img, curs_rect)
    screen.blit(snl_header, snlH_rect)
    

    intro = True

    while intro:
        # limit runtime speed to 30 frames//second
        clock.tick(30)
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Movement of the cursor UI
        screen.blit(bg, curs_rect, curs_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            curs_rect.centery = height//2 + 50
        if keys[pygame.K_DOWN]:
            curs_rect.centery = height//2 + 88

        if keys[pygame.K_RETURN] and curs_rect.centery == (height//2 + 88):
            pygame.quit()
            quit()

        if keys[pygame.K_RETURN] and curs_rect.centery == (height//2 + 50):
            startGame()

        if keys[pygame.K_h]:
            howTo()
            quit()

        
        screen.blit(point_img, curs_rect)
        pygame.display.flip()

# This function upates the window to show instructions on how to play the game
def howTo():

    intro = True

    while intro:
        # limit runtime speed to 30 frames//second
        clock.tick(30)
        pygame.event.pump()

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)

        # Setting up How to Window

        # --------------- Going Back to Main Menu ---------------------------
        TextSurf_b, TextRect_b = text_objects("Press B to go back to Main Menu", smallText, red)
        TextRect_b.center = ((width//2),(height//2 + 220))
        screen.blit(TextSurf_b, TextRect_b)
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            game_intro()

        # ---------------------------------------------------------------------
        TextSurf_h, TextRect_h = text_objects("How To Play", largeText, black)
        TextRect_h.center = ((width//2),(height//2 - 220))
        screen.blit(TextSurf_h, TextRect_h)

        screen.blit(howtoPlay, htp_rect)

        pygame.display.flip()

# Starting the Game
def startGame():

    intro = True
    
    
    while intro:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            # # User clicks the mouse. Get the position
            #     pos = pygame.mouse.get_pos()
            #     # Change the x/y screen coordinates to grid coordinates
            #     column = pos[0] // (res + margin)
            #     row = pos[1] // (res + margin)
            #     # Set that location to one
            #     grid[row][column] = 1
            #     print("Click ", pos, "Grid coordinates: ", row, column)
    

        screen.fill(black)
        
        # Blitting the board
        screen.blit(board, board_rect)
        screen.blit(prs_ent, ent_rect)
        
        playGame()

        # limit runtime speed to 30 frames//second
        clock.tick(30)
        
        # pygame.display.flip()
        
# Calling compMove and moving the tokens on the board
def playGame():
    p_pos = 0
    if keyPressed(pygame.K_p):
        row, col, num = compMove()
        printDiceRoll(num, 'p')
        screen.blit(player, (((p_pos+col)*(res+margin)), ((row)*(res+margin))))
        p_pos += 3
        pygame.display.update()

    elif keyPressed(pygame.K_c):
        r_ow, c_ol, n_um = compMove()
        printDiceRoll(n_um, 'c')
        screen.blit(comp, ((c_ol*(res+margin)-20), (r_ow*(res+margin))))
        pygame.display.update()

    # screen.blit(comp, ((0*(res+margin)-20), (9*(res+margin))))
    # screen.blit(comp, ((1*(res+margin)-20), (8*(res+margin))))


def compMove():    
    steps = random.randint(1, 6) 
    #Get Quotient = X 
    y = 9 - (steps//10)
    #Get remainder = Y
    x = (steps%10) - 1
    #Steps should be cumulative, whoever reach 100 first, wins

    return y, x, str(steps)

def printDiceRoll(num, var):

    if var == 'p':
        TextSurf_r, TextRect_r = text_objects('Player rolled ' + num, smallText, yellow)
        TextRect_r.center = (1000, 400)
        screen.blit(TextSurf_r, TextRect_r)

    elif var == 'c':
        TextSurf_r, TextRect_r = text_objects('Computer rolled ' + num, smallText, cyan)
        TextRect_r.center = (1000, 500)
        screen.blit(TextSurf_r, TextRect_r)

def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

def key_Pressed(inputKey):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == inputKey:
                return True
# Closing loops and initializations
game_intro()
pygame.quit()
