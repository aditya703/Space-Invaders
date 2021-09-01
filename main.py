from utils import *

pygame.init()

screen = pygame.display.set_mode((600, 600))

# loading images to be used in the game
background = pygame.image.load("img/background.jpg")
logo = pygame.image.load("img/logo.jpg")
play = pygame.image.load("img/play.png")
icon = pygame.image.load("img/space-invaders1.png")
settings = pygame.image.load("img/settings.png")
pygame.display.set_caption('Space Invaders')
quit_game = pygame.image.load('img/exit.png')
pygame.display.set_icon(icon)

# image scaling
logo = pygame.transform.scale(logo, (600, 350))
play = pygame.transform.scale(play, (120, 120))
settings = pygame.transform.scale(settings, (90, 90))
quit_game = pygame.transform.scale(quit_game, (50, 50))

# used for centering certain objects
width = screen.get_width()
height = screen.get_height()

# making buttons
settings_button = Button(screen, (150, 450), settings)
play_button = Button(screen, (240, 360), play)
quit_game_button = Button(screen, (550, 0), quit_game)

running = True
page = Pages(background, screen)
wait = True
difficulty = 1

# main game loop
while running:

    mouse = pygame.mouse.get_pos()

    screen.blit(background, (0, 0))
    screen.blit(logo, (0, 0))

    play_button.display()
    settings_button.display()
    quit_game_button.display()

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            running = False

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if settings_button.click(mouse, (90, 90)):
                difficulty = page.settings_page(quit_game_button, difficulty)

            if quit_game_button.click(mouse, (50, 50)):
                running = False

            if play_button.click(mouse, (120, 120)):
                page.game_page(difficulty)

    pygame.display.update()
