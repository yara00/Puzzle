import pygame
from tiles import *
from Controller import*
TILESIZE = 128
GAME_SIZE = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
MINTGREEN =	(170, 240, 200)
BGCOLOUR = DARKGREY




class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100,641))
        pygame.display.set_caption("Puzzle Game")
    def convert(self,num):
       b = str(num)
       c = []
       if num < 100000000:
        c.append(0)
       for digit in b:
          c.append (int(digit))

       return c 

    def create_game(self):
        grid = 12345678
        
        return grid    
    def solve (self,method):
        self.solving=True
        self.checkSol=False
        self.screen.blit(self.solvingText,(590,48))                     
        
        pygame.display.flip()

        ctrl = Controller()
        for method in self.boxes:
           if(method.checked == True):
             ans = ctrl.solve(method.caption,int(self.user_text))
             if ans == "Invalid Input" :
                self.new()
                self.solving=False
                self.checkInv=True

                self.user_text=''
             
             else:   
      
              self.steps = ans["path"]      
              if len(self.steps)==0:
                self.new()
                self.solving=False
                self.checkSol=True         
              else:
                 self.solving=False
                 self.checkSol=False 
                 self.checkInv=False
                 self.nodesExplored = str(ans["expanded"])
                 self.pathLength= str(len(self.steps))
                 self.maxDepth=str(ans["maxDepth"])
                 self.cost=str(ans["cost"])
                 self.time = str(ans["time"])+ " s"
                 self.tiles_grid = self.convert(self.steps[self.step])
                 self.bool = True
                 self.buttons_list1=[]
                 self.buttons_list1.append(Button(330, 450, 100, 50, "Step forward", MINTGREEN, BLACK,15))
                 self.buttons_list1.append(Button(50, 450, 100, 50, "Step back", MINTGREEN, BLACK,15))    
                          
                               
                 self.draw_tiles()
    def draw_tiles(self):
        row =0
        for col, x in enumerate(self.tiles_grid):
                
                if col %3 == 0 and col != 0:
                    row = row+1
                if x != 0:
                    Tile(self, (col%3)+0.39, row+0.39, str(x))
                else:
                    Tile(self, (col%3)+0.39, row+0.39, "empty")
    
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.convert(self.create_game())   
        self.buttons_list = []
        self.buttons_list1 = []
        self.buttons_list.append(Button(500, 130, 200, 50, "Solve", MINTGREEN, BLACK,30))
        self.buttons_list.append(Button(500, 200, 200, 50, "Reset", MINTGREEN, BLACK,30))
        self.step = 0
        self.boxes=[]
        self.steps=[]
        button = Checkbox(self.screen , 800, 100, 0, caption='BFS' ,font_color= WHITE , font_size=30)
        button2 = Checkbox(self.screen, 800, 150, 1, caption='DFS' ,font_color= WHITE, font_size=30)
        button3 = Checkbox(self.screen, 800, 200, 2, caption='A* Manhatten',font_color= WHITE, font_size=30)
        button4 = Checkbox(self.screen, 800, 250, 2, caption='A* Euclidean',font_color= WHITE, font_size=30)
        self.boxes.append(button)
        self.boxes.append(button2)
        self.boxes.append(button3)
        self.boxes.append(button4)
        self.solving= False 
        self.checkInv=False
        self.checkSol=False
        self.bool = False
        self.user_text=''
        self.nodesExplored =''
        self.pathLength=''
        self.maxDepth=''
        self.cost=''
        self.time=''
        self.base_font = pygame.font.SysFont("Consolas", 24)
        self.input_txt = pygame.Rect(500,80,140,32)
        font = pygame.font.SysFont("Consolas", 25)
        
        
        self.text = font.render('Input', True, MINTGREEN )
        self.noSolution=font.render('Has no solution', True, (220,20,60) )
        self.Invalid=font.render('Invalid input!', True, (220,20,60) )
        self.solvingText=font.render('Solving...', True, WHITE )
        self.text_nodesExplored = font.render('Explored nodes:', True, MINTGREEN )
        self.text_pathLength = font.render('Path Length: ', True, MINTGREEN ) 
        self.text_maxDepth = font.render('Max Depth: ', True, MINTGREEN )
        self.text_cost = font.render('Cost: ', True, MINTGREEN )
        self.text_time = font.render('Time: ', True, MINTGREEN )
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
            pygame.draw.line(self.screen,(100,100,100,100), (row+50, 50), (row+50, (GAME_SIZE * TILESIZE)+50))
        for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, (100,100,100,100), (50, col+50), ((GAME_SIZE * TILESIZE)+50, col+50)) 
   
    def draw(self):
        self.screen.fill((40,40,40,40))
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        for button in self.buttons_list:
            button.draw(self.screen)
        for button in self.buttons_list1:
            button.draw(self.screen)
        for box in self.boxes:
            box.render_checkbox()   
        pygame.draw.rect(self.screen,WHITE,self.input_txt,2)
        self.text_surface = self.base_font.render(self.user_text,True,(255,255,255))
        self.text_surface2 = self.base_font.render(self.nodesExplored,True,(255,255,255))
        self.text_surface3 = self.base_font.render(self.pathLength,True,(255,255,255))
        self.text_surface6 = self.base_font.render(self.maxDepth,True,(255,255,255)) 
        self.text_surface7 = self.base_font.render(self.cost,True,(255,255,255))
        self.text_surface8 = self.base_font.render(self.time,True,(255,255,255))
        self.text_surface4 = self.base_font.render(" / "+str(len(self.steps)),True,(255,255,255))
        self.text_surface5 = self.base_font.render(str(self.step+1),True,(255,255,255))

        self.screen.blit(self.text_surface,(self.input_txt.x+5,self.input_txt.y+5))
        
        self.screen.blit(self.text,(500,48))
        if self.bool:
           self.screen.blit(self.text_nodesExplored,(500,300))
           self.screen.blit(self.text_pathLength,(500,360))
           self.screen.blit(self.text_maxDepth,(500,420))
           self.screen.blit(self.text_cost,(500,480))
           self.screen.blit(self.text_time,(500,540))
           self.screen.blit(self.text_surface2,(714,303))
           self.screen.blit(self.text_surface3,(670,362))
           self.screen.blit(self.text_surface4,(215, 467))
           self.screen.blit(self.text_surface5,(185,467)) 
           self.screen.blit(self.text_surface6,(639,422)) 
           self.screen.blit(self.text_surface7,(570,482)) 
           self.screen.blit(self.text_surface8,(570,542))   
        if self.checkSol:
            self.screen.blit(self.noSolution,(500,300)) 
        if self.checkInv:
            self.screen.blit(self.Invalid,(500,25)) 
        if self.solving:
            self.screen.blit(self.solvingText,(590,48))                     
        self.input_txt.w = 200
        pygame.display.flip()
        

    

    def events(self):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type== pygame.MOUSEBUTTONDOWN:
              mouse_x, mouse_y = pygame.mouse.get_pos()
              for button in self.buttons_list1:
                if button.click(mouse_x, mouse_y):
                       if button.text == "Step forward":
                          
                          if self.step < len(self.steps)-1:
                             self.step+= 1
                             self.tiles_grid = self.convert(self.steps[self.step])
                             self.draw_tiles()
                       if button.text == "Step back":  
                            if self.step !=0: 
                              self.step-= 1  
                              self.tiles_grid = self.convert(self.steps[self.step])
                              self.draw_tiles()                        
              for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "Solve":
                           self.step=0
                           for method in self.boxes:
                             if(method.checked == True and self.user_text != ''): 
                                 
                               self.solve(method.caption)
                              
                        if button.text == "Reset":
                            self.new()
                        if button.text == "Step forward":
                          
                         if self.step < len(self.steps)-1:
                             self.step+= 1
                             self.tiles_grid = self.convert(self.steps[self.step])
                             self.draw_tiles()
                        if button.text == "Step back":  
                            if self.step !=0: 
                              self.step-= 1  
                              self.tiles_grid = self.convert(self.steps[self.step])
                              self.draw_tiles()    
              for box in self.boxes:
                    box.update_checkbox(event)
                    if box.checked is True:
                        for b in self.boxes:
                            if b != box:
                                b.checked = False
            if event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                   if (event.key == pygame.K_0 or event.key == pygame.K_1  or event.key ==pygame.K_2 or event.key ==pygame.K_3 or event.key ==pygame.K_4 or event.key ==pygame.K_5 or event.key ==pygame.K_6 or event.key ==pygame.K_7 or event.key ==pygame.K_8 or event.key == pygame.K_KP_0 or event.key == pygame.K_KP_1  or event.key ==pygame.K_KP_2 or event.key ==pygame.K_KP_3 or event.key ==pygame.K_KP_4 or event.key ==pygame.K_KP_5 or event.key ==pygame.K_KP_6 or event.key ==pygame.K_KP_7 or event.key ==pygame.K_KP_8 ) and len(self.user_text)<9 : 
                      self.user_text+= event.unicode                     
game  = Game()

while True:
    game.new()
    game.run()
    