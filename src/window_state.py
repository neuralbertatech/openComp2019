from state import State
from primitives import rect
from collections import deque
import pygame
import time
import random
import math
from demon_sprite import DemonSprite
from demon_sprite import Death

class WindowState:
    def __init__(self, state_str, state):
        self.state_str = state_str
        self.state = state

    def __str__(self):
        return self.state_str

    def __cmp__(self, other):
        return cmp(self.state_str, other.state_str)

    def __hash__(self):
        return hash(self.state_str)


class MainMenuState (State):
    def __init__(self, window):
        self.window = window

        width = self.window.get_width()
        height = self.window.get_height()
        self.play_button = rect((width/2)-34, (height*2/5)-14, 68, 28, window.__surface__,'green')
        self.settings_button = rect((width/2)-68, (height*2/5)+20, 135, 28, window.__surface__,'green')
        self.quit_button = rect((width/2)-38, (height*2/5)+50, 135, 28, window.__surface__,'green')
        self.start_time = time.time()
        self.egg_baseline = True


    def run(self):
        if time.time() - self.start_time >= 13:
            self.egg_baseline = False
            
        self.draw_bg()
        self.draw_buttons()
        self.window.update()


    def next(self, events):
        for event in events:
            # Clicked Mouse
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # Clicked on Play Button
                if self.play_button.intersect(pos):
                    self.draw_bg()

                    WindowState.game.state.__init__(self.window)
                    return WindowState.game

                # Clicked on Settings Button
                elif self.settings_button.intersect(pos):
                    self.draw_bg()
                    # NOT IMPLEMENTED YET
                    return WindowState.settings

                # Clicked on Quit Button
                elif self.quit_button.intersect(pos):
                    # Purposely crash program
                    return

            # Pressed return key, start game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.draw_bg()
                WindowState.game.state.__init__(self.window)
                return WindowState.game

        return WindowState.main_menu


    def draw_buttons(self):
        width = self.window.get_width()
        height = self.window.get_height()
        self.play_button.draw()
        self.settings_button.draw()

        if (self.egg_baseline):
            self.window.set_font_size(20)
            self.window.draw_string('Reading EEG baseline, please wait...',(width/2)-(self.window.get_string_width('Reading EEG baseline, please wait...'))/2, (height*2/5), pygame.Color(0,0,0,255))


        else:
            self.window.set_font_size(40)
            #self.window.draw_string('                                                         ',(width/2)-(self.window.get_string_width('                                                         '))/2, (height*2/5)-14, pygame.Color(0,0,0,255))
            self.window.draw_string('Play',(width/2) - (self.window.get_string_width('Play'))/2, (height*2/5)-14, pygame.Color(0,0,0,255))

        self.window.set_font_size(40)
        self.window.draw_string('Quit', (width/2)-(self.window.get_string_width('Quit'))/2, (height*2/5)+20, pygame.Color(0,0,0,255))

    def draw_bg(self):
        color = (0,0,0,255)
        self.window.__surface__.fill(color)


