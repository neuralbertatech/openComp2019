from state import State
from primitives import rect
from collections import deque
import pygame
import time
import random
from demon_sprite import DemonSprite

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

        green = (0,255,0)
        width = self.window.get_width()
        height = self.window.get_height()
        self.play_button = rect((width/2)-34, (height*2/5)-14, 68, 28, window.__surface__,'green')
        self.settings_button = rect((width/2)-68, (height*2/5)+20, 135, 28, window.__surface__,'green')
        self.quit_button = rect((width/2)-38, (height*2/5)+50, 135, 28, window.__surface__,'green')

    def run(self):
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
                return WindowState.game

        return WindowState.main_menu

    def draw_buttons(self):
        width = self.window.get_width()
        height = self.window.get_height()
        self.play_button.draw()
        self.settings_button.draw()
        self.window.set_font_size(40)
        self.window.draw_string('Play',(width/2)-34, (height*2/5)-14, pygame.Color(0,0,0,100))
        self.window.draw_string('Settings', (width/2)-68, (height*2/5)+20, pygame.Color(0,0,0,100))
        self.window.draw_string('Quit', (width/2)-38, (height*2/5)+50, pygame.Color(0,0,0,100))


    def draw_bg(self):
        color = (35,99,47,100)
        self.window.__surface__.fill(color)

class SettingsState (State):
    pass

class GameState (State):
    def __init__(self, window):
        self.window = window
        self.frame_bullet = 0
        self.frame_enemy = 0
        self.fire_rate = 100
        self.queue = deque([100,200,400, 500, 650])
        self.bullet_count = 1000
        self.enemies = []
        self.enemiesStrength = []
        self.score = 0
        self.projectiles = []

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
        self.score = pygame.time.get_ticks() // 1000
        time.sleep(0.0001) # set game velocity by pausing

    def fire_bullet(self):
        if self.fire_rate <= self.frame_bullet:
            self.spawn_bullet()
            self.frame_bullet = 0
        else:
            self.frame_bullet += 1

    def next(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if self.fire_rate > 10:
                        self.fire_rate -= 10
                if event.key == pygame.K_l:
                    if self.fire_rate < 100:
                        self.fire_rate += 10

        return WindowState.game


    def draw(self):
        color = (35,99,47,100)
        self.window.set_bg_image('cyberpunk-street.png', self.window.get_width, self.window.get_height)

        self.window.draw_string('Bullets: ' + str(self.bullet_count), 0, 0, pygame.Color(5,44,70,100))

        for enemy in self.enemies:
            enemy.rect.draw()
        for projectile in self.projectiles:
            projectile.draw()

        self.player.draw()

        self.window.draw_string('Time: ' + str(self.score),  self.window.get_width() - self.window.get_string_width('Time: ' + str(self.score)), 30, pygame.Color(5,44,70,100))




    def generate_enemy(self):
        if random.randint(-2000, 0)+self.frame_enemy > 60 and self.frame_enemy > 60:
            self.spawn_enemy(random.randint(1,5))
            self.frame_enemy = 0
        else:
            self.frame_enemy += 1


    def spawn_enemy(self, strength):
        height = self.window.get_height()
        width = self.window.get_width()

        # if strength == 1:
        #     enemy = rect(width-50,height*4/5,50,200,self.window.__surface__, 'red', 'zombie.png')
        # elif strength == 2:
        enemy = DemonSprite(width-50,height*4/5,50,200,self.window.__surface__, 'red')
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
        bullet = rect(100,height*4/5+67,30,5,self.window.__surface__, 'gray', 'bullet.png')
        self.projectiles.append(bullet)
        self.bullet_count -= 1

    def update_enemies(self):
        height = self.window.get_height()
        width = self.window.get_width()
        for enemy in self.enemies:
            pygame.Rect.move_ip(enemy.rect.rectangle, -1, 0)
            enemy.update()

            self.window.draw_string('Next Enemy HP: ' + str(self.enemiesStrength[0] + 1),  width - self.window.get_string_width('Next Enemy HP: ' + str(self.enemiesStrength[0] + 1)), 0, pygame.Color(5,44,70,100))

        # Display an empty amount of HP if
        if(len(self.enemies) == 0):
            self.window.draw_string('Next Enemy HP:  ',  width - self.window.get_string_width('Next Enemy HP:  '), 0, pygame.Color(5,44,70,100))


    def update_projectiles(self):
        height = self.window.get_height()

        for projectile in self.projectiles:
            pygame.Rect.move_ip(projectile.rectangle, 15, 0)
            projectile.x += 15

            if(pygame.Rect.collidepoint(projectile.rectangle, 1280, height*4/5+67)):
                self.projectiles.pop(0)

    def check_collision(self):
        try:
            if( pygame.Rect.colliderect(self.enemies[0].rectangle, self.projectiles[0].rectangle) ):
                self.projectiles.pop(0)

                if(self.enemiesStrength[0] == 0):
                    self.enemies.pop(0)
                    self.enemiesStrength.pop(0)
                else:
                    self.enemiesStrength[0] -= 1

        except Exception as e:
                pass
