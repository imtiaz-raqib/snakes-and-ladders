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

# ------ SET THE SPEED OF THE GAME --------
SPEED = 3
# -----------------------------------------

# Window Variables
(width, height) = (1200, 800) # Width and Height of the board
res = 70
margin = 10

# Color variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (46, 139, 87)
pastelRed = (255, 107, 107)
yellow = (255, 159, 67)
cyan = (10, 189, 227)
blue = (95, 39, 205)

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

''' This function upates the window to show instructions on how to play the game '''
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
    c = 0
    player_switcher = 0 # Even number is Player 2 and Odd number is Player 1

    while intro:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        screen.fill(black)
        
        # Blitting the board
        screen.blit(board, board_rect)

        # Run until total number of steps (i.e. c) < 100
        if c < 100:
            row, col, num, c = compMove(c)
            # incrementing c with the roll on the die as the number to move
            c += int(num)

            # Checking to see if the players hit anything and printing the ---
            # appropriate message
            c1, check_bool = checkSnl(c)
            if check_bool == True and c1 > c and player_switcher%2==0:
                print_message('c', 'ladder')
                c = c1
            
            elif check_bool == True and c1 > c and player_switcher%2!=0:
                print_message('p', 'ladder')
                c = c1

            elif check_bool == True and c1 < c and player_switcher%2==0:
                print_message('c', 'snake')
                c = c1
            
            elif check_bool == True and c1 < c and player_switcher%2!=0:
                print_message('p', 'snake')
                c = c1
            # -----------------------------------------------------------------

            elif player_switcher % 2 != 0:
                printDiceRoll(num, 'p')
                playGame(row, col, c, 'player')
            
            elif player_switcher % 2 == 0:
                printDiceRoll(num, 'c')
                playGame(row, col, c, 'comp')

            player_switcher += 1
        
        # Check to see if the game is over
        elif c >= 100:
            
            if player_switcher % 2 == 0:
                victory_message('c', comp, (1000, 250))
            elif player_switcher % 2 != 0:
                victory_message('p', player, (1000, 250))

# Calling compMove and moving the tokens on the board -------------------------------------------------------------
def playGame(row, col, c, p):
    global SPEED
    # print('Row: ' + str(row) + '  Col: ' + str(col) + '  Num: ' + num)
    if p == 'player':
        screen.blit(player, ((col*(res+margin)), (row*(res+margin))))
    
    elif p == 'comp':
        screen.blit(comp, ((col*(res+margin)), (row*(res+margin))))
    # limit runtime speed to 30 frames//second
    clock.tick(SPEED)
    pygame.display.update()
# ------------------------------------------------------------------------------------------------------------------

# Using checkSnl() and printing what the player hit in the board --------------------------------------------------
def print_message(player, type):

    if type == 'ladder':
        if player == 'p':
            TextSurf_r, TextRect_r = text_objects('Player 1 climbed a ladder!', smallText, yellow)
            TextRect_r.center = (1000, 600)
            screen.blit(TextSurf_r, TextRect_r)

        elif player == 'c':
            TextSurf_r, TextRect_r = text_objects('Player 2 climbed a ladder!', smallText, cyan)
            TextRect_r.center = (1000, 700)
            screen.blit(TextSurf_r, TextRect_r)

    elif type == 'snake':
        if player == 'p':
            TextSurf_r, TextRect_r = text_objects('Player 1 was bitten by a snake!!!', smallText, yellow)
            TextRect_r.center = (1000, 600)
            screen.blit(TextSurf_r, TextRect_r)

        elif player == 'c':
            TextSurf_r, TextRect_r = text_objects('Player 2 was bitten by a snake!!!', smallText, cyan)
            TextRect_r.center = (1000, 700)
            screen.blit(TextSurf_r, TextRect_r)

    pygame.display.flip()
# -----------------------------------------------------------------------------------------------------------------

# Computing the movement of the players within the board ----------------------------------------
def compMove(c):   
    steps = random.randint(1, 6)
    #Get Quotient = Y 
    y = 9 - (c //10)
    #Get remainder = X
    x = (c % 10) - 1
    #Steps should be cumulative, whoever reach 100 first, wins

    return y, x, str(steps), c
# -----------------------------------------------------------------------------------------------

# Checking to see if the roll made the player hit a Snake or Ladder ---------------------------
def checkSnl(c):

    # LADDERS ---------
    if c == 3: 
        c = 51
    
    elif c == 6:  
        c = 27
    
    elif c == 20: 
        c = 70
    
    elif c == 36: 
        c = 55
    
    elif c == 63: 
        c = 95

    elif c == 68:
        c = 98
    # -----------------
    # SNAKES ----------
    elif c == 34:
        c = 1

    elif c == 25:
        c = 5

    elif c == 47:
        c = 19
    
    elif c == 65:
        c = 52
    
    elif c == 87:
        c = 57
    
    elif c == 91:
        c = 61
    
    elif c == 99:
        c = 69
    # -----------------
    return c, True
# -----------------------------------------------------------------------------------------------

# Printing the random number generated as a dice roll -------------------------------------------
def printDiceRoll(num, var):

    if var == 'p':
        TextSurf_r, TextRect_r = text_objects('Player rolled a ' + num, smallText, yellow)
        TextRect_r.center = (1000, 400)
        screen.blit(TextSurf_r, TextRect_r)

    elif var == 'c':
        TextSurf_r, TextRect_r = text_objects('Computer rolled a ' + num, smallText, cyan)
        TextRect_r.center = (1000, 500)
        screen.blit(TextSurf_r, TextRect_r)
# -----------------------------------------------------------------------------------------------

# Printing the winner of the game ---------------------------------------------------------------
def victory_message(winningPlayer, image, image_rect):
    
    if winningPlayer == 'p':
        TextSurf_r, TextRect_r = text_objects('Player 1 won \(-_-)/', largeText, pastelRed)
        TextRect_r.center = (1000, 200)
        screen.blit(TextSurf_r, TextRect_r)

    elif winningPlayer == 'c':
        TextSurf_r, TextRect_r = text_objects('Player 2 won \(-_-)/', largeText, pastelRed)
        TextRect_r.center = (1000, 200)
        screen.blit(TextSurf_r, TextRect_r)
    
    screen.blit(image, image_rect)
    pygame.display.flip()
# -----------------------------------------------------------------------------------------------

# Closing loops and initializations
game_intro()
pygame.quit()