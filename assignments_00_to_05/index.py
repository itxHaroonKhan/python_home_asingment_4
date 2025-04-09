import pygame

pygame.init()

# Screen size and grid settings
canva_width = 400
canva_height = 400
cell_size = 40
eraser_size = 20

# Colors
blue_color = (0, 0, 255)
white_color = (255, 255, 255)

# Pygame screen setup
screen = pygame.display.set_mode((canva_width, canva_height))
pygame.display.set_caption("Pygame Game")

# Creating grid
grid = []
for row in range(0, canva_height, cell_size):
    for col in range(0, canva_width, cell_size):
        rect = pygame.Rect(col, row, cell_size, cell_size)
        grid.append(rect)

# Eraser setup
eraser = pygame.Rect(0, 0, eraser_size, eraser_size)

# Game loop
running = True
while running:
    screen.fill(white_color)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw filled grid (full blue)
    for rect in grid:
        pygame.draw.rect(screen, blue_color, rect)  # <-- Border thickness removed

    # Eraser follows mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.center = (mouse_x, mouse_y)

    # Remove cells that collide with eraser
    grid = [rect for rect in grid if not eraser.colliderect(rect)]

    # Draw eraser
    pygame.draw.rect(screen, (255, 0, 0), eraser)

    # Update display
    pygame.display.flip()
    pygame.time.delay(50)  # Reduce CPU usage

pygame.quit()
