import pygame
import sys
import random

from pygame import MOUSEBUTTONDOWN


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speedx = random.randint(-10, 10)
        self.speedy = random.randint(-10, 10)
        self.lifetime = 0
        self.radius = random.randint(9, 21)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def move(self):
        self.x = self.speedx + self.x
        self.y = self.speedy + self.y
        if self.y + self.radius >= self.screen.get_height():
            self.speedy = -self.speedy
        if self.x + self.radius >= self.screen.get_width():
            self.speedx = -self.speedx
        if self.x - self.radius <= 0:
            self.speedx = -self.speedx
        if self.y - self.radius <= 0:
            self.speedy = -self.speedy
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    def shrink(self):
        shrink_rate = 1000
        self.radius = self.radius - shrink_rate * time.time()+shrink_rate * time.time.init


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('white'))
    clock = pygame.time.Clock()


    balls = []

    # TODO: Create an instance of the Ball class called ball1
    while True:

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            balls.append(Ball(screen, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            print("ball")



        clock.tick(60)
        screen.fill(pygame.Color('white'))

        # TODO: Move the ball
        # TODO: Draw the ball
        for ball in balls:
            ball.draw()
            ball.move()
            

        pygame.display.update()

main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
