import pygame

pygame.init()
screen_résolution = (800, 600)
screen = pygame.display.set_mode(screen_résolution)
black = (0,0,0)
white = (255, 255, 255)
image_path = "desktop/projets/1a/Pendu/pendu/pendu_1.png"
hanged_image = pygame.image.load(image_path) # surface created
screen.fill(white)
hanged_image.convert()
image_rect = hanged_image.get_rect(topleft=(200, 50))


ubuntu_font = pygame.font.Font("desktop/Ubuntu-Regular.ttf", 36)
hangman = ubuntu_font.render("HANGMAN", True, black)

screen.blit(hangman,[300,10])
lauched = True
while lauched:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            lauched = False


    screen.blit(hanged_image, (200, 50))
    pygame.display.flip()