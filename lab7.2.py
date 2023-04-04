import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Ball")

x = 400
y = 300
m = 20
def draw_ball():
    pygame.draw.circle(screen, 'red', (x, y), 25)

check = True
while check:
    screen.fill('white')
    draw_ball()
    pygame.display.flip()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
        elif action.type == pygame.KEYDOWN:
            if action.key == pygame.K_UP and y - m >= 25:
                y -= m
            elif action.key == pygame.K_DOWN and y + m <= 600 - 25:
                y += m
            elif action.key == pygame.K_LEFT and x - m >= 25:
                x -= m
            elif action.key == pygame.K_RIGHT and x + m <= 800 - 25:
                x += m