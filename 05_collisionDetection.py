import pygame
import math

#initialize pygame
pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("collision detection")
color = pygame.Color("white")
print(color)


#properites of balls
ball_1_radius = ball_2_radius = 20
#position of ball 1
xPostion_1 = ball_1_radius +1
yPostion_1 = height - ball_1_radius 
#color of ball 1
color_1 = pygame.Color("red")

#position of ball2
xPostion_2 = width - ball_2_radius -1
yPostion_2 = height - ball_2_radius 
#color of ball 2
color_2 = pygame.Color("green")

#change in positio x
dx = 2





#window loop to run until quit
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if(xPostion_2 + ball_2_radius>= width and xPostion_1 - ball_1_radius <= 0):
        dx = -dx
        print("out of bound")
    
    
    distance = math.sqrt((xPostion_2 - xPostion_1)**2 + (yPostion_2 - yPostion_1)**2)
    
    if distance <= ball_1_radius*2:
        dx = - dx

    xPostion_1 += dx
    xPostion_2 -= dx
    screen.fill(color)
    
    #ball one
    pygame.draw.circle(screen,color_1,(xPostion_1, yPostion_1), ball_1_radius)
    #ball two
    pygame.draw.circle(screen, color_2, (xPostion_2, yPostion_2), ball_2_radius)
    
    pygame.display.update()
    pygame.time.Clock().tick(60)