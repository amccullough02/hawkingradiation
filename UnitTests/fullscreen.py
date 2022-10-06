
import pygame
from win32api import GetSystemMetrics

WIDTH = GetSystemMetrics(0)
HEIGTH = GetSystemMetrics(1)
MASTER = pygame.display.set_mode((WIDTH, HEIGTH))

def event_ESC_pressed(get_pressed):
    if get_pressed[pygame.K_ESCAPE]:
        print("You pressed ESC")
        exit() # or pygame.quit()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        get_pressed = pygame.key.get_pressed()
        event_ESC_pressed(get_pressed)

    pygame.quit()

if __name__ == "__main__":
    main()

