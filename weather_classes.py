import pygame

class Window:
    def __init__(self, width, height, caption=None, icon=None, background_img=None, background_colour=None):
        self.width = width  # window's width
        self.height = height  # height
        self.caption = caption
        self.icon = icon
        self.background_img = background_img
        self.background_colour = background_colour

    def create_window(self):
        display = pygame.display.set_mode((self.width, self.height))  # setting up display dimensions
        self.display = display  # Creates new attribute: display
        if self.caption:
            pygame.display.set_caption(self.caption)  # setting caption
        if self.icon:
            img = pygame.image.load(self.icon)  # setting window icon
            pygame.display.set_icon(img)
        if self.background_img:  # setting background image
            img = pygame.image.load(self.background_img)  # loading background image
            display.blit(img, (0, -200))  # Drawing image to window
        elif self.background_colour:  # if there is a background colour
            display.fill(self.background_colour)
        return display  # returns the display

    # method to refresh window
    def update_window(self, colour=None, background=None):
        if background:
            self.display.blit(background, (0, 0))
            background.set_alpha(200)
        elif self.background_img:
            image = pygame.image.load(self.background_img)
            self.display.blit(image, (0, -200))
        elif colour:
            self.display.fill(colour)
        elif self.background_colour:
            self.display.fill(self.background_colour)