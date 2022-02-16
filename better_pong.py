import pygame,sys,random

def ball_animation():
    global ball_dx,ball_dy,ball_color,RNG

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Border Check
    if ball.top <= 0 or ball.bottom >= screen_y:
        ball_dy *= -1
    if ball.left <= 0 or ball.right >= screen_x:
        ball_reset()

    # Colliding with paddle
    if ball.colliderect(PlayerLeft):
        ball.x += 10
        ball_dx *= -1
        ball_color = "red"
        if RNG == 1:
            pass
        else:
            RNG = random.choice(range(1,6))
        
    if ball.colliderect(PlayerRight):
        ball.x -= 10
        ball_dx *= -1
        ball_color = "blue"
        if RNG == 1:
            pass
        else:
            RNG = random.choice(range(1,6))

    # Colliding with PowerUp
    if ball.colliderect(PowerUp):
        # Increase ball speed slightly, changes position
        if RNG == 1:
            if ball_color == "red":
                ball_dx += 2
            if ball_color == "blue":
                ball_dx -= 2
            RNG = random.choice(range(1,6))
            PowerUp.center = (random.choice((400,800)), random.choice((100,500)))

        # Reverse ball speed slightly or drastically depending on hitspot
        if RNG == 2:
            if ball_color == "red":
                ball_dx -= 2
            if ball_color == "blue":
                ball_dx += 2

def player_animation():
    PlayerLeft.y += PlayerLeft_speed
    PlayerRight.y += PlayerRight_speed

    # Border Check for Player
    if PlayerLeft.top <= 0:
        PlayerLeft.top = 0
    if PlayerLeft.bottom >= screen_y:
        PlayerLeft.bottom = screen_y
    if PlayerRight.top <= 0:
        PlayerRight.top = 0
    if PlayerRight.bottom >= screen_y:
        PlayerRight.bottom = screen_y

# def BOT_animation():
    # if opponent.top < ball.y:
    #     opponent.top += opponent_speed
    # if opponent.botttom > ball.y:
    #     opponent.bottom -= opponent_speed
    # if opponent.top <= 0:
    #     opponent.top = 0
    # if opponent.bottom >= screen_y:
    #     opponent.bottom = screen_y

def ball_reset():
    global ball_dx, ball_dy, ball_color
    ball_color = 'white'
    ball.center = (screen_x/2, screen_y/2)
    ball_dx = 7
    ball_dx *= random.choice((1,-1))
    ball_dy *= random.choice((1,-1))

def RNG_Power():
    if RNG == 1:
        PowerUp_Color = "yellow"
        pygame.Rect.update(PowerUp, PowerUp.x, PowerUp.y, 50, 100)
        pygame.draw.rect(screen, PowerUp_Color, PowerUp)
    if RNG == 2:
        PowerUp_Color = "red"
        pygame.Rect.update(PowerUp, PowerUp.x, PowerUp.y, 200, 20)
        pygame.draw.rect(screen, PowerUp_Color, PowerUp)



# General Setup
pygame.init()
clock = pygame.time.Clock()

# Setup Main Window
screen_x = 1200
screen_y = 650
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Better Pong by Far')

# Objects
ball = pygame.Rect(screen_x/2 - 15, screen_y/2 - 15, 30, 30)
PlayerLeft = pygame.Rect(20, screen_y/2 - 70, 10, 140)
PlayerRight = pygame.Rect(screen_x - 30, screen_y/2 - 70, 10, 140)
PowerUp = pygame.Rect(random.choice((400,800)), random.choice((100,500)), 50, 100)

# PowerUp_Color = "yellow"
ball_color = 'white'
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Speeds
ball_dx = 7 * random.choice((1,-1))
ball_dy = 7 * random.choice((1,-1))
PlayerLeft_speed = 0
PlayerRight_speed = 0
BOT_speed = 7
RNG = 0

# Main Loop
while True:
    # Taking Input for quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                PlayerLeft_speed += 7
            if event.key == pygame.K_w:
                PlayerLeft_speed -= 7
            if event.key == pygame.K_DOWN:
                PlayerRight_speed += 7
            if event.key == pygame.K_UP:
                PlayerRight_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                PlayerLeft_speed -= 7
            if event.key == pygame.K_w:
                PlayerLeft_speed += 7
            if event.key == pygame.K_DOWN:
                PlayerRight_speed -= 7
            if event.key == pygame.K_UP:
                PlayerRight_speed += 7
        
    ball_animation()
    player_animation()
    # BOT_animation()
    
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, "red", PlayerLeft)
    pygame.draw.rect(screen, "blue", PlayerRight)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, light_grey, (screen_x/2, 0),
                       (screen_x/2, screen_y))
    
    RNG_Power()

    # Update the window
    pygame.display.flip()
    clock.tick(60)
