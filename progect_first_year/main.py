import pygame
pygame.init()
back= (43, 18, 52)
mw = pygame.display.set_mode(500,500)
#mw.fill(back)
background_image = pygame.image.load("pixil-frame-0.png")
#mw.blit(background_image, (0, 0))
clock=pygame.time.Clock()

#sound= pygame.mixer.Sound("")
dx = 3
dy=3 

racket_x=200
racket_y=410
 
racket2_x=200
racket2_y=50

move_right= False
move_left=False

move_right2= False
move_left2=False

game_over = False

#platform_x =200
#platform_y=300


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        #запамятовуємо прямокутник
        self.rect= pygame.Rect(x,y,width,height)
        #колур заливки- або переданий параметр, або загальний колір тла
        self.fill_color=back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color
    
    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint (x,y)

    def colliderect(self,rect):
        return self.rect.colliderect(rect) 

class Label(Area):
    def set_text (self, text, fsize=12, text_color=(0,0,0)):
        self.image= pygame.font.SysFont("verdana", fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image,(self.rect.x +shift_x, self.rect.y + shift_y))
#класс для обьектів картинок
class Picture (Area):
    def __init__(self,filename,x=0,y=0,width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height, color=None )
        self.image=pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))
# хочу чай
ball =Picture("pixil-frame-0 (3).png", 215, 210, 100,100)

platform =Picture("platform2.0.png", racket_x, racket_y, 110,40) # нижняя платформа

platform_2 =Picture("platform22.0.png", racket2_x, racket2_y, 110, 40) #верхняя платформа( в 1  режиме бот)

goal_v = Picture("pixil-frame-0 (5).png", 0, 0) # верхние ворота
#я машина *крутой смайлик в очках*
goal_n = Picture("pixil-frame-0 (6).png", 0, 500 ) # нижние ворота


print("для начала игры выберите режим и нажмите на игровое поле")
print("здравствуйте вас приветствует игра ****")
print("одиночный режим против бота: нажмите 1")
print("режим с другом: нажмите 2")
game_mode = int(input(" "))
# какаша какая то получается

while not game_over:
    mw.blit(background_image, (0, 0))
    if game_mode == 1:
        platform_2.rect.x -= 3


    else:
        if game_mode == 2:

            for event in pygame.event.get():
# как же глупо выглядят эти коменты
              if event.type == pygame.QUIT:
                  game_over = True
              if event.type==pygame.KEYDOWN:
                  if event.key == pygame.K_RIGHT:#
                      move_right=True#піднімаємо флаг
                  if event.key == pygame.K_LEFT:
                      move_left=True#піднімаємо флаг

#                    if event.key == pygame.K_A:
                  if event.key == pygame.K_a:
                      move_left == True
# о мама мия
                  if event.key == pygame.K_d:
                      move_right == True
              elif event.type==pygame.KEYUP:
                  if event.key==pygame.K_RIGHT:
                      move_right=False#опускаємо флаг
                  if event.key==pygame.K_LEFT:
                        move_left=False#опускаємо флаг
                  if event.key == pygame.K_a:
                      move_left == False
                  if event.key== pygame.K_d:
                      move_right == False

#желание писать матные коменты все выше
            if move_right:#флаг руху вправо    #
                platform.rect.x += 3           ##
            if move_left: #флаг руху вліво     ##  нижняя платформа
                platform.rect.x -= 3           #

            if move_right2:              
                platform_2.rect.x += 3
            if move_left2:
                platform_2.rect.x -= 3



#тяжело

    goal_v.draw()
    goal_n.draw()
    platform.draw()
    platform_2.draw()
    ball.draw()

#проходит вторая неделя как я пытаюсь сделать этот проект

    pygame.display.update()
    clock.tick(40)