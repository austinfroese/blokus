from xml.etree.ElementTree import TreeBuilder
import pygame
from .constants import *
from .board import Board

class Game:
    def __init__(self, win, player_turn):
        self._init()
        self.win = win
        self.player_turn = player_turn
    
    def update(self):
        self.board.draw_window(self.win, self.player_turn)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        #self.turn = Player1
    
    def winner(self):
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected = None
                self.select(row,col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            return True
        
        return False