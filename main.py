import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, GREY
from checkers.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Checkers') #sets name displayed on the top of the app

def get_pos_from_mouse(pos): #pos: tuple with x and y position
    x,y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
  
 
    while run:
        clock.tick(FPS)
        
        if game.winner() != None:
            print(game.winner())
            run = False
                
        for event in pygame.event.get(): #events, setting button action etc...
            match event.type:
                case pygame.QUIT:   
                    run = False
                case pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_pos_from_mouse(pos)
                    game.select(row, col)
        game.update()

    pygame.QUIT
        


main()