import pygame
from .constants import BLACK
from .piece import *

top_left_x = (SCREEN_WIDTH - BOARD_WIDTH) / 2
top_left_y = (SCREEN_HEIGHT - BOARD_HEIGHT) / 2
player1_x = (top_left_x - 360) / 2
player_y = 60
player2_x = top_left_x + BOARD_WIDTH + player1_x

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.player1 = self.player2 = 0
        #self.create_board()

    def draw_board(self, win):
        win.fill(BLACK)
    
    def winner(self):       
        return None 

    def player_grid(self, screen, player1, player2):
        player_grid = [[[] for x in range(42)] for x in range(18)]
        k = 0

        for i in range(len(player_grid)):
            for j in range(len(player_grid[i])):
                if i % 6 == 2 and j % 6 == 2:
                    player1_piece = Piece(player1_x + i*RESERVE_SIZE, player_y + j*RESERVE_SIZE, player1[k], COLOR1, RESERVE_SIZE)
                    player2_piece = Piece(player2_x + i*RESERVE_SIZE, player_y + j*RESERVE_SIZE, player2[k], COLOR2, RESERVE_SIZE)
                    if player_str[k] in player1_reserves:
                        player1_piece.draw_shape(screen)
                    if player_str[k] in player2_reserves:
                        player2_piece.draw_shape(screen)
                    k += 1

    def game_grid(self, board_pieces = {}):
        # Make all grid positions black
        grid = [[(0,0,0) for _ in range(14)] for _ in range(14)]

        # Iterate through grid, if key is found in board_pieces, change corresponding grid pos to player1/2 color
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j,i) in board_pieces:
                    c = board_pieces[(j,i)]
                    grid[i][j] = c
        return grid

    def draw_grid(self, surface, row, col):
    # This function draws the grey grid lines
        sx = top_left_x
        sy = top_left_y

        for i in range(row):
            pygame.draw.line(surface, (128,128,128), (sx, sy+ i * BLOCK_SIZE), (sx + BOARD_WIDTH, sy + i * BLOCK_SIZE))  # horizontal lines
            for j in range(col):
                pygame.draw.line(surface, (128,128,128), (sx + j * BLOCK_SIZE, sy), (sx + j * BLOCK_SIZE, sy + BOARD_HEIGHT))  # vertical lines


    def draw_window(self, surface):
        surface.fill((0, 0, 0))

        pygame.font.init()
        font = pygame.font.SysFont('comicsans', 30)
        label1 = font.render('Player 1', 1, (255,255,255))
        label2 = font.render('Player 2', 1, (255,255,255))

        surface.blit(label1, (150, 30))
        surface.blit(label2, (SCREEN_WIDTH - top_left_x / 2, 30))

        board = Board()
        board.player_grid(surface, player_list, player_list)

        #for i in range(len(grid)):
        #    for j in range(len(grid[i])):
        #        pygame.draw.rect(surface, grid[i][j], (top_left_x + j*BLOCK_SIZE, top_left_y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        #pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, BOARD_WIDTH, BOARD_HEIGHT), 3)

        #draw_grid(surface, 14, 14)