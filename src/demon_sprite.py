import pygame as pygame
from primitives import rect

class DemonSprite(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,screen,color,):
        super(DemonSprite, self).__init__()
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('assets/demon1.png'))
        self.images.append(pygame.image.load('assets/demon2.png'))
        self.images.append(pygame.image.load('assets/demon3.png'))
        self.images.append(pygame.image.load('assets/demon4.png'))
        self.images.append(pygame.image.load('assets/demon5.png'))
        self.images.append(pygame.image.load('assets/demon6.png'))

        self.sprite_rate = 0



        #index value to get the image from the array
        #initially it is 0
        self.index = 0

        #now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        self.rect = rect(x,y,w,h,screen,color,self.image)

    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0

        #finally we will update the image that will be displayed
        self.image = self.images[self.index]

        #if self.index >= 0 and self.index <= 4:

        self.rect.set_content(self.image)
