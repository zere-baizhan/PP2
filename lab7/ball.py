import pygame
import sys

pygame.init()

# Установка экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_image = pygame.image.load("ball.webp")
ball_rect = ball_image.get_rect()

ball_rect.center = (screen_width // 2, screen_height // 2)
ball_speed_x = 0
ball_speed_y = 0


running = True
while running:
    screen.fill(WHITE)

  
    screen.blit(ball_image, ball_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                ball_speed_x = 5
            elif event.key == pygame.K_UP:
                ball_speed_y = -5
            elif event.key == pygame.K_DOWN:
                ball_speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ball_speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ball_speed_y = 0


    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    
    if ball_rect.left < 0 or ball_rect.right > screen_width:
        ball_speed_x *= -1
    if ball_rect.top < 0 or ball_rect.bottom > screen_height:
        ball_speed_y *= -1

    pygame.display.flip()

 
    pygame.time.Clock().tick(60)


pygame.quit()
