# Program to multiply two matrices using list comprehension
import pygame

pygame.init()

BLOCK_SIZE = 50



i1 = [0,0]

i2 = [[0,0], [1,0]]

i3 = [[0,0], [1,0], [2,0]]

i4 = [[0,0], [1,0], [2,0], [3,0]]

i5 = [[0,0], [1,0], [2,0], [3,0], [4,0]]

v3 = [[0,0], [1,0], [0,1]]

v5 = [[0,0], [1,0], [2,0], [0,1], [0,2]]

z4 = [[0,0], [0,1], [-1,1], [1,0]]

z5 = [[0,0], [0,1], [-1,1], [0,-1], [1,-1]]

t4 = [[0,0], [-1,0], [0,-1], [1,0]]

t5 = [[0,0], [-1,0], [0,-1], [1,0], [0,-2]]

l4 = [[0,0], [-1,0], [1,0], [-1,-1]]

l5 = [[0,0], [-1,0], [-2,0], [1,0], [1,-1]]

s4 = [[0,0], [0,1], [1,1], [1,0]]

f = [[0,0], [-1,0], [0,-1], [0,1], [1,1]]

p = [[0,0], [0,-1], [0,1], [0,1], [1,1]]

w = [[0,0], [0,-1], [1,-1], [-1,0], [-1,1]]

x = [[0,0], [1,0], [-1,0], [0,1], [0,-1]]

u = [[0,0], [0,-1], [1,-1], [0,1], [1,1]]

n = [[0,0], [0,-1], [1,-1], [-1,0], [-2,0]]

y = [[0,0], [-1,0], [0,-1], [1,0], [2,0]]

shape = l5

list_player1 = [i1, i2, i3 , i4, i5, v3, v5, z4, z5, t4, t5, l4, l5, s4, f, p, w, x, u, n, y]

screen = pygame.display.set_mode((600, 800))

def rot_shape(shape_matrix):
# Rotation Matrix for 90deg CW
   rot_cw = [[0,-1],[1,0]]

   # Rotated CW shape matrix
   rot_shape = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*rot_cw)] for X_row in shape_matrix]

   print(rot_shape)

   return rot_shape

def flip_shape(shape_matrix):
    # Takes shape matrix and flips it
    # Ex. of shape_matrix = [[0,0],[0,1],[-1,1],[1,0],[0,-1]]

    # y = x Matrix
    flip_matrix = [[0,1],[1,0]]

    # flipped shape matrix
    flip_shape = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*flip_matrix)] for X_row in shape_matrix]

    return flip_shape

class Piece(object):
   def __init__(self, x, y, shape, color):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = color
            
   def collision_box(self, shape):
        # Determine collision box based on given shape
        collision_list_x = []
        collision_list_y = []
        
        for i in range(len(shape)):
            collision_list_x.append(shape[i][0])
            collision_list_y.append(shape[i][1])
        
        collision_top_left_x = self.x + (min(collision_list_x) * BLOCK_SIZE)
        collision_top_left_y = self.y - abs((min(collision_list_y) * BLOCK_SIZE))
        collision_box_width = max(collision_list_x) - min(collision_list_x) + 1
        collision_box_height = max(collision_list_y) - min(collision_list_y) + 1

        collision_box = (collision_top_left_x, collision_top_left_y, collision_box_width * BLOCK_SIZE, collision_box_height * BLOCK_SIZE)

        return collision_box

run = True

rectangle = Piece(300,300,shape,(255,0,0))

while run:
   

   screen.fill((0,0,0))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      elif event.type == pygame.MOUSEMOTION:
         origin_x, origin_y = event.pos
         rectangle = Piece(origin_x,origin_y,shape,(255,0,0))
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            shape = rot_shape(shape)
         elif event.key == pygame.K_f:
            shape = flip_shape(shape)
      else:
         origin_x, origin_y = pygame.mouse.get_pos()
         rectangle = Piece(origin_x,origin_y,shape,(255,0,0))

   for i in range(len(shape)):
      pygame.draw.rect(screen, (255,0,0), pygame.Rect(origin_x + shape[i][0] * 50, origin_y + shape[i][1] * 50, 50, 50))
      pygame.draw.rect(screen, (255,255,255), pygame.Rect(origin_x + shape[i][0] * 50, origin_y + shape[i][1] * 50, 50, 50),1)
      pygame.draw.rect(screen, (255,255,0), rectangle.collision_box(shape), 1)

   pygame.display.update()
