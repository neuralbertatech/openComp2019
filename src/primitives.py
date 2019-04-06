import pygame

# class we use to make hit boxes in the game. It utilizes the
class primitive:
    def draw(self):
        assert 0

    def intersect(self, x, y):
        assert 0

class rect(primitive):
    def __init__(self, x, y, w, h, screen, colour, content = None):
        self.rectangle = pygame.Rect(x, y, w, h)
        self.screen = screen

        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.colour = colour
        self.content = content

    def draw(self):
        if self.content == None:
            pass
        elif  not isinstance(self.content,str):
             self.screen.blit(self.content, (self.x, self.y))
        else:
            self.screen.blit(pygame.image.load(self.content), (self.x, self.y))

    def intersect(self, pos):
        x = pos[0]
        y = pos[1]
        if x - self.x < self.width and x >= self.x and \
           y - self.y < self.height and y >= self.y:
            return True

        return False

    def getX():
        return self.x

    def getY():
        return self.y

    def set_content(self, content):
        self.content = content
