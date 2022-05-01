import pygame
import random
import os
from .constants import BLACK
from .piece import *

top_left_x = (SCREEN_WIDTH - BOARD_WIDTH) / 2
top_left_y = (SCREEN_HEIGHT - BOARD_HEIGHT) / 2
player1_x = (top_left_x - 360) / 2
player_y = 60
player2_x = top_left_x + BOARD_WIDTH + player1_x

class Board:
    def __init__(self, surface, turn, selected_piece):
        self.surface = surface
        self.turn = turn
        self.selected_piece = selected_piece      
    
    def update(self):
        self.draw_window(self.surface)
        pygame.display.update()

    def player_reserves(self, screen, piece_list):
        player_grid = [[[] for x in range(42)] for x in range(18)]
        k = 0

        for i in range(len(player_grid)):
            for j in range(len(player_grid[i])):
                if i % 6 == 2 and j % 6 == 2:
                    if player_str[k] in player1_reserves:
                        p1_piece_name = Piece(player1_x + i*RESERVE_SIZE, player_y + j*RESERVE_SIZE, piece_list[k], piece_corners_list[k], COLOR1, RESERVE_SIZE)
                        p1_piece_name.draw_shape(screen)
                    if player_str[k] in player2_reserves:
                        p2_piece_name = Piece(player2_x + i*RESERVE_SIZE, player_y + j*RESERVE_SIZE, piece_list[k], piece_corners_list[k], COLOR2, RESERVE_SIZE)
                        p2_piece_name.draw_shape(screen)
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
        
        x_pic_image = pygame.image.load(os.path.join('assets', 'x_pic.png'))
        x_pic = pygame.transform.scale(x_pic_image, (BLOCK_SIZE - 6, BLOCK_SIZE - 6))

        for i in range(row):
            pygame.draw.line(surface, (128,128,128), (sx, sy+ i * BLOCK_SIZE), (sx + BOARD_WIDTH, sy + i * BLOCK_SIZE))  # horizontal lines
            for j in range(col):
                pygame.draw.line(surface, (128,128,128), (sx + j * BLOCK_SIZE, sy), (sx + j * BLOCK_SIZE, sy + BOARD_HEIGHT))  # vertical lines
                # Draws x on starting pos
                if (i == 4 and j == 4) or (i == 9 and j == 9):
                    surface.blit(x_pic, (sx + j * BLOCK_SIZE + 3, sy + i * BLOCK_SIZE + 3))
    
    def draw_dragged_piece(self, surface):
        if self.turn == 1:
            color = COLOR1
        elif self.turn == 2:
            color = COLOR2
        
        origin_x, origin_y = pygame.mouse.get_pos()
        origin_x -= BLOCK_SIZE // 2
        origin_y -= BLOCK_SIZE // 2
        pygame.draw.rect(surface, color, self.selected_piece.x)
        pygame.draw.rect(surface, WHITE, self.selected_piece.y, 1)


    def draw_window(self, surface):
        surface.fill((0, 0, 0))

        font = pygame.font.SysFont('comicsans', 30)
        label1 = font.render('Player 1', 1, WHITE)
        label2 = font.render('Player 2', 1, WHITE)
        label3 = font.render('Player ' + str(self.turn) + "'s turn", 1, WHITE)

        surface.blit(label1, (150, 30))
        surface.blit(label2, (player2_x + 130, 30))
        surface.blit(label3, (top_left_x + (BOARD_WIDTH / 2) - (label3.get_width() / 2), 30))

        self.player_reserves(surface, player_list)
        self.draw_grid(surface, 14, 14)
        pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, BOARD_WIDTH, BOARD_HEIGHT), 3)

        #self.draw_dragged_piece(surface)

        #for i in range(len(grid)):
        #    for j in range(len(grid[i])):
        #        pygame.draw.rect(surface, grid[i][j], (top_left_x + j*BLOCK_SIZE, top_left_y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)