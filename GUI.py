import State

import pygame
from tiles import *
TILESIZE = 128
GAME_SIZE = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
BGCOLOUR = DARKGREY




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100,641))
        pygame.display.set_caption("Puzzle Game")
    
    def create_game(self):
        grid = [[0,1,2],[3,4,5],[6,7,8]]
        
        return grid    
    
    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile != 0:
                    self.tiles[row].append(Tile(self, col, row, str(tile)))
                else:
                    self.tiles[row].append(Tile(self, col, row, "empty"))
    
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()   
        self.buttons_list = []
        self.buttons_list.append(Button(500, 100, 200, 50, "Solve", WHITE, BLACK))
        self.buttons_list.append(Button(500, 170, 200, 50, "Reset", WHITE, BLACK))
        self.draw_tiles()
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for row in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen,(100,100,100,100), (row, 0), (row, GAME_SIZE * TILESIZE))
        for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, (100,100,100,100), (0, col), (GAME_SIZE * TILESIZE, col)) 
   
    def draw(self):
        self.screen.fill((40,40,40,40))
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        for button in self.buttons_list:
            button.draw(self.screen)
        
        pygame.display.flip()
        

    

    def events(self):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type== pygame.MOUSEBUTTONDOWN:
              mouse_x, mouse_y = pygame.mouse.get_pos()
              for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "Solve":
                           # print("solve")
                            self.shuffle_time = 0
                            self.start_shuffle = True
                        if button.text == "Reset":
                            self.new()

game  = Game()
while True:
    game.new()
    game.run()