import pygame

#initialize pygame
pygame.init()

width = 500
height = 500
caption = "circle"

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(caption)
clock = pygame.time.Clock()
colorOfScreen = pygame.Color("white")

#coordinates for circle(ball)
x = width /2
y = 40

#radius of ball
radius = 10

#color of ball
ballColor = pygame.Color("red")

#for moving circle we need speed or velocity, time, acceleration
acceleration = 0.5
initialVelocity = 0.1
timeInterval = 1
velocity = initialVelocity
print(velocity)
vNew = 0


#running window until closed
run = True
ballstopped = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if velocity != 0:
    #fill screen color in each frame
        screen.fill(colorOfScreen)

        #update velocity
    
        velocity += acceleration * timeInterval
        

        #updating the position of y
        y = y+velocity
        
        #if the ball hits the ground
        if (y + radius >= height):
            velocity = - velocity 
            # making sure ball doesnt goes radius out of bound
            y = height - radius
            print((velocity))
        if abs(velocity) < 2.1 and y + radius >= height:
            velocity = 0
            print(velocity)
            
        
        #drawing circle
        pygame.draw.circle(screen, ballColor, (x,y), radius)

    else:
        screen.fill(colorOfScreen)
        pygame.draw.circle(screen, ballColor, (x,y), radius)

    # print(f"({x}, {y})")
    #update display in each frame
    pygame.display.update()
    clock.tick(60)

