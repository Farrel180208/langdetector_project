import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Atur ukuran layar
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Posisi tile catur
tile_size = width // 8

# Membuat papan catur kosong
chessboard = [[None for _ in range(8)] for _ in range(8)]

# Inisialisasi posisi awal bidak
# 8 Pawn
for i in range(8):
    chessboard[1][i] = 'P'  # Pawn putih
    chessboard[6][i] = 'p'  # Pawn hitam

# 1 King
chessboard[0][4] = 'K'  # King putih
chessboard[7][4] = 'k'  # King hitam

# 1 Queen
chessboard[0][3] = 'Q'  # Queen putih
chessboard[7][3] = 'q'  # Queen hitam

# 2 Bishop
chessboard[0][2] = 'B'  # Bishop putih
chessboard[0][5] = 'B'
chessboard[7][2] = 'b'  # Bishop hitam
chessboard[7][5] = 'b'

# 2 Knight
chessboard[0][1] = 'N'  # Knight putih
chessboard[0][6] = 'N'
chessboard[7][1] = 'n'  # Knight hitam
chessboard[7][6] = 'n'

# 2 Rook
chessboard[0][0] = 'R'  # Rook putih
chessboard[0][7] = 'R'
chessboard[7][0] = 'r'  # Rook hitam
chessboard[7][7] = 'r'

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gambar papan catur
    for row in range(8):
        for col in range(8):
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (col * tile_size, row * tile_size, tile_size, tile_size))
            piece = chessboard[row][col]
            if piece:
                # Menambahkan gambar bidak sesuai dengan jenisnya (Anda perlu menambahkan gambar bidak yang sesuai)
                # Misalnya, Anda dapat menggunakan gambar PNG untuk setiap jenis bidak
                piece_image = pygame.image.load(f'images/{piece}.png')
                screen.blit(piece_image, (col * tile_size, row * tile_size))

    pygame.display.update()

pygame.quit()
sys.exit()
