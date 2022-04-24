from genericpath import exists
import pygame
import math
import random
from blokus.constants import *
from blokus.piece import *
from blokus.game import *
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
                if temp_rect.collidepoint(pos):
                    return (player_str[n], 1) # Returns piece name and player 1
                else:
                    n += 1
                
    if player == 2:
        for i in range(len(player_click_grid)):
            for j in range(len(player_click_grid[i])):
                temp_rect = pygame.Rect(player2_x + i * (RESERVE_SIZE * 6), player_y + j * (RESERVE_SIZE * 6), RESERVE_SIZE * 6, RESERVE_SIZE * 6)
                if temp_rect.collidepoint(pos):
                    return (player_str[n], 2) # Returns piece name and player 2
                else:
                    n += 1

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
    dragging = False
    clock = pygame.time.Clock()
    game = Game(screen, starting_player)
    board = Board()

    while run:
        clock.tick(FPS)
        grid = Board.game_grid(board_positions)
        
        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if dragging == False:
                    if mouse_pos[0] >= 0 and mouse_pos[0] < top_left_x:
                        selected_piece = player_board_click(mouse_pos, 1)
                    if mouse_pos[0] >= (player2_x):
                        selected_piece = player_board_click(mouse_pos, 2)
            
            if dragging:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or pygame.K_DOWN:
                        if event.key == pygame.K_UP:
                            shape = Piece.rot_shape(shape, "cw")
                        elif event.key == pygame.K_DOWN:
                            shape = Piece.rot_shape(shape, "ccw")
                    if event.key == pygame.K_f:
                        shape = Piece.flip_shape(shape)
                    if event.key == pygame.K_RETURN:
                        dragging = False
        
        game.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()