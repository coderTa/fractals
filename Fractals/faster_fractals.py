import pygame
import numpy as np
from pygame.locals import *
import matplotlib.pyplot as plt

res = 250

def clip(x, minimum, maximum):
    if x < minimum:
        return minimum
    elif x > maximum:
        return maximum 
    
    return x

grid = np.zeros((res * 2, res * 2)).astype(complex)

for x in range (-res, res):
    for y in range (-res, res):
        grid[y + res][x + res] = 1j * y/3000. + (x + 350 * 15)/3000.

print(grid)

iterations = 100
z = np.zeros((res * 2, res * 2))
counter = np.zeros((res * 2, res * 2))

for i in range(iterations):
    #z = ((z ** 2 + grid - 1) / (2 * z + grid - 2 + 0.0001)) ** 2
    #z = np.sin(z) ** 2 + grid
    #z = np.tan(z) ** 2 + grid
    #z = z - (z - 1) ** 3 / (3 * z ** 2) + grid
    z = (np.abs(z.real) + np.abs(z.imag) * 1j) ** 2 - grid

    counter += np.abs(z) < 100

#final = abs(z) > 0.1
plt.imshow(counter, cmap = plt.get_cmap("gist_ncar"))
plt.show()

    
"""
pygame.init()
screen = pygame.display.set_mode((res * 2, res * 2))
done = False
screen.fill((100, 100, 100))
while not done:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
    
    for i in range(len(z)):
        for j in range(len(z[0])):
            if abs(z[i][j]) + 10  > 0 or z[i][j] == np.inf:
                screen.set_at((i, j), (255, 255, 255))
            else:
                screen.set_at((i, j), (0, 0, 0))

    pygame.display.flip()
    input("")

    for y in range(-res, res):
        c = (x + 60) / 50 + 1j * y / 50
        z = 0
        iterations = 100
        speed = iterations

        for i in range(iterations):
            z = ((z ** 2 + c - 1) / (2 * z + c - 2 + 0.0001)) ** 2

            if abs(z) > 100:
                speed = i * 1
                break

        if y % 10 == 0:
            print(speed)
        #if abs(z) > 100:

        #! INTERPOLATION
        color = clip(int(255 - speed ** 5/iterations ** 2 * 255), 0, 255)
        screen.set_at((x + res, y + res), (color, color, color))
        #! END OF INTERPOLATION

        #    screen.set_at((x + res, y + res), (0, 0, 0))

    #print("column!")
    pygame.display.flip()
"""

#alpha = speed / iterations
#color = (0 * (1 - alpha) + 255 * alpha)
#screen.set_at((x, y), (color, 100, color))