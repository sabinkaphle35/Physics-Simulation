import pygame

#initialize pygame
pygame.init()

width = 500
height = 500
caption = "circle"

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(caption)

colorOfScreen = pygame.Color("white")

#coordinates for circle(ball)
x = width /2
y = 40

#radius of ball
radius = 10

#color of ball
ballColor = pygame.Color("red")

#running window until closed
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #fill screen color in each frame
    screen.fill(colorOfScreen)

    #drawing circle
    pygame.draw.circle(screen, ballColor, (x,y), radius)

    #update display in each frame
    pygame.display.update()