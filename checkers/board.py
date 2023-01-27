import pygame
from .constants import BLACK, ROWS, WHITE, SQUARE_SIZE, COLOMNS, GREY
from .piece import *

number_of_pieces = 12
number_of_kings = 0
class Board:
    def __init__(self) -> None: #Time for some OOP !!
        self.board = []
        self.grey_left = self.white_left = 12
        self.grey_king = self.white_king = 0
        self.create_board()

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] #swap positions between the piece we want to move and the empty space it can move to
        piece.move(row, col)
        if row == ROWS-1 or row == 0:
            piece.transform_king()
            if piece.color == WHITE:
                self.white_king += 1
            else:
                self.grey_king+=1

    def get_piece(self, row, col):
        return self.board[row][col]


    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLOMNS, 2): #steps of 2 to put the color in each suares
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #dimensions of a cube

    def create_board(self):
        for row in range(ROWS):
            self.board.append([]) #list that contains whats inside each row, same thing for colomns
            for col in range(COLOMNS):
                if col % 2 == ((row+1) % 2): #put pieces only in black squares
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, GREY))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0) #0 to differentiate with pieces and blanks

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLOMNS):
                piece = self.board[row][col]
                if piece !=0:
                    piece.draw(win)
    

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col -1
        right = piece.col + 1
        row = piece.row
        if piece.color == GREY or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3,-1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3,-1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3,ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3,ROWS), 1, piece.color, right))

        return moves
           
    def _traverse_left(self, start, stop, step, color,left, skipped = []): #left diagonal
        moves = {}
        last = []
        for i in range(start,stop,step):
            if left < 0:
                break
            current = self.board[i][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i,left)] = last + skipped

                else:
                    moves[(i, left)] = last
                if last:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)
                    
                    moves.update(self._traverse_left(i+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(i+step, row, step, color, left+1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves


    def _traverse_right(self, start, stop, step, color,right, skipped = []): #right diagonal
        moves = {}
        last = []
        for i in range(start,stop,step):
            if right >= COLOMNS:
                break
            current = self.board[i][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i,right)] = last + skipped
                    
                else:
                    moves[(i, right)] = last
                if last:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)
                    
                    moves.update(self._traverse_left(i+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(i+step, row, step, color, right+1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == GREY:
                    self.grey_left -=1
                else:
                    self.white_left -=1
    
    def winner(self):
        if self.grey_left <= 0:
            return WHITE
        elif self.white_left <=0:
            return GREY
        return None