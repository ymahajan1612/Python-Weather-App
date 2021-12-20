import pygame
from weather_classes import *
import sys
pygame.init()


def home():
	display = Window(600,500,"Weather Around the World",None,"mountain_bg.jpg",None)
	window = display.create_window()
	search_bar = Text_box(100,10,400,80,str,100)
	while True:
		display.update_window(None,pygame.image.load("mountain_bg.jpg"))
		search_bar.draw(window)
		for event in pygame.event.get():
			search_bar.add_chars(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()


home()