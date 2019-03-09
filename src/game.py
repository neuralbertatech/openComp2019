import pygame

class Game:
    class __Game:
        def __init__(self, width, height):
            self.window = Window('Hello World', width, height)


        def start(self):
            self.main_menu = MainMenu(self.window)
            while(1):
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESC:
                            self.window.close()
                            break


    instance = None

    def __init__(self, width = 1280, height = 720):
        if(not self.instance):
            self.instance = self.__Game(width, height)

    def start(self):
        self.instance.start()
