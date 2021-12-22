import pygame
from weather_classes import *
import sys
import requests
pygame.init()

#colours
white = (255,255,255)
api_key = '44e522bdab1e065926ef411813823305'
display = Window(600,500,"Weather Around the World",None,"background.png",None)
window = display.create_window()

search_bar = Text_box(90,10,400,80,str,100)
search_button = Button(500,0,"",",","",white,"",100,100,"search_icon.png")
objects = [search_bar,search_button]
def home():
	location = None
	while True:
		display.update_window(None,pygame.image.load("background.png"))
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
					show_weather(location)
		pygame.display.update()

def show_weather(location):
	weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}".format(location,api_key))
	print(weather_data.json())
	home()


home()