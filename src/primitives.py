import pygame

class primitive:
    def draw(self):
        assert 0;

    def intersect(self, x, y):
        assert 0;

class rect(primitive):
    def __init__(self, x, y, w, h, color, screen):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.color = color
        self.screen = screen

    def draw(self):
        pos = [self.x, self.y, self.width, self.height]
        pygame.draw.rect(self.screen, self.color, pos)

    def intersect(self, pos):
        print(pos)
        x = pos[0]
        y = pos[1]
        if x - self.x < self.width and x >= self.x and \
           y - self.y < self.height and y >= self.y:
            return True

        return False
