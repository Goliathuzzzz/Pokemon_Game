import pygame


class SpriteSheet(object):
    def __init__(self, filename, hex_colour):
        self.sheet = pygame.image.load(filename).convert()
        self.colourkey = hex_colour

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        # Loads image from x,y,x+offset,y+offset
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if self.colourkey != self.colourkey:
            if self.colourkey == -1:
                self.colourkey = image.get_at((0, 0))
            image.set_colorkey(self.colourkey, pygame.RLEACCEL)
        return image

    # Load a bunch of images and return them as a list
    def images_at(self, rects):
        # Loads multiple images, supply a list of coordinates
        return [self.image_at(rect) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count):
        # Loads a strip of images and returns them as a list
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups)


test = SpriteSheet('graphics/pokemon/gen1/Gen 1 sheet.png', '#fefeff')
test_image = test.image_at((5, 5, 64, 64))
test_image_rect = test_image.get_rect(topleft=(0, 0))
test_images = []


