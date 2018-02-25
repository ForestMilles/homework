import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green
pygame.draw.line(gameDisplay, blue, (100,200), (300,500),5)
pygame.draw.rect(gameDisplay, red, (400,200,50,25))
pygame.draw.circle(gameDisplay, white, (400,400), 100, 50 )
pygame.draw.polygon(gameDisplay, green, ((55,75),(36,124),(260,375),(450,25),(6,540)))

print("")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()