import random
import pygame
from pygame import mixer
import asyncio

async def main():
    pygame.init()
    clock = pygame.time.Clock()


    screen = pygame.display.set_mode((900,600))
    mixer.music.load('assets/sounds/LaHssab.ogg')
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    pygame.display.set_caption('Duck Hunt')

    duckbg1 = pygame.image.load('assets/images/duckbg1.jpeg')
    duckbg2 = pygame.image.load('assets/images/duckbg2.png')


    #duck
    duck1=pygame.image.load('assets/images/duckf-1.png')
    duck2=pygame.image.load('assets/images/duckf-2.png')
    duck3=pygame.image.load('assets/images/duckf-3.png')
    duck4=pygame.image.load('assets/images/duckf-4.png')
    duck5=pygame.image.load('assets/images/duckf-5.png')
    duck6=pygame.image.load('assets/images/duckf-6.png')
    duck7=pygame.image.load('assets/images/duckf-7.png')
    duck8=pygame.image.load('assets/images/duckf-8.png')
    duck9=pygame.image.load('assets/images/duckf-9.png')
    duck10=pygame.image.load('assets/images/duckf-10.png')
    duck11=pygame.image.load('assets/images/duckf-11.png')
    duck12=pygame.image.load('assets/images/duckf-12.png')
    duck13=pygame.image.load('assets/images/duckf-13.png')
    duck14=pygame.image.load('assets/images/duckf-14.png')
    duck15=pygame.image.load('assets/images/duckf-15.png')

    duckX = -100
    duckY = 200

    #duck_variable
    flyD_count = 0
    duck_die = False
    duckY_up = False
    duck_speed = 5
    duckY_down = True
    randYup =0
    randYdown = 0


    def duckXY(x,y,flyD_count):
        if flyD_count >= 1 and flyD_count <= 50:
            screen.blit(duck1,(x,y))
        if flyD_count >= 51 and flyD_count <= 100 :
            screen.blit(duck2,(x,y))
        if flyD_count >= 101 and flyD_count <= 150 :
            screen.blit(duck3,(x,y))
        if flyD_count >= 151 and flyD_count <= 200 :
            screen.blit(duck4,(x,y))
        if flyD_count >= 201 and flyD_count <= 250 :
            screen.blit(duck5,(x,y))
        if flyD_count >= 251 and flyD_count <= 300 :
            screen.blit(duck6,(x,y))
        if flyD_count >= 301 and flyD_count <= 350 :
            screen.blit(duck7,(x,y))
        if flyD_count >= 351 and flyD_count <= 400 :
            screen.blit(duck8,(x,y))
        if flyD_count >= 401 and flyD_count <= 450 :
            screen.blit(duck9,(x,y))
        if flyD_count >= 451 and flyD_count <= 500 :
            screen.blit(duck10,(x,y))
        if flyD_count >= 501 and flyD_count <= 550 :
            screen.blit(duck11,(x,y))
        if flyD_count >= 551 and flyD_count <= 600 :
            screen.blit(duck12,(x,y))
        if flyD_count >= 601 and flyD_count <= 650 :
            screen.blit(duck13,(x,y))
        if flyD_count >= 651 and flyD_count <= 700 :
            screen.blit(duck14,(x,y))
        if flyD_count >= 701 and flyD_count <= 750 :
            screen.blit(duck15,(x,y))


    #duckDie
    duckD=pygame.image.load('assets/images/duckDie.png')
    def duckDieXY(x,y):
        screen.blit(duckD,(x,y))


    #target
    aim = pygame.image.load('assets/images/aim.png')
    aimX = 300
    aimY = 200
    def aimXY(x,y):
        screen.blit(aim,(x,y))
    #aim_xy_variable
    aimX_change = 0
    aimY_change = 0
    aim_shoot = False

    #fox with duck
    fox = pygame.image.load('assets/images/foxwithduck.png') #change
    foxX= duckX+20
    foxY = 480
    def foxXY(x,y):
        screen.blit(fox,(x,y))

    #fox_variable
    fox_hide = False
    foxH_count = 0
    fox_speed = 2

    #foxAngry
    foxAngry = pygame.image.load('assets/images/angryfox.png') #change
    foxAngryX = 350
    foxAngryY = 500
    def foxAngryXY(x,y):
        screen.blit(foxAngry,(x,y))
    #foxAngry_variable
    foxA_vissi = False
    foxA_hide = False
    foxAV_count = 0


    #score
    sfont = pygame.font.SysFont('freesansbold.ttf',40)
    score_value = 0
    def scoreXY(x,y):
        score= sfont.render('SCORE:'+str(score_value),True,(0,0,0))
        screen.blit(score,(x,y))

    #gameOver
    passing_duck = 0
    gameOver = False

    gfont = pygame.font.SysFont('freesansbold.ttf',128)
    def gameXY(x,y):
        gameO = gfont.render('GAME OVER',True,(0,0,0))
        screen.blit(gameO,(x,y))

    #duckIcon
    duckIcon = pygame.image.load('assets/images/duck_icon.png')
    def duckIconXY(x,y):
        screen.blit(duckIcon,(x,y))

    #bullet_counting
    bullet_count = 0
    bullet = pygame.image.load('assets/images/bullet.png')
    def bulletXY(x,y):
        screen.blit(bullet,(x,y))

    # ---------------- UI Buttons ----------------
    button_fire = pygame.Rect(60, 480, 120, 100)
    button_start= pygame.Rect(650, 500, 200, 80)
    mouse_pad = pygame.Rect(500, 430, 400, 170)  # x,y,w,h
    mouse_pad1 = pygame.Rect(500, 480, 400, 120)  # x,y,w,h
    font_btn = pygame.font.SysFont('freesansbold.ttf', 32)
    font_start= pygame.font.SysFont('freesansbold.ttf', 32)

    def draw_buttons():
        pygame.draw.rect(screen, (255, 0, 0), button_fire, border_radius= 30)
        text = font_btn.render("Shoot", True, (0, 0, 0))
        screen.blit(text, (button_fire.x + 30, button_fire.y + 40))

    def draw_start_button():
        pygame.draw.rect(screen, (250, 100, 10), button_start, border_radius=15)
        text = font_start.render("START", True, (0, 0, 0))
        screen.blit(text, (button_start.x + 50, button_start.y + 30))
    def mouse_pad_xy():
        pygame.draw.rect(screen, (100, 100, 100), mouse_pad1, border_radius=10)  # grey pad
        text = font_start.render("Drag to shoot", True, (0, 0, 0))
        screen.blit(text, (mouse_pad1.x + 100, mouse_pad1.y + 40))

    game_start = False
    game_cover = pygame.image.load('assets/images/cover.png')
    gun_sound = mixer.Sound('assets/sounds/gunSht.ogg')
    def game_start_cover(x,y):
        msg1 = font_btn.render("Multi-touch not supported!", True, (255, 255, 0))
        msg2 = font_btn.render("Lift finger before tapping shoot.", True, (255, 255, 0))
        screen.blit(game_cover,(x,y))
        screen.blit(msg1,(550,445))
        screen.blit(msg2, (550, 470))

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(duckbg1,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: #game control by mouse
                if event.button == 1 and button_fire.collidepoint(event.pos) and duck_die == False and gameOver == False and bullet_count<=2 and game_start == True:
                    gun_sound.play()
                    aim_shoot = True
                    bullet_count += 1  # number of bullet using
                if event.button == 3 and duck_die == False and gameOver == False and bullet_count<=2 and game_start == True :
                    gun_sound.play()
                    aim_shoot = True
                    bullet_count += 1  # number of bullet using
                if button_start.collidepoint(event.pos):
                    game_start = True
            if event.type == pygame.MOUSEBUTTONUP :
                aim_shoot = False
            if event.type == pygame.MOUSEMOTION and game_start: # for touch pad to move aim
                if mouse_pad.collidepoint(event.pos):
                    dx, dy = event.rel
                    aimX += dx
                    aimY += dy
                    if aimX < 0: aimX = 0
                    if aimX > 900 - aim.get_width(): aimX = 900 - aim.get_width()
                    if aimY < 0: aimY = 0
                    if aimY > 500 - aim.get_height(): aimY = 500 - aim.get_height()
        if game_start == False:
            game_start_cover(0,0)
            draw_start_button()
        else:

            #duck_hunting
            if duckX-10 <= aimX <= duckX+58 and duckY-10 <= aimY <= duckY+40 and aim_shoot == True:
                duck_die = True
                duckSound = mixer.Sound('assets/sounds/duckS.ogg')
                duckSound.play()
                duckSound.set_volume(0.5)


            if gameOver == False: #when game is over game loop will stop

                #duck_all
                if duck_die == False:
                    duckX+=duck_speed
                    if duckX>=1050 and foxA_vissi == False:  #when the duck pass
                        passing_duck+=1
                        bullet_count = 0 #renew bullet
                        foxA_vissi = True
                    if foxA_vissi == True and foxA_hide == False:  #showing angry fox
                        foxAngryY-= fox_speed
                        if foxAngryY <= 360:
                            foxAngryY = 360
                            foxA_hide = True
                    if foxA_hide == True:         #hide angry fox
                        foxAV_count+=1
                        if foxAV_count >=200: #change
                            foxAngryY+=1
                            if foxAngryY>=500 :
                                foxAngryY = 500
                                foxA_vissi = False
                                foxA_hide = False
                                foxAV_count = 0
                                duckX = -100    #coming new duck

                    foxAngryXY(foxAngryX,foxAngryY)


                    if duckY_down == True and duckY_up == False: #y change
                        duckY+=1.5*duck_speed #change
                        if duckY>=420-randYdown:
                            duckY = 420 -randYdown
                            randYdown = random.randrange(0,250,50)
                            duckY_up = True
                            duckY_down = False
                    if duckY_down == False and duckY_up == True:  #y change
                        duckY-=1.5*duck_speed #change
                        if duckY<=5+randYup:
                            duckY = 5+randYup
                            randYup = random.randrange(0,200,50)
                            duckY_up = False
                            duckY_down = True
                if passing_duck >= 3 :
                    gameOver = True

                if duck_die == True:
                    duckX = duckX
                    foxX = duckX + 20 #fox x-axis place
                    duckY+=3  #change
                    if duckY >=500:
                        duckY = 500

                flyD_count+=5 #change
                if flyD_count >=750:
                    flyD_count = 0
                if duck_die == False:
                    duckXY(duckX,duckY,flyD_count)
                if duck_die == True:
                    duckDieXY(duckX,duckY)

            #game loop

            #fox
            if duck_die == True and duckY>=500 and fox_hide == False :
                foxY-=fox_speed #change
                if foxY <= 360 :
                    foxY = 360
                    score_value += 10
                    fox_hide = True
            if fox_hide == True:
                foxH_count+=1
                if foxH_count>=200: #change
                    foxY+=fox_speed #change
                    if foxY >= 500:  #when fox hide , new duck coming
                        foxY = 500
                        duck_die = False
                        bullet_count = 0 #renew bullet
                        duckX =-100
                        duckY = 50+ random.randrange(0,320,5)
                        flyD_count = 0
                        fox_hide = False
                        foxH_count = 0

            foxXY(foxX,foxY)


            #target
            aimX+=aimX_change
            if aimX<=1:
                aimX =1
            if aimX>=836:
                aimX =836
            aimY += aimY_change
            if aimY <=1:
                aimY =1
            if aimY >= 366:
                aimY = 366
            aimXY(aimX,aimY)

            #grass
            screen.blit(duckbg2,(0,430))
            mouse_pad_xy()
            draw_buttons()
            if gameOver == False:
                scoreXY(5,5)
            #game_over
            if gameOver == True :
                gameXY(180,100)
                scoreXY(300, 205)

            #duck_passing
            if passing_duck==0:
                duckIconXY(800,5)
                duckIconXY(832, 5)
                duckIconXY(864, 5)
            if passing_duck==1:
                duckIconXY(800,5)
                duckIconXY(832, 5)
            if passing_duck==2:
                duckIconXY(800,5)

            #bullet_icon
            if bullet_count == 0 :
                bulletXY(10,50)
                bulletXY(25, 50)
                bulletXY(40, 50)
            if bullet_count == 1 :
                bulletXY(10,50)
                bulletXY(25, 50)
            if bullet_count == 2 :
                bulletXY(10,50)

        clock.tick(60)
        pygame.display.flip()
        await asyncio.sleep(0)

# This is the program entry point
asyncio.run(main())
