import pygame.font

class Button():
    '''A model of a play button for Target Practice'''
    def __init__(self, screen, msg):
        '''Initialise play button attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_colour = (255, 0, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont('arialblack', 32)

        #Build rect and set position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery + 100
        self.rect.centerx = self.screen_rect.centerx


        #The button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''Turn msg into rendered image and center text on button'''
        self.msg_image = self.font.render(msg, True, self.text_colour,
            self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw blank button and the draw message
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)