class GameState (State):
    def __init__(self, window):
        self.window = window
        self.frame_bullet = 0
        self.frame_enemy = 0
        self.fire_rate = 100
        self.queue = deque([100, 200, 400, 500, 650])
        self.bullet_count = 200
        self.enemies = []
        self.enemiesStrength = []
        self.score = 0
        self.final_score = 0
        self.start_time = pygame.time.get_ticks() // 1000
        self.projectiles = []
        self.game_over = False
        self.dead_enemies = []

        self.wave = False

        self.soldier = []
        self.soldier.append(pygame.image.load('assets/soldier1.png'))
        self.soldier.append(pygame.image.load('assets/soldier2.png'))
        self.soldier.append(pygame.image.load('assets/soldier3.png'))
        self.soldier.append(pygame.image.load('assets/soldier4.png'))
        self.soldier.append(pygame.image.load('assets/soldier5.png'))
        self.soldier_index = 0

        self.firing = False

        height = self.window.get_height()
        self.player = rect(50,height*4/5,80,200,window.__surface__, 'yellow', 'soldier.png')

    def run(self):
        self.window.clear()
        self.draw()
        self.generate_enemy()
        self.update_enemies()
        self.update_projectiles()
        self.check_collision()
        self.fire_bullet()
        self.score = (pygame.time.get_ticks() // 1000) - self.start_time
        time.sleep(0.0001) # set game velocity by pausing


    def fire_bullet(self):
        if self.fire_rate <= self.frame_bullet and self.bullet_count > 0:
            self.spawn_bullet()
            self.frame_bullet = 0
        else:
            self.frame_bullet += 1


    def next(self, events):

        try:
            if self.window.stream.state == 'high_alpha':
                self.fire_rate = 8
            elif self.window.stream.state == 'low_alpha':
                self.fire_rate = 10000
        except:
            pass
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.fire_rate = 8
                if event.key == pygame.K_l:
                    self.fire_rate = 10000

        if self.game_over:
            self.final_score = self.score
            return WindowState.end_game

        return WindowState.game


    def draw(self):
        color = (35,99,47,255)
        self.window.set_bg_image('cyberpunk-street.png', self.window.get_width, self.window.get_height)

        self.window.draw_string('Bullets: ' + str(self.bullet_count), 0, 0, pygame.Color(5,44,70,100))

        for dead_enemy in self.dead_enemies:
            dead_enemy.rect.draw()
            if dead_enemy.sprite_rate >= 3:
                dead_enemy.update()
                dead_enemy.sprite_rate = 0
            else:
                dead_enemy.sprite_rate += 1

            if dead_enemy.index >= 5:
                self.dead_enemies.pop(0)

        for enemy in self.enemies:
            enemy.rect.draw()
        for projectile in self.projectiles:
            projectile.draw()

        if self.firing == True:
            self.player.set_content(self.soldier[self.soldier_index])
            self.player.draw()
            if self.soldier_index >= 4:
                self.soldier_index = 0
                self.firing = False
            else:
                self.soldier_index += 1
        else:
            self.player.draw()

        if(self.score%60 < 10):
            self.window.draw_string('Time: ' + str(math.floor(self.score/60)) + ':0' + str(self.score%60),  self.window.get_width() - self.window.get_string_width('Time: ' + str(math.floor(self.score/60)) + ':0' + str(self.score%60)), 30, pygame.Color(5,44,70,100))
        else:
            self.window.draw_string('Time: ' + str(math.floor(self.score/60)) + ':' + str(self.score%60),  self.window.get_width() - self.window.get_string_width('Time: ' + str(math.floor(self.score/60)) + ':' + str(self.score%60)), 30, pygame.Color(5,44,70,100))



    def generate_enemy(self):
        if random.randint(-2000, 0)+self.frame_enemy > 60 and self.frame_enemy > 60 and self.wave is False:
            self.spawn_enemy(random.randint(1,15))
            self.frame_enemy = 0

            if random.randint(0, 10) > 8:
                self.wave = True
        else:
            self.frame_enemy += 1

            if self.frame_enemy > random.randint(300, 600):
                self.wave = False


    def spawn_enemy(self, strength):
        height = self.window.get_height()
        width = self.window.get_width()

        # if strength == 1:
        #     enemy = rect(width-50,height*4/5,50,200,self.window.__surface__, 'red', 'zombie.png')
        # elif strength == 2:
        enemy = DemonSprite(width-200,height*3/5,200,400,self.window.__surface__, 'red')
        # elif strength == 3:
        #     enemy = rect(width-50,height*4/5,50,200,self.window.__surface__, 'red', 'zombie.png')
        # elif strength == 4:
        #     enemy = rect(width-50,height*4/5,50,200,self.window.__surface__, 'red', 'zombie.png')
        # else :
        #     enemy = rect(width-50,height*4/5,50,200,self.window.__surface__, 'red', 'zombie.png')
        self.enemies.append(enemy)
        self.enemiesStrength.append(strength)


    def spawn_bullet(self):
        height = self.window.get_height()
        bullet = rect(100,height*4/5+57,30,5,self.window.__surface__, 'gray', 'bullet.png')
        self.projectiles.append(bullet)
        self.bullet_count -= 1
        self.firing = True


    def draw_bg(self):
        color = (35,99,47,255)
        self.window.__surface__.fill(color)


    def update_enemies(self):
        height = self.window.get_height()
        width = self.window.get_width()

        for enemy in self.enemies:
            pygame.Rect.move_ip(enemy.rect.rectangle, -1, 0)
            enemy.rect.x -= 1

            if enemy.sprite_rate >= 7:
                enemy.update()
                enemy.sprite_rate = 0
            else:
                enemy.sprite_rate += 1

            # Display the next enemy's HP
            self.window.draw_string('Next Enemy HP: ' + str(self.enemiesStrength[0] + 1),  width - self.window.get_string_width('Next Enemy HP: ' + str(self.enemiesStrength[0] + 1)), 0, pygame.Color(5,44,70,100))

            # Check if the player is hit by an enemy and execute the end condition
            if(pygame.Rect.colliderect(enemy.rect.rectangle, self.player.rectangle)):
                self.game_over = True

        # Display an empty amount of HP if there are no enemies
        if(len(self.enemies) == 0):
            self.window.draw_string('Next Enemy HP:  ',  width - self.window.get_string_width('Next Enemy HP:  '), 0, pygame.Color(5,44,70,100))


    def update_projectiles(self):
        height = self.window.get_height()

        for projectile in self.projectiles:
            pygame.Rect.move_ip(projectile.rectangle, 40, 0)
            projectile.x += 40

            if(pygame.Rect.collidepoint(projectile.rectangle, 1280, height*4/5+57)):
                self.projectiles.pop(0)


    def check_collision(self):
        try:
            if( pygame.Rect.colliderect(self.enemies[0].rect.rectangle, self.projectiles[0].rectangle) ):
                self.projectiles.pop(0)

                if(self.enemiesStrength[0] == 0):
                    self.dead_enemies.append(Death(self.enemies[0].rect))
                    self.enemies.pop(0)
                    self.enemiesStrength.pop(0)
                else:
                    self.enemiesStrength[0] -= 1
                    enemy_rect = False
        except Exception as e:
                pass


class EndGameState (State):
    def __init__(self, window):
        self.window = window

        width = self.window.get_width()
        height = self.window.get_height()
        self.main_menu_button = rect((width/2)-75, (height*2/5)+100, 150, 28, window.__surface__,'green')


    def run(self):
        self.draw_bg()
        self.draw()
        self.window.update()


    def next(self, events):
        for event in events:
            # Clicked Mouse
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # Clicked on main menu button
                if self.main_menu_button.intersect(pos):
                    self.draw_bg()
                    return WindowState.main_menu


            # Pressed return key, end game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.draw_bg()
                return WindowState.main_menu

        return WindowState.end_game


    def draw(self):
        width = self.window.get_width()
        height = self.window.get_height()
        self.main_menu_button.draw()
        self.window.set_font_size(40)
        self.window.draw_string('GAME OVER',(width/2)-90, (height*2/5)-14, pygame.Color(35,0,0,0))
        self.window.draw_string('You died.', (width/2)-60, (height*2/5)+20, pygame.Color(35,0,0,0))

        if(WindowState.game.state.final_score >= 120 or WindowState.game.state.final_score < 60 ):
            self.window.draw_string('You survived ' + str(math.floor(WindowState.game.state.final_score/60)) + ' minutes ' + str(WindowState.game.state.final_score%60) + ' seconds',  (width/2) - (self.window.get_string_width('You survived ' + str(math.floor(WindowState.game.state.final_score/60)) + ' minutes ' + str(WindowState.game.state.final_score%60) + ' seconds'))/2, (height*2/5)+50, pygame.Color(35,0,0,0))
        else:
            self.window.draw_string('You survived ' + str(math.floor(WindowState.game.state.final_score/60)) + ' minute ' + str(WindowState.game.state.final_score%60) + ' seconds',  (width/2) - (self.window.get_string_width('You survived ' + str(math.floor(WindowState.game.state.final_score/60)) + ' minute ' + str(WindowState.game.state.final_score%60) + ' seconds'))/2, (height*2/5)+50, pygame.Color(35,0,0,0))

        self.window.draw_string('Main Menu', (width/2)-75, (height*2/5)+100, pygame.Color(35,0,0,0))

    def draw_bg(self):
        color = (35,0,0,100)
        self.window.__surface__.fill(color)
