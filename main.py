import pygame
import random

pygame.init()
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/icon.png")
target_width = 220
target_height = 220
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
        screen.fill(color)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        screen.blit(target_img, (target_x, target_y))
        pygame.display.update()

pygame.quit()