import pygame
from weather_classes import *
import sys
pygame.init()

#colours
white = (255,255,255)

def home():
	display = Window(600,500,"Weather Around the World",None,"mountain_bg.jpg",None)
	window = display.create_window()
	search_bar = Text_box(90,10,400,80,str,100)
	#search_icon = pygame.image.load("search_icon.png")
	search_button = Button(500,0,"",",","",white,"",100,100,"search_icon.png")
	location = None
	while True:
		display.update_window(None,pygame.image.load("mountain_bg.jpg"))
		search_bar.draw(window)
		search_button.draw(window)
		for event in pygame.event.get():
			search_bar.add_chars(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if search_button.isClicked(pygame.mouse.get_pos()):
					location = search_bar.get_text()
					print(location)
		pygame.display.update()


home()