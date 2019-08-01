import pygame, math, sys
from pygame.locals import *
import random

import os

SCREEN_X = 1000
SCREEN_Y = 500

class Dinosaur(pygame.sprite.Sprite):
	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		folder = os.path.dirname(os.path.realpath(__file__))
		self.image = pygame.image.load(os.path.join(folder, "dinosaur.jpeg"))
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = pygame.Rect(self.image.get_rect())

		self.rect.x = 50
		self.rect.y = 300
		
		self.y_velocity = 0

	def jump(self):
		self.y_velocity = -40

	def update(self):
		#if jumping
		self.y_velocity += 5
		if 300 - self.rect.y <= self.y_velocity:
			self.rect.y = 300
			self.y_velocity = 0	

		self.rect.y += self.y_velocity
		#gravity

class Cactus(pygame.sprite.Sprite):
	def __init__(self, width, height, speed):

		pygame.sprite.Sprite.__init__(self)
		folder = os.path.dirname(os.path.realpath(__file__))
		self.image = pygame.image.load(os.path.join(folder, "cactus.jpeg"))
		self.image = pygame.transform.scale(self.image, (width, height))
		self.rect = pygame.Rect(self.image.get_rect())

		self.width = width
		self.height = height

		self.rect.x = SCREEN_X - width
		self.rect.y = 350 - height

		self.spe = speed

	def update(self):
		self.rect.x -= self.spe

class Game():

	def cactus_generator(self):
		number = random.randint(300, 1401)
		test = True
		for cactus in self.cacti:
			if SCREEN_X - cactus.rect.x < number:
				test = False
		if test:
			self.cacti.add(Cactus(25, 50, self.speed))
	
	def Game_over(self, dinosaur, screen, clock, font):
		while True:
			clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and \
				event.key == pygame.K_ESCAPE:
					return

			text = font.render('Game Over!', True, (50, 50, 50), (200, 200, 200)) 
			textRect = text.get_rect()  
			textRect.center = (500, 200) 
			screen.blit(text,textRect)
			pygame.display.update()

			#reset everything
			self.score = 0
			self.cacti = pygame.sprite.Group()
			dinosaur.rect.x = 50
			dinosaur.rect.y = 300

			return 0

	def main(self, screen):
		clock = pygame.time.Clock()
		#Sprite Groups
		self.cacti = pygame.sprite.Group()
		#Objects
		dinosaur = Dinosaur()

		#initialize
		self.score = 0
		font = pygame.font.Font('freesansbold.ttf', 15) 

		self.speed = 10

		while True:
			clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and \
				event.key == pygame.K_ESCAPE:
					return

			#check for collisions
			collisions = pygame.sprite.spritecollide(dinosaur, self.cacti, False)

			#Game Over
			if len(collisions) != 0:
				self.Game_over(dinosaur, screen, clock, font)
				while True:
					clock.tick(500)
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							return
						if event.type == pygame.KEYDOWN and \
						event.key == pygame.K_ESCAPE:
							return

					key_dict = pygame.key.get_pressed()
					if key_dict[pygame.K_UP]:
						break
					elif key_dict[pygame.K_SPACE]:
						break
				continue

			#generate cacti
			if self.score >= 150:
				self.cactus_generator()

			#move
			if dinosaur.y_velocity != 0 or dinosaur.rect.y != 300:
				dinosaur.update()
			else:
				key_dict = pygame.key.get_pressed()
				if key_dict[pygame.K_UP]:
					dinosaur.jump()
				elif key_dict[pygame.K_SPACE]:
					dinosaur.jump()
			#update
			self.cacti.update()

			#draw
			#background
			screen.fill((200, 200, 200))
			#bottom line
			pygame.draw.line(screen, (0, 0, 0), (0, 350), (1000, 350))
			#cacti and dinosaur
			screen.blit(dinosaur.image, (dinosaur.rect.x, dinosaur.rect.y))
			self.cacti.draw(screen)

			#update score by 10
			self.score += 10
			#display score
			text = font.render('Score ' + str(self.score), True, (0, 0, 0), (200, 200, 200)) 
			textRect = text.get_rect()  
			textRect.center = (120, 35) 
			screen.blit(text,textRect)

			#change speed based on score
			if self.score % 500 == 0:
				self.speed += 1
				for cactus in self.cacti:
					cactus.spe = self.speed
			#end draw
			pygame.display.update()

			#remove cacti that are off the screen
			for cactus in self.cacti:
				if cactus.rect.x <= -cactus.width:
					self.cacti.remove(cactus)

pygame.init()
screen = pygame.display.set_mode((1000 ,500))
Game().main(screen)
