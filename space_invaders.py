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
    screen.blit(red_text, (800,20))


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

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
    draw()
    key_pressed = pygame.key.get_pressed()
    yellow_mov(key_pressed)
    red_mov(key_pressed)
    
    pygame.display.update()