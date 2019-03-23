import pygame

class primitive:
    def draw(self):
        assert 0;

    def intersect(self, x, y):
        assert 0;

class rect(primitive):
    def __init__(self, x, y, w, h, screen, colour):
        self.rectangle = pygame.Rect(x, y, w, h)
        self.screen = screen

        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.colour = colour

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color(self.colour), self.rectangle)

    def intersect(self, pos):
        x = pos[0]
        y = pos[1]
        if x - self.x < self.width and x >= self.x and \
           y - self.y < self.height and y >= self.y:
            return True

        return False
