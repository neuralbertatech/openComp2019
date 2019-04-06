import pygame

# object primitives
class primitive:
    def draw(self):
        assert 0

    def intersect(self, x, y):
        assert 0

# class for the hitboxes of the game
# also draws the
class rect(primitive):
    def __init__(self, x, y, w, h, screen, colour, content = None):

        # create a python rectangle
        self.rectangle = pygame.Rect(x, y, w, h)
        self.screen = screen # where everything is printed

        # coordingates of the rectangle
        self.x = x
        self.y = y
        # attributes of the rectangle
        self.width = w
        self.height = h
        self.colour = colour
        self.content = content # the image that will be displayed

    # draw the rectangle. If there is no image then do not draw anything
    def draw(self):
        if self.content == None:
            pass
        elif not isinstance(self.content,str):
             self.screen.blit(self.content, (self.x, self.y))
        else:
            self.screen.blit(pygame.image.load(self.content), (self.x, self.y))

    # checks if the player clicked on something
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
