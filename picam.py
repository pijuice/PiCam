#!/usr/bin/python
import pygame, os, sys, time
import RPi.GPIO as GPIO
from subprocess import call
from pygame.locals import *


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()

pygame.mouse.set_visible(0)
BACKDISPLAY = pygame.display.set_mode((320, 240))

BLACK =  (  0,   0,   0)
WHITE =  (255, 255, 255)
RED   =  (255,   0,   0)
GREEN =  (  0, 255,   0)
BLUE  =  (  0,   0, 255)
PURPLE = (255,   0, 255)

file

argument = "raspistill -o photo.jpg -t 0"
filename = "photo.jpg"

logo1 = pygame.image.load("/home/pi/Downloads/pijuice small.jpg")
logo2 = pygame.transform.scale(logo1,(320, 100))

BACKDISPLAY.fill(WHITE)
BACKDISPLAY.blit(logo2, (0, 70))
pygame.display.flip()

icon1 = pygame.image.load("/home/pi/Downloads/icon.jpg")
icon2 = pygame.transform.scale(icon1,(200, 210))

while True:

	if(GPIO.input(27) ==0):

			BACKDISPLAY.fill(WHITE)
			BACKDISPLAY.blit(icon2, (60, 25))
			pygame.display.flip()
			time.sleep(0.25)

			call ([argument], shell = True)
			surf = pygame.image.load(filename)
			picture = pygame.transform.scale(surf,(320, 240))
			BACKDISPLAY.blit(picture,(0,0))		
			pygame.display.flip()
			time.sleep(8)

			BACKDISPLAY.fill(WHITE)
    			BACKDISPLAY.blit(logo2, (0, 70))
       			pygame.display.flip()


GPIO.cleanup()
