from window_manager import WindowManager
from window import Window
import pygame

class Game:
    instance = None

    class __Game:
        def __init__(self, width, height):
            self.window = Window('Hello World', width, height)
            self.window_manager = WindowManager(self.window)
            


        def run(self):
            while(1):
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.window.close()
                            return

                self.window_manager.run(events)
                self.window.update()
                pygame.clock.tick(15)


    def __init__(self, width = 1280, height = 720):
        if(not self.instance):
            self.instance = self.__Game(width, height)

    def run(self):
        self.instance.run()
