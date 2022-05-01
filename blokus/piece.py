from .constants import *
import pygame

# Shape Matrices

i1 = [[0,0]]
i1_corners = [[-1,-1], [1,-1], [1,1], [-1,1]]

i2 = [[0,0], [1,0]]
i2_corners = [[-1,-1], [-1,1], [2,1], [2,-1]]

i3 = [[0,0], [-1,0], [1,0]]
i3_corners = [[-2,-1], [-2,1], [2,-1], [2,1]]

i4 = [[0,0], [-1,0], [1,0], [2,0]]
i4_corners = [[-2,-1], [-2,1], [3,-1], [3,1]]

i5 = [[0,0], [-2,0], [-1,0], [1,0], [2,0]]
i5_corners = [[-3,-1], [-3,1], [3,-1], [3,1]]

v3 = [[0,0], [1,0], [0,1]]
v3_corners = [[-1,-1], [2,-1], [2,1], [-1,2], [1,2]]

v5 = [[0,0], [1,0], [2,0], [0,1], [0,2]]
v5_corners = [[-1,-1], [3,-1], [3,1], [-1,3], [1,3]]

z4 = [[0,0], [0,1], [-1,1], [1,0]]
z4_corners = [[-2,2], [-2,0], [-1,-1], [1,2], [2,-1], [2,1]]

z5 = [[0,0], [0,1], [-1,1], [0,-1], [1,-1]]
z5_corners = [[-2,2], [-2,0], [1,2], [-1,-2], [2,-2], [2,0]]

t4 = [[0,0], [-1,0], [0,-1], [1,0]]
t4_corners = [[-2,1], [-2,-1], [2,1], [2,-1], [-1,-2], [1,-2]]

t5 = [[0,0], [-1,0], [0,-1], [1,0], [0,-2]]
t5_corners = [[-2,1], [-2,-1], [2,1], [2,-1], [-1,-3], [1,-3]]

l4 = [[0,0], [-1,0], [1,0], [-1,-1]]
l4_corners = [[-2,1], [-2,-2], [0,-2], [2,1], [2,-1]]

l5 = [[0,0], [-1,0], [-2,0], [1,0], [-2,-1]]
l5_corners = [[-3,1], [-3,-2], [-1,-2], [2,1], [2,-1]]

s4 = [[0,0], [0,1], [1,1], [1,0]]
s4_corners = [[-1,-1], [-1,2], [2,-1], [2,2]]

f = [[0,0], [-1,0], [0,-1], [0,1], [1,1]]
f_corners = [[-1,2], [2,2], [2,0], [1,-2], [-1,-2], [-2,-1], [-2,1]]

p = [[0,0], [0,-1], [0,1], [1,0], [1,1]]
p_corners = [[-1,2], [-1,-2], [1,-2], [2,-1], [2,2]]

w = [[0,0], [0,-1], [1,-1], [-1,0], [-1,1]]
w_corners = [[-2,2], [0,2], [1,1], [2,0], [2,-2], [-1,-2], [-2,-1]]

x = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]
x_corners = [[1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2]]

u = [[0,0], [0,-1], [1,-1], [0,1], [1,1]]
u_corners = [[2,2], [2,0], [2,-2], [-1,-2], [-1,2]]

n = [[0,0], [0,-1], [1,-1], [-1,0], [-2,0]]
n_corners = [[1,1], [2,0], [2,-2], [-1,-2], [-3,-1], [-3,1]]

y = [[0,0], [-1,0], [0,-1], [1,0], [2,0]]
y_corners = [[3,-1], [3,1], [1,-2], [-1,-2], [-2,-1], [-2,1]]

player_str = ['i1', 'i2', 'i3' , 'i4', 'i5', 'v3', 'v5', 'z4', 'z5', 't4', 't5', 'l4', 'l5', 's4', 'f', 'p', 'w', 'x', 'u', 'n', 'y']
player_list = [i1, i2, i3 , i4, i5, v3, v5, z4, z5, t4, t5, l4, l5, s4, f, p, w, x, u, n, y]
piece_corners_list = [i1_corners, i2_corners, i3_corners, i4_corners, i5_corners, v3_corners, v5_corners, z4_corners, z5_corners, \
    t4_corners, t5_corners, l4_corners, l5_corners, s4_corners, f_corners, p_corners, w_corners, x_corners, u_corners, n_corners, y_corners]

piece_corners = dict(zip(player_str, piece_corners_list))
player1_reserves = dict(zip(player_str, player_list))
player2_reserves = player1_reserves

class Piece:
    def __init__(self, x, y, shape, corners, color, block):
            self.x = x
            self.y = y
            self.shape = shape
            self.corners = corners
            self.color = color
            self.block = block
    
    def draw_shape(self, surface):   
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
                # Rotated CW shape matrix for corners
                rot_shape_corners = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*rot_cw)] for X_row in self.corners]
            
            elif direction == 'ccw':
                # Rotation Matrix for 90deg CCW
                rot = [[0,1],[-1,0]]

                # Rotated CCW shape matrix
                rot_shape = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*rot)] for X_row in self.shape]
                # Rotated CCW shape matrix for corners
                rot_shape_corners = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*rot)] for X_row in self.corners]
        else:
            rot_shape = self.shape
            rot_shape_corners = self.corners

        return rot_shape, rot_shape_corners

    def flip_shape(self):
        # Takes shape matrix and flips it
        # Ex. of shape = [[0,0],[0,1],[-1,1],[1,0],[0,-1]]
        if len(self.shape) != 1:
            # y = x Matrix
            flip_matrix = [[0,1],[1,0]]

            # flipped shape matrix
            flip_shape = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*flip_matrix)] for X_row in self.shape]
            # flipped shape matrix for corners
            flip_shape_corners = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*flip_matrix)] for X_row in self.corners]
        else:  
            flip_shape = self.shape
            flip_shape_corners = self.corners

        return flip_shape, flip_shape_corners