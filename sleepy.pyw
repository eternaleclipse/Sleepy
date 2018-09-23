import sys
import time
import datetime
import pygame
import os

def display_go_to_sleep():
    pygame.display.init()
    pygame.font.init()

    text = "Go to sleep you idiot! INS: Sleep ESC: Quit"
    font = pygame.font.SysFont('comicsansms', 20)
    text = font.render(text, True, (255, 255, 255))

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_INSERT:
                    os.system("psshutdown.exe -d -t 0")

        screen.blit(text, (100, 100))
        pygame.display.flip()
        clock.tick(60)
        
while True:
    if datetime.datetime.now().hour in range(7):
        display_go_to_sleep()
        
    time.sleep(10)