from genericpath import exists
import pygame
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
                    return player_str[n] # Returns piece name
                else:
                    n += 1
                
    if player == 2:
        for i in range(len(player_click_grid)):
            for j in range(len(player_click_grid[i])):
                temp_rect = pygame.Rect(player2_x + i * (RESERVE_SIZE * 6), player_y + j * (RESERVE_SIZE * 6), RESERVE_SIZE * 6, RESERVE_SIZE * 6)
                if temp_rect.collidepoint(pos) and (player_str[n] in player2_reserves):
                    return player_str[n] # Returns piece name
                else:
                    n += 1

def drop_piece(pos, grid):
    board_click_grid = [[[] for x in range(14)] for x in range(14)]
    # counter for figuring out which spot is clicked
    n = 0

    for i in range(len(board_click_grid)):
        for j in range(len(board_click_grid[i])):
            temp_rect = pygame.Rect(top_left_x + i * BLOCK_SIZE, top_left_y + j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if temp_rect.collidepoint(pos) and is_valid(i, j, grid):
                return (i,j) # True if piece can go there
            else:
                n += 1
    
    return None

def is_valid(i, j, grid):
    # 1. Starting pos   
    if len(player1_reserves) == 21 or len(player2_reserves) == 21:
        if (i == 4 and j == 4 and grid[i][j] == BLACK) or (i == 9 and j == 9 and grid[i][j] == BLACK):
            return True
    # 2. Corners  
    # 3. Overlap     
    # 4. Off the board
    return False

def locked_positions():
    pass

# Main loop

def main():
    board_positions = {} # (x,y): (255,0,0)
    grid = Board.game_grid(board_positions)

    run = True
    dragging = False
    dropped = False
    clock = pygame.time.Clock()
    board = Board(screen, starting_player, None, dragging)

    while run:
        clock.tick(FPS)
        grid = Board.game_grid(board_positions)

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if dragging == True:
                    dropped_pos = drop_piece(mouse_pos, grid)
                    if dropped_pos is not None:
                        dropped = True
                        board.selected_piece.x = top_left_x + (dropped_pos[0] * BLOCK_SIZE)
                        board.selected_piece.y = top_left_y + (dropped_pos[1] * BLOCK_SIZE)

                if dragging == False:
                    if mouse_pos[0] >= 0 and mouse_pos[0] < top_left_x and board.turn == 1:
                        selected_piece = player_board_click(mouse_pos, 1)
                        dragging = True
                    if mouse_pos[0] >= (player2_x) and board.turn == 2:
                        selected_piece = player_board_click(mouse_pos, 2)
                        dragging = True
                    if dragging == True:
                        if board.turn == 1:
                            color = COLOR1
                        if board.turn == 2:
                            color = COLOR2
                        board.selected_piece = Piece(mouse_pos[0], mouse_pos[1], player1_reserves[str(selected_piece)], piece_corners[str(selected_piece)], color, BLOCK_SIZE)
                        board.dragging = True
            
            if dragging:
                if dropped == False:
                    board.selected_piece.x = mouse_pos[0] - BLOCK_SIZE // 2 
                    board.selected_piece.y = mouse_pos[1] - BLOCK_SIZE // 2

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or pygame.K_DOWN:
                        if event.key == pygame.K_UP:
                            board.selected_piece.rot_shape("cw")
                        elif event.key == pygame.K_DOWN:
                            board.selected_piece.rot_shape("ccw")
                    if event.key == pygame.K_f:
                        board.selected_piece.flip_shape()
                    if event.key == pygame.K_RETURN and dropped:
                        dragging = False
                        dropped = False
                        board.dragging = False

        
        board.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()