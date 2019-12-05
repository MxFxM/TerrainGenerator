"""
Requires:
Source for noise: https://github.com/caseman/noise/blob/master/perlin.py
From: https://github.com/caseman/noise
"""

import pygame

import max_color as mc
import noise

bn = noise.SimplexNoise()

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TerrainGenerator')


def col_from_height(h):
    if h < 10:
        return (0, 8, 61)
    if h < 30:
        return (0, 14, 107)
    if h < 50:
        return (0, 29, 219)
    if h < 70:
        return (206, 209, 0)
    if h < 100:
        return (160, 209, 0)
    if h < 120:
        return (87, 209, 0)
    if h < 150:
        return (0, 209, 21)
    if h < 170:
        return (153, 191, 2)
    if h < 200:
        return (232, 206, 74)
    if h < 220:
        return (115, 115, 115)
    if h < 250:
        return (163, 163, 163)
    return (255, 255, 255)


col = [[0 for _ in range(display_height)] for _ in range(display_width)]
for x in range(display_width):
    for y in range(display_height):
        col[x][y] = col_from_height(int((bn.noise2(x/500, y/500) + 1) * 126))

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():  # event handling
        if event.type == pygame.QUIT:  # exit on closing
            done = True
        elif event.type == pygame.KEYDOWN and event.key == 13:  # exit on enter
            done = True
        """
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePressed(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            mouseMoved(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouseReleased(event.pos)
        """

    # background
    pygame.draw.rect(gameDisplay, mc.color('black'), [
                     0, 0, display_width, display_height])

    for x in range(display_width):
        for y in range(display_height):
            pygame.draw.circle(gameDisplay, col[x][y], (x, y), 0)

    pygame.display.update()  # draw to screen
    clock.tick(60)  # limit at 60 fps

pygame.quit()
quit()
