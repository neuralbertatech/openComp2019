from window_manager import WindowManager
from window import Window
import pygame

class Game:
    instance = None

    class __Game:
        def __init__(self, width, height):
            self.window = Window('NeurAlbertaTech', width, height)
            self.window_manager = WindowManager(self.window)

            # Set the window icon
            window_icon = pygame.image.load("NeurAlbertaTechLogo.png")
            pygame.display.set_icon(window_icon)


        def run(self):
            clock = pygame.time.Clock()
            while(1):
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.window.close()
                        return
                    if event.type == pygame.QUIT:
                        self.window.close()
                        return

                self.window_manager.run(events)
                self.window.update()
                clock.tick(100)

                print(self.window.__bg_color__)


    def __init__(self, width = 1280, height = 720):
        if(not self.instance):
            self.instance = self.__Game(width, height)

    def run(self):
        self.instance.run()
