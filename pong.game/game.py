import pygame
# 1
pygame.init()
pygame.display.set_caption("pong game")

# set up game window
SIZE = (600,600)
BG_COLOR = (8, 113, 142)
canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()
paddle_image = pygame.image.load("assets/paddle.png")
ball_image = pygame.image.load("assets/ball.png")

x1 = 0
y1 = 100
x2 = 570
y2 = 100
ball_x = 300
ball_y = 10
ball_v_x = 4
ball_v_y = 2
w_pressed = False
s_pressed = False
o_pressed = False
l_pressed = False
loop = True
while loop:
    # pooling
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
             loop = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_pressed = True
            if e.key == pygame.K_s:
                s_pressed = True
            if e.key == pygame.K_o:
                o_pressed = True
            if e.key == pygame.K_l:
                l_pressed = True
        elif e.type == pygame.KEYUP:
            w_pressed = False
            s_pressed = False
            o_pressed = False
            l_pressed = False
    if w_pressed:
        y1 -= 5
    if s_pressed:
        y1 += 5
    if o_pressed:
        y2 -= 5
    if l_pressed:
        y2 += 5
    ball_x += ball_v_x
    ball_y += ball_v_y
    if ball_x >= 580 or ball_x <=0 :
        ball_v_x = -ball_v_x
    if ball_y == 580 and ball_x >= 0 and ball_x <= 600:
        ball_v_y = - ball_v_y
    if ball_y == 0 and ball_x >= 0 and ball_x <= 600:
        ball_v_y = - ball_v_y
    if ball_x <= 30 and ball_y >= y1 and ball_y <= y1+120:
        ball_v_x = -ball_v_x
    if ball_x >= 550 and ball_y >= y2 and ball_y <= y2+120:
        ball_v_x = -ball_v_x

    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image,(x1, y1))

    canvas.blit(paddle_image,(x2, y2))
    canvas.blit(ball_image,(ball_x, ball_y))


    clock.tick(60)
    pygame.display.flip()