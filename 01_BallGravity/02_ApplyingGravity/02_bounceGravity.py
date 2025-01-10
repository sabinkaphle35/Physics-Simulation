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
radius = 20

#color of ball
ballColor = pygame.Color("red")

#for moving circle we need speed or velocity, time, acceleration
acceleration = 0.5
initialVelocity = 0.1
timeInterval = 1
velocity = initialVelocity
vNew = 0
coofOfRestitution_e = 0.8


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

        #update velocity in each time interval
        velocity += acceleration * timeInterval
        

        #updating the position of y
        y = y+velocity
        # print(f"velocity Before Collision: {velocity}")
        #if the ball hits the ground
        if (y + radius >= height):
            # e = velocity after collision / velocity before collision
            vNew = - velocity * coofOfRestitution_e #if ball goes out of bound velocity is in -
            # making sure ball doesnt goes radius out of bound
            velocity = vNew
            y = height - radius
            # print(f"velocity After Collision: {vNew}")

        if abs(velocity) < 0.1 and y + radius >= height:
            velocity = 0
            # print(velocity)

            
        
        #drawing circle
        pygame.draw.circle(screen, ballColor, (x,y), radius)

    else:
        screen.fill(colorOfScreen)
        pygame.draw.circle(screen, ballColor, (x,y), radius)

    # print(f"({x}, {y})")
    #update display in each frame
    pygame.display.update()
    clock.tick(60)

