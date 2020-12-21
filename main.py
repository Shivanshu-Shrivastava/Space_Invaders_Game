import pygame
import random
import math
from pygame import mixer

pygame.init()
# screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("space satyam")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

mixer.music.load("cima.mp3")
mixer.music.play(-1)

running = True
# player
playerImg = pygame.image.load('spaceship (2).png')
playerX = 400
playerY = 459
playerchane = 0

# game
over = pygame.font.Font("freesansbold.ttf", 62)


def gameover():
    overte = over.render("GAME OVER", True, (255, 0, 0))
    screen.blit(overte, (400, 300))


# enemy
enemyimh = []
enemyX = []
enemyY = []
enemyXchan = []
enemyYchan = []
for i in range(6):
    # if enemyY[i] > 450:
    #   gameover()
    #  break
    enemyimh.append(pygame.image.load('monster (1).png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(55, 155))
    enemyXchan.append(0.5)
    enemyYchan.append(30)

# bullet
bulletImh = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 459
bulletYchan = 1
bulletXchan = 0.4
bulletstate = "ready"

#bulletX1=random.randint()


# collison
def iscollison(x1, y1, x2, y2):
    distsnce = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distsnce < 30:
        return True


def fire(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletImh, (x, y))

    # score


scorevalue = 0
font = pygame.font.Font("freesansbold.ttf", 32)


# scoreX=10
# scoreY=10


def ss():
    score = font.render('SCORE: ' + str(scorevalue), True, (255, 0, 0))
    screen.blit(score, (10, 10))


def enemy():
    for j in range(6):
        screen.blit(enemyimh[j], (enemyX[j], enemyY[j]))


def player(x, y):
    screen.blit(playerImg, (x, y))


# game loop
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerchane = -0.3
            if event.key == pygame.K_RIGHT:
                playerchane = 0.3
            if event.key == pygame.K_UP:
                if bulletstate == "ready":
                    laser = mixer.Sound("la.wav")
                    laser.play()
                    bulletX = playerX
                    fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerchane = 0

    playerX += playerchane
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    for i in range(6):

        enemyX[i] += enemyXchan[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyXchan[i] = 0.3
            enemyY[i] += enemyYchan[i]
        if enemyX[i] >= 736:
            enemyX[i] = 736
            enemyXchan[i] = -0.3
            enemyY[i] += enemyYchan[i]
        if enemyY[i] > 200:
            enemyY[i] = 2000
            gameover()
            break
        colison = iscollison(enemyX[i], enemyY[i], bulletX, bulletY)
        if colison:
            explo = mixer.Sound("exp.wav")
            explo.play()
            bulletY = 459
            bulletstate = "ready"
            scorevalue += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(55, 155)

    player(playerX, playerY)
    enemy()
    if bulletstate is "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletYchan
    if bulletY <= 0:
        bulletY = 459
        bulletstate = "ready"

    ss()

    pygame.display.update()
