import pygame

# colours
black = (0, 0, 0)
white = (255, 255, 255)


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
		elif self.background_img:
			image = pygame.image.load(self.background_img)
			self.display.blit(image, (0, -200))
		elif colour:
			self.display.fill(colour)
		elif self.background_colour:
			self.display.fill(self.background_colour)


class Text_box():
	def __init__(self, x, y, width, height, input_type, font_size, mask=False):
		self.x = x
		self.y = y
		self.text = ""
		self.width = width
		self.height = height
		self.font_size = font_size
		self.rect = pygame.Rect(x, y, width, height)  # Creates the textbox using rect.
		self.font = pygame.font.SysFont(None, self.font_size)  # setting the font to pygame default (None)
		self.colour = black  # colour of the box
		self.font_colour = white  # colour of the font
		self.text_rect = self.font.render(self.text, True, self.font_colour)  # creating the text surface
		self.active = False  # setting to False
		self.input_type = input_type  # expected data type of input (could be str, int or float)
		self.mask = mask  # characters replaced by *
		try:
			self.variable = self.input_type(self.text)  # setting input to correct type
		except:
			self.variable = None
		self.active = False

	def add_chars(self, event):  # A method which adds user's input to the textbox
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):  # checks if textbox clicked
				self.active = True  # sets to True
				self.colour = white  # changes colour to white
			else:
				self.active = False  # if mouse clicks off the textbox
				self.colour = black
		if event.type == pygame.KEYDOWN:  # adding characters
			if self.active:
				# Refreshing text
				if event.key == pygame.K_RETURN:
					self.active = False
				elif event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
				elif self.text_rect.get_width() + 10 < self.rect.width:
					self.text += event.unicode
			if self.mask:
				self.text_rect = self.font.render("*" * len(self.text), True,
												  self.font_colour)  # renders the text (masked)
			else:
				self.text_rect = self.font.render(self.text, True, self.font_colour)  # renders the text

	def draw(self, display):  # a method to draw the textbox to the screen
		display.blit(self.text_rect, (self.rect.x + 5, self.rect.y + 5))
		pygame.draw.rect(display, self.colour, self.rect, 2)


	def get_text(self):
		return self.text