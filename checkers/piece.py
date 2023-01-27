import pygame
from .constants import BLACK, WHITE, SQUARE_SIZE, GREY, CROWN
class Piece:

    PADDING = 12
   

    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == WHITE:
            self.direction = -1 #which way pieces are going
        if self.color == BLACK:
            self.direction = 1 
        self.x = 0
        self.y = 0
        self.calculate_position()

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()
        
    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2 #to put the pieces in the middle of the squares
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2

    def transform_king(self):
        self.king = True
  
    def draw(self, win):
        raduis = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), raduis)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2)) #put king in middle, cant draw at pos x y, because image position start from top right
    

    