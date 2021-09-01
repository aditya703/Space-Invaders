import pygame
import random


class Bullet:

    def __init__(self, screen, img, pos):
        self.screen = screen
        self.img = img
        self.posX, self.posY = pos

    def render(self):
        self.screen.blit(self.img, (self.posX, self.posY))

    def shoot(self, up, speed):
        if up:
            for x in range(10):
                self.posY -= speed
                self.render()
        else:
            for x in range(10):
                self.posY += speed
                self.render()

    def delete(self, list, up):
        if up:
            if self.posY < 0:
                list.pop(0)
        else:
            if self.posY > 550:
                list.pop(0)

    def destroy(self, list, x):
        list.pop(x)

    def hit(self, pos, size):
        sizeX, sizeY = size
        posX, posY = pos

        if posX <= self.posX <= posX + sizeX and posY <= self.posY <= posY + sizeY:
            return True
        else:
            return False


class Sprite:

    def __init__(self, screen, img, pos):
        self.screen = screen
        self.img = img
        self.posX, self.posY = pos

    def render(self):
        self.screen.blit(self.img, (self.posX, self.posY))

    def move(self, mouse):
        self.posX = mouse[0] - 65
        if self.posX > 500:
            self.posX = 500
        elif self.posX < 0:
            self.posX = 0
        return self.posX

    def shooting(self, img, pos, list):
        bullet = Bullet(self.screen, img, pos)
        list.append(bullet)

    def destroy(self, list, x):
        list.pop(x)

    def alien_movement(self):
        self.posY += 0.04

    def change_img(self, new_img):
        self.img = new_img


class Button:

    def __init__(self, screen, pos, img):
        self.screen = screen
        self.posX, self.posY = pos
        self.img = img

    def display(self):
        self.screen.blit(self.img, (self.posX, self.posY))

    def hide(self):
        self.img.set_alpha(0)

    def show(self):
        self.img.set_alpha(255)

    def click(self, mouse_pos, size):
        self.mouseX, self.mouseY = mouse_pos
        self.sizeX, self.sizeY = size

        if self.posX <= self.mouseX <= self.posX + self.sizeX and self.posY <= self.mouseY <= self.posY + self.sizeY:
            return True


