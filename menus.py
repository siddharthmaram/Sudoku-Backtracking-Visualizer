import pygame
import sys


def difficulty(screen, font):
    img = pygame.image.load("image.png")
    close = pygame.image.load("close.png")
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 <= mouse[0] <= 370 and 150 <= mouse[1] <= 200:
                    diff = 1
                    return diff
                elif 220 <= mouse[0] <= 370 and 250 <= mouse[1] <= 300:
                    diff = 2
                    return diff
                elif 220 <= mouse[0] <= 370 and 350 <= mouse[1] <= 400:
                    diff = 3
                    return diff
                elif 390 <= mouse[0] <= 410 and 100 <= mouse[1] <= 120:
                    return 0

        screen.fill((255, 255, 255))
        screen.blit(img, (0, 0))
        
        pygame.draw.rect(screen, (255, 165, 0), pygame.Rect(180, 100, 230, 350), border_radius=10)

        if 390 <= mouse[0] <= 410 and 100 <= mouse[1] <= 120:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(390, 100, 20, 20))
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(390, 100, 20, 20))

        screen.blit(close, (385, 95))

        if 220 <= mouse[0] <= 370 and 150 <= mouse[1] <= 200:
            pygame.draw.rect(screen, (104, 104, 104), pygame.Rect(220, 150, 150, 50), border_radius=5)
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(220, 150, 150, 50), border_radius=5)

        easy = font.render("Easy", True, (255, 255, 255))

        screen.blit(easy, (270, 160))

        if 220 <= mouse[0] <= 370 and 250 <= mouse[1] <= 300:
            pygame.draw.rect(screen, (104, 104, 104), pygame.Rect(220, 250, 150, 50), border_radius=5)
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(220, 250, 150, 50), border_radius=5)

        medium = font.render("Medium", True, (255, 255, 255))

        screen.blit(medium, (260, 260))

        if 220 <= mouse[0] <= 370 and 350 <= mouse[1] <= 400:
            pygame.draw.rect(screen, (104, 104, 104), pygame.Rect(220, 350, 150, 50), border_radius=5)
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(220, 350, 150, 50), border_radius=5)

        hard = font.render("Hard", True, (255, 255, 255))

        screen.blit(hard, (270, 360))

        pygame.display.update()
