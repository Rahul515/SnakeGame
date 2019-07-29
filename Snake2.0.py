import pygame, time, random

pygame.init()

display_width = 800
display_height = 600

gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.update()

clock = pygame.time.Clock()

snake_size = 20
apple_image = pygame.image.load('apple.png')
snake_image = pygame.image.load("Snake.png")
snake_image = picture = pygame.transform.scale(snake_image, (300, 150))

font1 = pygame.font.SysFont("cooper black", 45)
font2 = pygame.font.SysFont("Comic Sans MS", 25)
font3 = pygame.font.SysFont("cooper black", 60)
font4 = pygame.font.SysFont("Copperplate Gothic Bold", 100)
font5 = pygame.font.SysFont("Calibri (Body)", 45)

def snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(gamedisplay, (0,150,0), [i[0], i[1], snake_size, snake_size])

def score(score):
    text = font2.render("Score: "+str(score), True, (255,255,255))
    gamedisplay.blit(text, [1,1])

def pause():
    pause = True
    while pause == True:
        gamedisplay.fill((0,0,0))
        text_1 = font4.render("Paused", True, (255,130,0))
        text_2 = font2.render("Press SPACE to resume or ESC to quit", True, (255,255,255))
        gamedisplay.blit(text_1, [(display_width/2) - (text_1.get_rect().width/2), 250])
        gamedisplay.blit(text_2, [(display_width/2) - (text_2.get_rect().width/2), 500])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def start_page():
    global name
    intro = True
    while intro == True:
        gamedisplay.fill((0,0,0))
        text1 = font4.render("Snkae Game", True, (255,100,0))
        text2 = font2.render("press ENTER to start the game or ESC to quit", True, (255,255,255))
        text3 = font5.render("Enter your name: ", True, (190,100,40))
        gamedisplay.blit(text1, [(display_width/2) - (text1.get_rect().width/2), 30])
        gamedisplay.blit(snake_image, [(display_width/2) - (snake_image.get_rect().width/2), 100])
        gamedisplay.blit(text2, [(display_width/2) - (text2.get_rect().width/2), 490])
        gamedisplay.blit(text3, [(display_width/2) - (text3.get_rect().width/2) - 100, 330])
        pygame.display.update()
        name_loop = True
        name = ""
        while name_loop == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        name_loop = False
                        intro = False
                        gameloop()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    else:
                        name += chr(event.key-32)
                        text4 = font5.render(name, True, (190,100,40))
                        gamedisplay.blit(text4, [(display_width/2) + (text3.get_rect().width/2) - 100, 330])
                        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()            

def gameloop():
    exit_game = False
    gameover = False
    
    x = 400
    y = 300
    x_change = 0
    y_change = -10
    apple_size = 40
    snake_list = []
    snake_length = 3
    c_score = 0
    fps = 10

    apple_x = round(random.randrange(0, display_width - apple_size)/20.0)*20.0
    apple_y = round(random.randrange(0, display_height - apple_size)/20.0)*20.0
    
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_size
                elif event.key == pygame.K_SPACE:
                    pause()
                
        x += x_change
        y += y_change

        if x < 0 or x + snake_size > display_width or y < 0 or y + snake_size > display_height:
            gameover = True

        gamedisplay.fill((0,0,0))

        gamedisplay.blit(apple_image, [apple_x, apple_y])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        for i in snake_list[:-1]:
            if i == snake_head:
                gameover = True

        if len(snake_list) > snake_length:
            del snake_list[0]
            
        snake(snake_list)
        score(c_score)
        pygame.display.update()

        if x >= apple_x and x + snake_size <= apple_x + apple_size:
            if y >= apple_y and y + snake_size <= apple_y + apple_size:
                apple_x = round(random.randrange(0, display_width - apple_size)/20.0)*20.0
                apple_y = round(random.randrange(0, display_height - apple_size)/20.0)*20.0
                snake_length += 1
                c_score = snake_length - 3        
                if int(c_score) % 10 == 0:
                    fps += 5

        clock.tick(fps)

        f = open('HighScore.txt', 'r')
        a = f.readlines()
        high_scorer1 = a[0][:-1]
        high_score1 = int(a[1][:-1])
        high_scorer2 = a[2][:-1]
        high_score2 = int(a[3][:-1])
        high_scorer3 = a[4][:-1]
        high_score3 = int(a[5])
        f.close()
        
        if snake_length-3 >= high_score1:
            high__score3 = high_score2
            high__scorer3 = high_scorer2
            high__score2 = high_score1
            high__scorer2 = high_scorer1
            high__score1 = snake_length-3
            high__scorer1 = name
        elif snake_length-3 >= high_score2:
            high__score3 = high_score2
            high__scorer3 = high_scorer2
            high__score2 = snake_length-3
            high__scorer2 = name
            high__score1 = high_score1
            high__scorer1 = high_scorer1
        elif snake_length-3 >= high_score3:
            high__score3 = snake_length-3
            high__scorer3 = name
            high__score2 = high_score2
            high__scorer2 = high_scorer2
            high__score1 = high_score1
            high__scorer1 = high_scorer1
        else:
            high__score1 = high_score1
            high__scorer1 = high_scorer1
            high__score2 = high_score2
            high__scorer2 = high_scorer2
            high__score3 = high_score3
            high__scorer3 = high_scorer3
        
        while gameover == True:
            gamedisplay.fill((0,0,0))
            text1 = font3.render("GAME OVER! ", True, (255,0,0))
            text2 = font4.render("Your score was: "+str(snake_length-3), True, (0,175,230))
            text3 = font1.render("Highscores:", True, (0,160,0))
            text4 = font5.render(high__scorer1+": "+str(high__score1), True, (255,130,0))
            text5 = font5.render(high__scorer2+": "+str(high__score2), True, (255,130,0))
            text6 = font5.render(high__scorer3+": "+str(high__score3), True, (255,130,0))
            text7 = font2.render("Press Space to play again, ENTER to change name or Esc to quit ", True, (255,255,255))
            gamedisplay.blit(text1, [(display_width/2) - (text1.get_rect().width/2), 80])
            gamedisplay.blit(text2, [(display_width/2) - (text2.get_rect().width/2), 170])
            gamedisplay.blit(text3, [(display_width/2) - (text3.get_rect().width/2),280])
            gamedisplay.blit(text4, [(display_width/2) - (text4.get_rect().width/2),380])
            gamedisplay.blit(text5, [(display_width/2) - (text5.get_rect().width/2),430])
            gamedisplay.blit(text6, [(display_width/2) - (text6.get_rect().width/2),480])
            gamedisplay.blit(text7, [(display_width/2) - (text7.get_rect().width/2),540])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                        gameover = False
                    elif event.key == pygame.K_SPACE:
                        gameloop()
                    elif event.key == 13:
                        gameover = False
                        start_page()

            f = open("HighScore.txt", 'w')
            f.write(high__scorer1+'\n')
            f.write(str(high__score1)+'\n')
            f.write(high__scorer2+'\n')
            f.write(str(high__score2)+'\n')
            f.write(high__scorer3+'\n')
            f.write(str(high__score3))

    pygame.quit()
    quit()

start_page()
        
