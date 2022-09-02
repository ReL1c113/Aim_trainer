import pygame
import random
import math

pygame.init()
pygame.display.set_caption('MAIN MENU')

screen = pygame.display.set_mode((1500, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
play = pygame.image.load('play (1).png')

mouse_x = 0
mouse_y = 0


def aim_training1(text,x, y):
    trainer_1 = font.render(text, True, (255, 255, 255))
    screen.blit(trainer_1, (x, y))


def start(x, y):
    trainer_2 = font.render("WELCOME CHOOSE YOUR AIM TRAINER", True, (255, 255, 255))
    screen.blit(trainer_2, (x, y))


def isCollision(x, y, i, j):
    distance = math.sqrt(math.pow(x - i, 2) + math.pow(y - j, 2))
    if distance <= 200:
        return True
    else:
        return False


def play_(x, y):
    screen.blit(play, (x, y))


# MAIN GAME 1
def aim_train1():
    pygame.init()

    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption("AIM TRAINER 1")


    m_x = 0
    m_y = 0
    score = 0
    overall_score = 0

    font = pygame.font.Font('freesansbold.ttf', 32)

    # SPHERE
    number_spheres = 5
    sphereimg = []
    sphere_x = []
    sphere_y = []

    for i in range(number_spheres):
        sphereimg.append(pygame.image.load('sphere.png'))
        sphere_x.append(random.randint(100, 1400))
        sphere_y.append(random.randint(100, 700))

    def sphere(x, y, i):
        screen.blit(sphereimg[i], (x, y))

    def isCollision(x, y, i, j):
        distance = math.sqrt(math.pow(x - i, 2) + math.pow(y - j, 2))
        if distance <= 40:
            return True
        else:
            return False

    def show_score():
        shown_score = font.render("SCORE :" + str(score), True, (255, 255, 255))
        screen.blit(shown_score, (70, 50))

    def final_score():
        final_score = font.render("Final score " + str(overall_score), True, (255, 255, 255))
        screen.blit(final_score, (1245, 50))

    run = True
    while run:

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
        for i in range(number_spheres):
            collision = isCollision(sphere_x[i], sphere_y[i], m_x, m_y)
            if collision:
                sphere_x[i] = random.randint(100, 1400)
                sphere_y[i] = random.randint(100, 700)
                score = score + 1
            sphere(sphere_x[i], sphere_y[i], i)

        show_score()
        pygame.display.update()  # ##


# MAIN GAME 2
def aim_train2():
    pygame.init()

    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption('AIM TRAINER 2')

    m_x = 0
    m_y = 0
    score = 0
    overall_score = 0

    font = pygame.font.Font('freesansbold.ttf', 32)

    # SPHERE
    number_spheres = 5
    sphereimg = []
    sphere_x = []
    sphere_y = []
    change_x = []

    for i in range(number_spheres):
        sphereimg.append(pygame.image.load('sphere.png'))
        sphere_x.append(random.randint(100, 1400))
        sphere_y.append(random.randint(100, 700))
        change_x.append(0.5)

    def sphere(x, y, i):
        screen.blit(sphereimg[i], (x, y))

    def isCollision(x, y, i, j):
        distance = math.sqrt(math.pow(x - i, 2) + math.pow(y - j, 2))
        if distance <= 40:
            return True
        else:
            return False

    def show_score():
        shown_score = font.render("SCORE :" + str(score), True, (255, 255, 255))
        screen.blit(shown_score, (70, 50))

    def final_score():
        final_score = font.render("Final score " + str(overall_score), True, (255, 255, 255))
        screen.blit(final_score, (1245, 50))

    run = True
    while run:

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
        for i in range(number_spheres):
            sphere_x[i] = sphere_x[i] + change_x[i]
            # BOUNDARY CONDITIONS
            if sphere_x[i] == 1400:
                change_x[i] = -0.5
                sphere_x[i] = sphere_x[i] + change_x[i]
            if sphere_x[i] == 100:
                change_x[i] = 0.5
                sphere_x[i] = sphere_x[i] + change_x[i]
            collision = isCollision(sphere_x[i], sphere_y[i], m_x, m_y)
            if collision:
                sphere_x[i] = random.randint(100, 1400)
                sphere_y[i] = random.randint(100, 700)
                score = score + 1
                change_x[i] = 0.5
            sphere(sphere_x[i], sphere_y[i], i)

        show_score()
        pygame.display.update()


run = True
while run:

    screen.fill((25, 50, 75))
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.type==pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_1:
                aim_train1()
            if event.key == pygame.K_2:
                aim_train2()
            if event.key==pygame.K_ESCAPE:
                run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            collision1 = isCollision(mouse_x, 750, mouse_y, 350)
            collision2 = isCollision(mouse_x, 750, mouse_y, 650)
            if collision1:
                aim_train1()
            if collision2:
                aim_train2()

    aim_training1("TRAINER 1 -- PRESS 1 TO PLAY",550, 300)
    aim_training1("TRAINER 2 -- PRESS 2 TO PLAY",550, 600)
    play_(750, 350)
    play_(750, 650)
    start(500, 50)
    pygame.display.update()
