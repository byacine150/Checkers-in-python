import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLOMNS = 8, 8
SQUARE_SIZE = WIDTH//COLOMNS

GREY = (128,128,128)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
TEMP_CROWN = pygame.image.load("./assets/crown.png")
CROWN = pygame.transform.scale(TEMP_CROWN, (70,40)) #resizing image
