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

#for moving circle we need speed or velocity, time, acceleration
acceleration = 0.001
initialVelocity = 0
timeInterval = 1
velocity = initialVelocity
print(velocity)


#running window until closed
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #fill screen color in each frame
    screen.fill(colorOfScreen)

    #update velocity
    velocity += acceleration * timeInterval
    # print(velocity)
    y = y+velocity
    #updating the position of ball in y-axis 
    

    #drawing circle
    pygame.draw.circle(screen, ballColor, (x,y), radius)
    print(f"({x}, {y})")
    #update display in each frame
    pygame.display.update()

