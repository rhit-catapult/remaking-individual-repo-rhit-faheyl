import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Setup Test")

# Colors
WHITE = (255, 255, 255)
RED = (50, 50, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (350, 350, 100, 100)) # Draw a blue square
    pygame.draw.rect(screen, RED, (250, 250, 300, 100))  # Draw a blue square
    pygame.draw.rect(screen, RED, (150, 150, 500, 100))  # Draw a blue square
    pygame.draw.rect(screen, RED, (250, 50, 100, 100))  # Draw a blue square
    pygame.draw.rect(screen, RED, (450, 50, 100, 100))  # Draw a blue square
    # Update the display
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
