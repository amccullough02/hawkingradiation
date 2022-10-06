import pygame


def debug_text(screen, text, colour=(255, 255, 255), font=None, size=50, pos=(20, 20)):
    font = pygame.font.SysFont(font, size)
    x = font.render(text, True, colour)
    screen.blit(x, pos)


def draw_text(screen, text, path, colour=(255, 255, 255), size=50, pos=(20, 20)):
    font = pygame.font.Font(path, size)
    x = font.render(text, True, colour)
    screen.blit(x, pos)
