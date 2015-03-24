#PiJuice Compact Camera 
#Nick Pestell 2015

#!/usr/bin/python

import pygame, os, sys, time
import RPi.GPIO as GPIO
from subprocess import call
from pygame.locals import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP) # set the GPIO pin for the capture photo push button

os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()

pygame.mouse.set_visible(0)
BACKDISPLAY = pygame.display.set_mode((320, 240)) # initialise a window with the correct resolution

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
PURPLE = (255, 0, 255)

file

argument = "raspistill -o photo.jpg -t 0" # command to take photo
filename = "photo.jpg" 

logo1 = pygame.image.load("/home/PiCam/PiJuice/pijuice small.jpg") # load pijuice logo
logo2 = pygame.transform.scale(logo1,(320, 100)) # transform pijuice logo to fit screen

BACKDISPLAY.fill(WHITE) # set a white background
BACKDISPLAY.blit(logo2, (0, 70)) # position logo in centre of screen
pygame.display.flip() 

icon1 = pygame.image.load("/home/PiCam/PiJuice/icon.jpg") # load pijuice icon
icon2 = pygame.transform.scale(icon1,(200, 210)) # transform pijuice icon to fit screen

while True:

	if(GPIO.input(27) ==0): # condition for capture photo push button to be activated

		BACKDISPLAY.fill(WHITE) 
		BACKDISPLAY.blit(icon2, (60, 25)) # change background image to the icon
		pygame.display.flip()
		time.sleep(0.25) # 
	
		call ([argument], shell = True) # call the "raspistill" bash command
		surf = pygame.image.load(filename) # load the photo just taken
		picture = pygame.transform.scale(surf,(320, 240)) # transform photo to fill screen
		BACKDISPLAY.blit(picture,(0,0)) # change background image to the photo
		pygame.display.flip()
		time.sleep(8) # leave for 8 seconds

		BACKDISPLAY.fill(WHITE) # return to original screen
		BACKDISPLAY.blit(logo2, (0, 70))
		pygame.display.flip()

GPIO.cleanup()