class Pages:
    def __init__(self, background, screen):
        self.screen = screen
        self.background = background
        self.sound = pygame.mixer.Sound('spaceinvaders1.wav')
        self.sound.play()

    def settings_page(self, quit_game_button, diff):
        on = pygame.image.load("img/on.png")
        off = pygame.image.load("img/off.png")
        easy = pygame.image.load("img/easy.png")
        medium = pygame.image.load("img/medium.png")
        hard = pygame.image.load("img/hard.png")
        on = pygame.transform.scale(on, (100, 50))
        off = pygame.transform.scale(off, (100, 50))
        easy = pygame.transform.scale(easy, (100, 50))
        medium = pygame.transform.scale(medium, (100, 50))
        hard = pygame.transform.scale(hard, (100, 50))
        on_button = Button(self.screen, (350, 170), on)
        off_button = Button(self.screen, (350, 170), off)
        off_button.hide()

        easy_button = Button(self.screen, (355, 250), easy)
        medium_button = Button(self.screen, (355, 250), medium)
        hard_button = Button(self.screen, (355, 250), hard)
        medium_button.hide()
        hard_button.hide()

        font1 = pygame.font.Font('MachineStd-Bold.otf', 40)
        font2 = pygame.font.Font('MachineStd-Bold.otf', 30)
        text2 = font2.render('Music:', True, (0, 0, 0))
        text3 = font2.render('Difficulty: ', True, (0, 0, 0))
        text1 = font1.render('SETTINGS', True, (0, 0, 0))

        difficulty = diff
        on_off = True
        running = True

        while running:

            mouse = pygame.mouse.get_pos()

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    running = False

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if quit_game_button.click(mouse, (50, 50)):
                        running = False
                        on_button.show()
                    if on_button.click(mouse, (100, 50)):
                        if on_off:
                            on_button.hide()
                            off_button.show()
                            self.sound.stop()
                            on_off = False

                        else:
                            on_button.show()
                            off_button.hide()
                            self.sound.play()
                            on_off = True

                    if hard_button.click(mouse, (100, 50)):
                        if difficulty == 1:
                            difficulty = 2
                            medium_button.show()
                            easy_button.hide()

                        elif difficulty == 2:
                            difficulty = 3
                            hard_button.show()
                            medium_button.hide()

                        else:
                            difficulty = 1
                            easy_button.show()
                            hard_button.hide()

            self.screen.blit(self.background, (0, 0))
            pygame.draw.rect(self.screen, (255, 212, 0), pygame.Rect(60, 70, 480, 480), 300, 50)
            quit_game_button.display()
            self.screen.blit(text1, (235, 100))
            self.screen.blit(text2, (150, 185))
            self.screen.blit(text3, (150, 265))
            easy_button.display()
            medium_button.display()
            hard_button.display()
            off_button.display()
            on_button.display()
            pygame.display.update()

        return difficulty

    def game_page(self, difficulty):

        player_fixed = pygame.image.load('img/space-invaders1.png')
        player_damaged = pygame.image.load('img/space-invaders2.png')
        player_severe_damaged = pygame.image.load('img/space-invaders3.png')
        alien1 = pygame.image.load("img/red_alien.png")
        alien2 = pygame.image.load("img/green_alien.png")
        shoot_sound = pygame.mixer.Sound('shoot.wav')
        shoot_sound.set_volume(0.1)
        alien3 = pygame.image.load("img/pink_alien.png")
        alien4 = pygame.image.load("img/yellow_alien.png")
        single_bullet = pygame.image.load("img/single_bullet.png")
        font = pygame.font.Font('space_invaders.ttf', 30)
        alien1 = pygame.transform.scale(alien1, (50, 50))
        alien2 = pygame.transform.scale(alien2, (50, 50))
        alien3 = pygame.transform.scale(alien3, (50, 50))
        alien4 = pygame.transform.scale(alien4, (50, 50))
        player_fixed = pygame.transform.scale(player_fixed, (130, 100))
        player_damaged = pygame.transform.scale(player_damaged, (130, 100))
        player_severe_damaged = pygame.transform.scale(player_severe_damaged, (130, 100))
        player = Sprite(self.screen, player_fixed, (250, 450))
        bullets = []
        aliens = []
        alien_bullet = []
        alien_frequency = 0
        alien_bullet_frequency = 0
        max_aliens = 0

        if difficulty == 1:
            alien_frequency = 700
            alien_bullet_frequency = 1300
            max_aliens = 7

        if difficulty == 2:
            alien_frequency = 600
            alien_bullet_frequency = 1200
            max_aliens = 8

        if difficulty == 3:
            alien_frequency = 500
            alien_bullet_frequency = 1100
            max_aliens = 9

        health = 100
        points = 0

        running = True

        while running:

            lives_text = font.render(f"Health: {health}%", True, (255, 255, 255))
            points_text = font.render(f"Points: {points}", True, (255, 255, 255))
            mouse = pygame.mouse.get_pos()

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    running = False

                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        running = False

                if ev.type == pygame.MOUSEBUTTONDOWN and len(bullets) <= 1:
                    player.shooting(single_bullet, (player.posX + 45, player.posY - 10), bullets)
                    shoot_sound.play()

            self.screen.blit(self.background, (0, 0))
            player.render()
            player.move(mouse)

            if 30 < health < 70:
                player.change_img(player_damaged)

            if health < 30:
                player.change_img(player_severe_damaged)

            if len(bullets) > 0:
                for bullet in bullets:
                    bullet.render()
                    bullet.shoot(True, 0.2)
                    bullet.delete(bullets, True)

            if len(aliens) < max_aliens:
                generate = random.randint(1, alien_frequency)
            else:
                generate = 0

            if generate == 5:
                pos = 10
                skin = random.randint(1, 4)
                if skin == 1:
                    enemy = Sprite(self.screen, alien1, (random.randint(0, 530), pos))
                elif skin == 2:
                    enemy = Sprite(self.screen, alien2, (random.randint(0, 530), pos))
                elif skin == 3:
                    enemy = Sprite(self.screen, alien3, (random.randint(0, 530), pos))
                else:
                    enemy = Sprite(self.screen, alien4, (random.randint(0, 530), pos))
                aliens.append(enemy)

            if len(aliens) > 0:
                for alien in aliens:
                    alien.render()
                    alien.alien_movement()
                    shooting = random.randint(1, alien_bullet_frequency)
                    if shooting == 10 and len(alien_bullet) < 6:
                        alien.shooting(single_bullet, (alien.posX, alien.posY), alien_bullet)

                    if alien.posY > 600:
                        alien.destroy(aliens, aliens.index(alien))

                    for a_bullet in alien_bullet:
                        a_bullet.render()
                        a_bullet.shoot(False, 0.03)
                        a_bullet.delete(alien_bullet, False)

                        try:
                            if a_bullet.hit((player.posX, player.posY), (130, 100)) and health > 0:
                                a_bullet.destroy(alien_bullet, alien_bullet.index(a_bullet))
                                health -= 10
                            if health == 0:
                                del player
                                running = False

                        except UnboundLocalError:
                            pass

                    try:
                        if bullet.hit((alien.posX, alien.posY), (50, 50)):
                            alien.destroy(aliens, aliens.index(alien))
                            points += 10
                    except UnboundLocalError:
                        pass
            self.screen.blit(lives_text, (0, 0))
            self.screen.blit(points_text, (385, 0))

            pygame.display.update()
