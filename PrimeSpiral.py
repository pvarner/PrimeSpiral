# import pygame module in this program
from math import isqrt
from os import stat
import pygame
import enum


class state(enum.Enum):
    right = 1
    up = 2
    left = 3
    down = 4


 
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
 
# assigning values to X and Y variable
X = 1000
Y = 1000

x_index = X // 2
y_index = Y // 2

 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Prim Spiral')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 16 )

curState = state.right
distanceCounter = 0
distance = 0
num = 0

# Config variables
rectSize = 5
numSpacing = 5 
turnsToTake = 500


def isPrime(num):
    for i in range(2,isqrt(num) + 2):
        if num % i == 0 and num != i:
            return True

    return False


def drawNum(num):
    global x_index
    global y_index

    text = font.render(str(num), True, black)
    
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (x_index, y_index)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    if not isPrime(num):
        display_surface.blit(text, textRect)


def drawSquare(num):
    global x_index
    global y_index
    
    text = font.render(str(num), True, black)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    if not isPrime(num):
        pygame.draw.rect(display_surface, black, pygame.Rect( x_index, y_index, rectSize, rectSize ))
        pygame.display.flip()
    

def calcNumbers():
    global x_index
    global y_index
    global state
    global distanceCounter
    global distance
    global num
    global curState
    global numSpacing
    global turnsToTake


    # completely fill the surface object
    # with white color
    display_surface.fill(white)

    for i in range(turnsToTake):
        # check to see if we need to increase the amount of number on the row/col, should increase every other time
        if distanceCounter % 2 == 0:
            distance = distance + 1

        distanceCounter = distanceCounter + 1

        for i in range(distance):
            num = num + 1

            #drawNum(num)
            drawSquare(num)

            # adjust index to place the next number base on current direction
            if curState == state.right:
                x_index = x_index + numSpacing
            elif curState == state.up:
                y_index = y_index - numSpacing
            elif curState == state.left:
                x_index = x_index - numSpacing
            elif curState == state.down:
                y_index = y_index + numSpacing



        # adjust index to place the next number base on current direction
        if curState == state.right:
            curState = state.up
        elif curState == state.up:
            curState = state.left
        elif curState == state.left:
            curState = state.down
        elif curState == state.down:
            curState = state.right
        

 

calcNumbers()

 
# infinite loop
while True:
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()



