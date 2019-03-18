from state import State
from primitives import rect
from collections import deque
import pygame

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
        self.play_button = rect(width/2,height*2/5,30,15,green,window.__surface__)

    def run(self):
        self.draw_buttons()
        self.draw_bg()
        self.window.update()

    def next(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if self.play_button.intersect(pos):
                    print("State: {}".format(WindowState.game))
                    return WindowState.game
                
                #elif self.settings_button.clicked(pos):
                #    return WindowState.settings
                
        return WindowState.main_menu

    def draw_buttons(self):
        width = self.window.get_width()
        height = self.window.get_height()
        self.play_button.draw()        
        self.window.draw_string('Play', width/2, height*2/5)

    def draw_bg(self):
        self.window.set_bg_color('green')

class SettingsState (State):
    pass

class GameState (State):
    def __init__(self, window):
        self.window = window
        self.frame = 0;
        self.queue = deque([100,200,400, 500, 650])
        self.enemies = []
        self.projectiles = []
        self.window.set_bg_color('blue')
        
        height = self.window.get_height()
        red = (255,0,0)
        self.player = rect(50,height*4/5,50,200,red,window.__surface__)

        
    def run(self):
        self.window.clear()
        self.generate_enemy()
        self.update_enemies()
        self.update_projectiles()
        self.check_collision()
        self.player.draw()
        self.frame += 1
        self.window.update()

        
    def next(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spawn_bullet()

        
                
        return WindowState.game
    

    def generate_enemy(self):
        self.handle_enemy_queue()

        while(self.queue[0] < self.frame):
            self.queue.popleft()
            self.spawn_enemy()


    def handle_enemy_queue(self):
        pass


    def spawn_enemy(self):
        height = self.window.get_height()
        width = self.window.get_width()
        blue = (0,0,255)
        enemy = rect(width-50,height*4/5,50,200,blue,self.window.__surface__)
        self.enemies.append(enemy)

    def spawn_bullet(self):
        height = self.window.get_height()
        yellow = (255,0,255)
        bullet = rect(50,height*4/5+25,30,5,yellow,self.window.__surface__)
        self.projectiles.append(bullet)


    def update_enemies(self):
        for enemy in self.enemies:
            enemy.x -= 2
            enemy.draw()

    def update_projectiles(self):
        for projectile in self.projectiles:
            projectile.x += 6
            projectile.draw()

    def check_collision(self):
        try:
            pos = (self.projectiles[0].x + self.projectiles[0].width, \
                   self.projectiles[0].y + self.projectiles[0].height/2)
            print(pos)
            print("ENEMIES {}".format(self.enemies[0].y))
            if(self.enemies[0].intersect(pos)):
                self.projectiles.pop(0)
                self.enemies.pop(0)
                print("DESTROYED")
        except Exception as e:
                print("BROKE {}".format(e))
