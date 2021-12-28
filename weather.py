import pygame
from weather_classes import *
import sys
import requests
import os
import pycountry

pygame.init()


countries = [country.name.lower() for country in list(pycountry.countries)]

# colours
white = (255, 255, 255)

api_key = '44e522bdab1e065926ef411813823305'
display = Window(600, 500, "Weather Around the World", None, "background.png", None)
window = display.create_window()
search_bar = Text_box(10, 10, 400, 50, str, 100)
search_button = Button(420, 10, None, 40, black, white, "Get Weather", 175, 50, None)
objects = [search_bar, search_button]
relevant_data = None


def home():
	location = None
	while True:
		display.update_window(None, pygame.image.load("background.png"))
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
					get_weather(location)
		if relevant_data:
			print("Hi")
		pygame.display.update()


def get_weather(location):
	global relevant_data
	weather_data = requests.get(
		"https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}".format(location, api_key)).json()
	if not location.lower() in countries:
		try:
			icon_directory = os.path.join(os.getcwd(), "icons")
			icon_directory = os.path.join(icon_directory, "{}.png".format(weather_data['weather'][0]['icon']))
			relevant_data = {"country": weather_data['sys']['country'],
							 "city": weather_data['name'],
							 "weather": weather_data['weather'][0]['main'],
							 "weather_desc": weather_data['weather'][0]['description'],
							 "weather_icon": pygame.image.load(icon_directory),
							 "temperature":weather_data['main']['temp']+"°C"}

			print(weather_data)
		except:
			relevant_data = None
	else:
		relevant_data = None



home()

