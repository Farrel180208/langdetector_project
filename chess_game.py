import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ukuran layar
WIDTH, HEIGHT = 800, 800

# Membuat layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game Catur')

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Warna latar belakang
    screen.fill(WHITE)

    # Tampilkan hasil layar
    pygame.display.flip()
