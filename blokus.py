from genericpath import exists
import pygame
import math
from blokus.constants import *
from blokus.piece import *
from blokus.game import *
from blokus.board import *

FPS = 60

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BLOKUS DUO")

top_left_x = (SCREEN_WIDTH - BOARD_WIDTH) / 2
top_left_y = (SCREEN_HEIGHT - BOARD_HEIGHT) / 2
player1_x = (top_left_x - BOARD_WIDTH) / 2
player_y = 60
player2_x = SCREEN_WIDTH + player1_x

# functions
def get_row_col_from_mouse(pos):
    x, y = pos
    # Determine which board the mouse is in
    # Player 1's board
    if x >= 0 and x < top_left_x:
        row = y // RESERVE_SIZE
        col = x // RESERVE_SIZE
    # Main Board
    elif x >= top_left_x and x < top_left_x + SCREEN_WIDTH:
        row = y // BLOCK_SIZE
    # Player 2's Board
    else:
        row = y // RESERVE_SIZE

    return row, col

def is_valid():
    pass

def locked_positions():
    pass

def drag_drop(surface, grid, shape, offset_x, offset_y, dragging):
    deciding = True
    Start_flag = True

    # Allow the piece to be moved, flipped and rotated until position is locked
    while deciding:
        while dragging:
            if Start_flag == True:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                origin_x = mouse_x + offset_x
                origin_y = mouse_y + offset_y
                Start_flag = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dragging = False
                    deciding = False
                    pygame.display.quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        dragging = False
                
                if event.type == pygame.MOUSEMOTION:
                    if dragging:
                        mouse_x, mouse_y = event.pos
                        origin_x = mouse_x + offset_x
                        origin_y = mouse_y + offset_y
                        shape_origin = pygame.Rect(origin_x, origin_y, BLOCK_SIZE, BLOCK_SIZE)                 
            
            if dragging == True:
                Board.draw_window(surface, grid)

            #draw_shape(screen, origin_x, origin_y, shape, (255,0,0), BLOCK_SIZE)

            pygame.display.flip()

         #   clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                deciding = False
                pygame.display.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shape_origin.collidepoint(event.pos):
                        dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = shape_origin.x - mouse_x
                        offset_y = shape_origin.y - mouse_y
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    if event.key == pygame.K_UP:
                        shape = Piece.rot_shape(shape, "cw")
                    elif event.key == pygame.K_DOWN:
                        shape = Piece.rot_shape(shape, "ccw")
                if event.key == pygame.K_f:
                    shape = Piece.flip_shape(shape)
                if event.key == pygame.K_RETURN:
                    deciding = False

        if deciding == True:
            Board.draw_window(surface, grid)

        # surface, origin_x, origin_y, shape_matrix, color, block_size
        #draw_shape(screen, origin_x, origin_y, shape, (255,0,0), BLOCK_SIZE)

        pygame.display.update()

# Main loop

def main():
    board_positions = {} # (x,y): (255,0,0)
    grid = Board.game_grid(board_positions)

    run = True
    clock = pygame.time.Clock()
    game = Game(screen)
    board = Board()

    while run:
        clock.tick(FPS)
        #grid = Board.game_grid(board_positions)
        
        #if game.winnner() != None:
        #    print(game.winner())
        #    run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    if event.key == pygame.K_UP:
                        shape = Piece.rot_shape(shape, "cw")
                    elif event.key == pygame.K_DOWN:
                        shape = Piece.rot_shape(shape, "ccw")
                if event.key == pygame.K_f:
                    shape = Piece.flip_shape(shape)
                if event.key == pygame.K_RETURN:
                    pass
        
        board.player_grid(screen, player_list, player_list)
        game.update()
    
    pygame.quit()

main()