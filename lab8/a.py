import pygame , sys , random
from pygame.math import Vector2

class snake:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False

        self.head_up=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/head_up.png').convert_alpha()
        self.head_down=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/head_down.png').convert_alpha()
        self.head_right=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/head_right.png').convert_alpha()
        self.head_left=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/head_left.png').convert_alpha()


        self.tail_up=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/tail_down.png').convert_alpha()
        self.tail_down=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/tail_up.png').convert_alpha()
        self.tail_right=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/taik_left.png').convert_alpha()
        self.tail_left=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/tail-right.png').convert_alpha()

        self.body_vertical=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/vertical_body.png').convert_alpha()
        self.body_horizontal=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/horizontal_body.png').convert_alpha()

        self.body_tr=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/body_tr.png').convert_alpha()
        self.body_tl=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/body_tl.png').convert_alpha()
        self.body_br=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/body_br.png').convert_alpha()
        self.body_bl=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            #1.We still need a rect for the posiotions
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            #2. what direction is the faceheading
            if index == 0:
                screen.blit(self.head,block_rect)
                #3. snake head direction is not updating
            elif index == len(self.body)-1:
                screen.blit(self.tail,block_rect)
            else:
                preious_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                if preious_block.x==next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif preious_block.y==next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if preious_block.x==-1 and next_block.y==-1 or preious_block.y==-1 and next_block.x==-1:
                        screen.blit(self.body_bl,block_rect)
                    elif preious_block.x==-1 and next_block.y==1 or preious_block.y==1 and next_block.x==-1:
                        screen.blit(self.body_tr,block_rect)
                    elif preious_block.x==1 and next_block.y==-1 or preious_block.y==-1 and next_block.x==1:
                        screen.blit(self.body_br,block_rect)
                    elif preious_block.x==1 and next_block.y==1 or preious_block.y==1 and next_block.x==1:
                        screen.blit(self.body_tl,block_rect)

    def update_head_graphics(self):
        head_relation=self.body[1] - self.body[0]
        if head_relation== Vector2(1,0): self.head = self.head_left
        elif head_relation== Vector2(-1,0): self.head = self.head_right
        elif head_relation== Vector2(0,1): self.head = self.head_up
        elif head_relation== Vector2(0,-1): self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation=self.body[-2]-self.body[-1]
        if tail_relation==Vector2(1,0):self.tail=self.tail_left
        elif tail_relation==Vector2(-1,0):self.tail=self.tail_right
        elif tail_relation==Vector2(0,1):self.tail=self.tail_up
        elif tail_relation==Vector2(0,-1):self.tail=self.tail_down


    def move_snake(self):
        if self.new_block==True:
            body_copy=self.body[:]
            body_copy.insert(0,self.body[0]+ self.direction)
            self.body=body_copy
            self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,self.body[0]+ self.direction)
            self.body=body_copy

    def add_block(self):
        self.new_block=True 

class fruit:
    def __init__(self):
        #create an x and y position 
        #draw a square 
        self.randomize()

    def draw_fruit(self):
        #create a rectanglr and draw ut
        fruit_rec=pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rec)
        # pygame.draw.rect(screen,(126,166,114),fruit_rec)

    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)

class main:
    def __init__(self):
        self.snake=snake()
        self.fruit=fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
            #reposition the fruit and another block to the snake
            self.fruit.randomize()
            self.snake.add_block()
    
    def check_fail(self):
        # check if snail is outside of the screen and check if snake hits itself 
        if not 0 <= self.snake.body[0].x<cell_number or not 0 <= self.snake.body[0].y<cell_number :
            self.game_over()

        for block in self.snake.body[1:]:
            if block== self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()  
        sys.exit()
    
    def draw_score(self):
        score_text=str(len(self.snake.body)-3)
        score_surface=game_font.render(score_text,True,(56,74,12))
        score_x=int(cell_size*cell_number-60)
        score_y=int(cell_size*cell_number-40)
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        screen.blit(score_surface,score_rect)




pygame.init()
cell_size=40
cell_number=20
screen=pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock=pygame.time.Clock()
apple=pygame.image.load('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/apple.png').convert_alpha()
game_font=pygame.font.Font('/Users/ayananauryzbaeva/Desktop/pp2/labky/lab8/PoetsenOne-Regular.ttf',25)


main_game=main()
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    #draw all our elemets 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  #oppposite of pygame init
            sys.exit() #to make sure thatour code stopped 
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if main_game.snake.direction.y!=1:
                    main_game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_RIGHT:
                if main_game.snake.direction.x!=1:
                    main_game.snake.direction=Vector2(1,0)
            if event.key==pygame.K_DOWN:
                if main_game.snake.direction.y!=-1:
                    main_game.snake.direction=Vector2(0,1)
            if event.key==pygame.K_LEFT:
                if main_game.snake.direction.x != 1 :
                    main_game.snake.direction=Vector2(-1,0)


    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
