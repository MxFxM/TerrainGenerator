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
            col = int((bn.noise2(x/100, y/100) + 1) * 126)
            pygame.draw.circle(gameDisplay, (col, col, col), (x, y), 0)

    pygame.display.update()  # draw to screen
    clock.tick(60)  # limit at 60 fps

pygame.quit()
quit()
