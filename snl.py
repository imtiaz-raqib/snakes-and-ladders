import pygame
import random
import time
import sys


# Creating a rect out of the text to make easier to position
def text_objects(text, font, g_color):
    textSurface = font.render(text, True, g_color)
    return textSurface, textSurface.get_rect()


def game_intro():

    screen.fill(white) #Setting bg color

    # The Text for main menu
    #TextSurf, TextRect = text_objects("Snakes and Ladders", largeText, black)
    TextSurf_p, TextRect_p = text_objects("Play", smallText, black)
    TextSurf_q, TextRect_q = text_objects("Quit", smallText, black)
    TextSurf_h, TextRect_h = text_objects("Hold H to see How to play", smallText, red)

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

def howTo():

    screen.fill(white)

    # Setting up How to Window

    # --------------- Going Back to Main Menu ---------------------------
    # TextSurf_b, TextRect_b = text_objects("Press B to go back to Main Menu", smallText, red)
    # TextRect_b.center = ((width//2),(height//2 + 220))
    # screen.blit(TextSurf_b, TextRect_b)

    # ---------------------------------------------------------------------
    TextSurf_h, TextRect_h = text_objects("How To Play", largeText, black)
    TextRect_h.center = ((width//2),(height//2 - 220))
    screen.blit(TextSurf_h, TextRect_h)

    screen.blit(howtoPlay, htp_rect)

def createBoard():

    screen.fill(black)
        
    # Blitting the board
    screen.blit(board, board_rect)


# Initializing ------------------------------------------------------------
pygame.init()
# -------------------------------------------------------------------------

width = 1200
height = 800

clock = pygame.time.Clock()

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

# Text Types
largeText = pygame.font.Font('freesansbold.ttf', 42)
smallText = pygame.font.Font('freesansbold.ttf', 24)

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


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snakes and Ladders")

done = False

while not done:

    game_intro()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        curs_rect.centery = height//2 + 50
    if keys[pygame.K_DOWN]:
        curs_rect.centery = height//2 + 88

    if keys[pygame.K_RETURN] and curs_rect.centery == (height//2 + 88):
        pygame.quit()
        quit()

    if keys[pygame.K_h]:
        howTo()
    
    if keys[pygame.K_RETURN] and curs_rect.centery == (height//2 + 50):
        createBoard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    

    clock.tick(30)
    pygame.display.update()