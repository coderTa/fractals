import pygame
from pygame.locals import *

def clip(x, minimum, maximum):
    if x < minimum:
        return minimum
    elif x > maximum:
        return maximum 
    
    return x

pygame.init()
screen = pygame.display.set_mode((250, 250))
done = False
screen.fill((100, 100, 100))
while not done:  
    for x in range(-125, 125):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

        for y in range(-125, 125):
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
            screen.set_at((x + 125, y + 125), (color, color, color))
            #! END OF INTERPOLATION

            #    screen.set_at((x + 125, y + 125), (0, 0, 0))
    
        #print("column!")
        pygame.display.flip()

#alpha = speed / iterations
#color = (0 * (1 - alpha) + 255 * alpha)
#screen.set_at((x, y), (color, 100, color))