import pygame
import time
pygame.init()

base = pygame.image.load("C:/Users/modik/Documents/pp2/7lab/mickeyclock.png")
h1 = pygame.image.load("C:/Users/modik/Documents/pp2/7lab/hand-1.png")
h2 = pygame.image.load("C:/Users/modik/Documents/pp2/7lab/hand-2.png")

window = pygame.display.set_mode((1000, 750))

pygame.display.set_caption("MickeyClock")

check = True
while check:
    c_time = time.localtime()

    minutes = c_time.tm_min
    seconds = c_time.tm_sec

    minutes_angle = (minutes / 60) * 360
    seconds_angle = (seconds / 60) * 360

    h1_rotated = pygame.transform.rotate(h1, -minutes_angle)
    h2_rotated = pygame.transform.rotate(h2, -seconds_angle)

    window.blit(base, (0, 0))

    h1_x = 1000 / 2 - h1_rotated.get_width() / 2
    h1_y = 750 / 2 - h1_rotated.get_height() / 2
    window.blit(h1_rotated, (h1_x, h1_y))

    h2_x = 1000 / 2 - h2_rotated.get_width() / 2
    h2_y = 750 / 2 - h2_rotated.get_height() / 2
    window.blit(h2_rotated, (h2_x, h2_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
            pygame.quit()

    pygame.time.wait(1000)