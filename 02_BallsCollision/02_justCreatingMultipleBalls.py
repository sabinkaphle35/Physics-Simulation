import pygame
from random import randint
import random
import math

#initialize pygame
pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("multiple balls")

#Class Ball
class Ball:
    def __init__(self, x, y, radius, color, screen, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.velocity_x = velocity
        self.velocity_y = velocity
    def drawBall(self):
        pygame.draw.circle(self.screen, self.color,(self.x,self.y), self.radius)

    def moveBall(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

        if self.x + self.radius >= width or self.x - self.radius <= 0:
            self.velocity_x = -self.velocity_x
        if self.y + self.radius >= height or self.y - self.radius <= 0:
            self.velocity_y = -self.velocity_y

    def checkCollision(self, otherball):
        distance = math.sqrt((self.x - otherball.x)**2 + (self.y - otherball.y)**2)

        if distance <= self.radius + otherball.radius:
            return True
        return False
    
    def handleCollision(self, otherBall):
        distance = math.sqrt((self.x - otherBall)**2 + (self.y - otherBall.y)**2)

        if distance <= self.radius + otherBall.radius:
            pass


balls = []
for _ in range(20):
    x = randint(50, 500)
    y = randint(50, 500)
    radius = randint(10, 20)
    color = random.choice(["red", "green", "blue", "yellow", "purple"])
    velocity = 1
    print(color)
    balls.append(Ball(x, y, radius, color, screen,1))


#window
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    for ball in balls:
        ball.drawBall()
        ball.moveBall()
    
    pygame.display.update()
