import pygame
import os

pygame.font.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption ('Space Invaders By: Avira')

ship_width = 70
ship_height = 70
boreder = pygame.Rect(450,0,30,600)
font = pygame.font.SysFont('Times New Roman', 50)
bullet_speed = 5
y_bullets = []
r_bullets = []
y_health = 10
r_health = 10
gameover = False

yellow_ship = pygame.transform.rotate (pygame.transform.scale (pygame.image.load('space_invaders/yellow_ship.png'), (ship_width, ship_height)), 90)
red_ship = pygame.transform.rotate (pygame.transform.scale (pygame.image.load('space_invaders/red_ship.png'), (ship_width, ship_height)), 270)
background = pygame.image.load('space_invaders/background.png')
yellow = pygame.Rect(20,300, ship_width, ship_height)
red = pygame.Rect(820,300, ship_width, ship_height)

def draw():
    global yellow,red

    screen.blit(background, (0,0))
    pygame.draw.rect(screen,'black', boreder)
    '''pygame.display.update()'''
    screen.blit(red_ship, (red.x,red.y))
    screen.blit(yellow_ship, (yellow.x, yellow.y))
    yellow_text = font.render('Health', True, 'white')
    red_text = font.render('Health', True, 'white')
    screen.blit(yellow_text, (20,20))
    screen.blit(red_text, (760,20))

    for i in y_bullets:
        pygame.draw.rect(screen, 'yellow', i)
    for j in r_bullets:
        pygame.draw.rect(screen, 'red', j)

def bullet_movement(y_bullets, r_bullets):
    global bullet_speed, y_health, r_health, yellow, red
    for i in y_bullets:
        i.x += bullet_speed
        if red.colliderect(i):
            y_bullets.remove(i)
            r_health -= 1
    for i in r_bullets:
        i.x -= bullet_speed
        if yellow.colliderect(i):
            r_bullets.remove(i)
            y_health -= 1


def yellow_mov(key_pressed):
    if key_pressed [pygame.K_a]:
        yellow.x -= 1
    if key_pressed [pygame.K_d]:
        yellow.x += 1
    if key_pressed [pygame.K_w]:
        yellow.y -= 1
    if key_pressed [pygame.K_s]:
        yellow.y += 1

def red_mov(key_pressed):
    if key_pressed [pygame.K_LEFT]:
        red.x -= 1
    if key_pressed [pygame.K_RIGHT]:
        red.x += 1
    if key_pressed [pygame.K_UP]:
        red.y -= 1
    if key_pressed [pygame.K_DOWN]:
        red.y += 1

def game_over():
    global y_health, r_health, gameover
    if y_health == 0:
        gameover = True
    elif r_health == 0:
        gameover = True

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LSHIFT:
                bullet = pygame.Rect(yellow.x + 35, yellow.y +35, 10,5)
                y_bullets.append(bullet)
            if i.key == pygame.K_RSHIFT:
                bullet = pygame.Rect(red.x + 35, red.y + 35, 10,5)
                r_bullets.append(bullet)
                
    draw()
    game_over()
    bullet_movement(y_bullets, r_bullets)
    key_pressed = pygame.key.get_pressed()
    yellow_mov(key_pressed)
    red_mov(key_pressed)
    
    pygame.display.update()