from genericpath import exists
import pygame
import math
import random
from blokus.constants import *
from blokus.piece import *
from blokus.board import *

FPS = 60

# Pick Starting player randomly
starting_player = random.choice([1, 2])

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BLOKUS DUO")

# functions
def player_board_click(pos, player):
    player_click_grid = [[[] for x in range(7)] for x in range(3)]
    # counter for figuring out which shape is clicked
    n = 0
    
    if player == 1:
        for i in range(len(player_click_grid)):
            for j in range(len(player_click_grid[i])):
                temp_rect = pygame.Rect(i * (RESERVE_SIZE * 6), player_y + j * (RESERVE_SIZE * 6), RESERVE_SIZE * 6, RESERVE_SIZE * 6)
                if temp_rect.collidepoint(pos) and (player_str[n] in player1_reserves):
                    return (player_str[n], 1) # Returns piece name and player 1
                else:
                    n += 1
                
    if player == 2:
        for i in range(len(player_click_grid)):
            for j in range(len(player_click_grid[i])):
                temp_rect = pygame.Rect(player2_x + i * (RESERVE_SIZE * 6), player_y + j * (RESERVE_SIZE * 6), RESERVE_SIZE * 6, RESERVE_SIZE * 6)
                if temp_rect.collidepoint(pos) and (player_str[n] in player2_reserves):
                    return (player_str[n], 2) # Returns piece name and player 2
                else:
                    n += 1

def is_valid():
    pass

def locked_positions():
    pass

# Main loop

def main():
    board_positions = {} # (x,y): (255,0,0)
    grid = Board.game_grid(board_positions)

    run = True
    dragging = False
    clock = pygame.time.Clock()
    board = Board(screen, starting_player, None)

    while run:
        clock.tick(FPS)
        grid = Board.game_grid(board_positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if dragging == False:
                    if mouse_pos[0] >= 0 and mouse_pos[0] < top_left_x and board.turn == 1:
                        selected_piece = player_board_click(mouse_pos, 1)
                        dragging = True
                    if mouse_pos[0] >= (player2_x) and board.turn == 2:
                        selected_piece = player_board_click(mouse_pos, 2)
                        dragging = True
                    if dragging == True:
                        board.turn = selected_piece[1]
                        if board.turn == 1:
                            color = COLOR1
                        if board.turn == 2:
                            color = COLOR2
                        board.selected_piece = Piece(mouse_pos[0], mouse_pos[1], player1_reserves[str(selected_piece[0])], piece_corners[str(selected_piece[0])], color, BLOCK_SIZE)
            
            if dragging:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or pygame.K_DOWN:
                        if event.key == pygame.K_UP:
                            board.selected_piece = Piece.rot_shape(board.selected_piece, "cw")
                        elif event.key == pygame.K_DOWN:
                            board.selected_piece = Piece.rot_shape(board.selected_piece, "ccw")
                    if event.key == pygame.K_f:
                        board.selected_piece = Piece.flip_shape(board.selected_piece)
                    if event.key == pygame.K_RETURN:
                        dragging = False
        
        board.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()