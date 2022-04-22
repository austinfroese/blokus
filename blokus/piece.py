from .constants import *
import pygame

# Shape Matrices

i1 = [[0,0]]

i2 = [[0,0], [1,0]]

i3 = [[0,0], [-1,0], [1,0]]

i4 = [[0,0], [-1,0], [1,0], [2,0]]

i5 = [[0,0], [-2,0], [-1,0], [1,0], [2,0]]

v3 = [[0,0], [1,0], [0,1]]

v5 = [[0,0], [1,0], [2,0], [0,1], [0,2]]

z4 = [[0,0], [0,1], [-1,1], [1,0]]

z5 = [[0,0], [0,1], [-1,1], [0,-1], [1,-1]]

t4 = [[0,0], [-1,0], [0,-1], [1,0]]

t5 = [[0,0], [-1,0], [0,-1], [1,0], [0,-2]]

l4 = [[0,0], [-1,0], [1,0], [-1,-1]]

l5 = [[0,0], [-1,0], [-2,0], [1,0], [-1,-1]]

s4 = [[0,0], [0,1], [1,1], [1,0]]

f = [[0,0], [-1,0], [0,-1], [0,1], [1,1]]

p = [[0,0], [0,-1], [0,1], [0,1], [1,1]]

w = [[0,0], [0,-1], [1,-1], [-1,0], [-1,1]]

x = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]

u = [[0,0], [0,-1], [1,-1], [0,1], [1,1]]

n = [[0,0], [0,-1], [1,-1], [-1,0], [-2,0]]

y = [[0,0], [-1,0], [0,-1], [1,0], [2,0]]

player_str = ['i1', 'i2', 'i3' , 'i4', 'i5', 'v3', 'v5', 'z4', 'z5', 't4', 't5', 'l4', 'l5', 's4', 'f', 'p', 'w', 'x', 'u', 'n', 'y']
player_list = [i1, i2, i3 , i4, i5, v3, v5, z4, z5, t4, t5, l4, l5, s4, f, p, w, x, u, n, y]

player1_reserves = dict(zip(player_str, player_list))
player2_reserves = player1_reserves

class Piece:
    def __init__(self, x, y, shape, color, block):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = color
            self.block = block
    
    def draw_shape(self, surface):   
        if len(self.shape) == 1:
            pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.block, self.block))
            pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.x, self.y, self.block, self.block),1) 
        else:
            for i in range(len(self.shape)):
                pygame.draw.rect(surface, self.color, pygame.Rect(self.x + self.shape[i][0] * self.block, self.y + self.shape[i][1] * self.block, self.block, self.block))
                pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.x + self.shape[i][0] * self.block, self.y + self.shape[i][1] * self.block, self.block, self.block),1)


    def rot_shape(self, direction):
        # Takes shape matrix and direction str(cw/ccw) of rotation and outputs rotated shape
        # Ex. of shape = [[0,0],[0,1],[-1,1],[1,0],[0,-1]]
        if len(self.shape) != 1:
            if direction == 'cw':
                # Rotation Matrix for 90deg CW
                rot_cw = [[0,-1],[1,0]]

                # Rotated CW shape matrix
                rot_shape = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*rot_cw)] for X_row in self.shape]
            
            elif direction == 'ccw':
                # Rotation Matrix for 90deg CCW
                rot = [[0,1],[-1,0]]

                # Rotated CCW shape matrix
                rot_shape = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*rot)] for X_row in self.shape]
        else:
            rot_shape = self.shape

        return rot_shape

    def flip_shape(self):
        # Takes shape matrix and flips it
        # Ex. of shape = [[0,0],[0,1],[-1,1],[1,0],[0,-1]]
        if len(self.shape) != 1:
            # y = x Matrix
            flip_matrix = [[0,1],[1,0]]

            # flipped shape matrix
            flip_shape = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*flip_matrix)] for X_row in self.shape]
        else:  
            flip_shape = self.shape

        return flip_shape
    
    def collision_box(self):
        # Get mouse pos
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Determine collision box based on given shape
        collision_list_x = []
        collision_list_y = []
        
        for i in range(len(self.shape)):
            collision_list_x.append(self.shape[i][0])
            collision_list_y.append(self.shape[i][1])
        
        collision_top_left_x = self.x + (min(collision_list_x) * BLOCK_SIZE)
        collision_top_left_y = self.y - abs((min(collision_list_y) * BLOCK_SIZE))
        collision_box_width = max(collision_list_x) - min(collision_list_x) + 1
        collision_box_height = max(collision_list_y) - min(collision_list_y) + 1

        # Outputs collision box with format = (top_left_x, top_left_y, width, height)
        collision_box = pygame.Rect(collision_top_left_x, collision_top_left_y, collision_box_width * BLOCK_SIZE, collision_box_height * BLOCK_SIZE)

        # Check to see if box was clicked or not
        if collision_box.collidepoint(mouse_x, mouse_y):
            return True
        else:
            return False