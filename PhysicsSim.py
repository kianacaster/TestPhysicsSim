import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Simulator")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw a circle (example object)
    pygame.draw.circle(screen, BLUE, (400, 300), 50)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()