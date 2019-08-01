import pygame, math, sys
from pygame.locals import *
import random

SCREEN_X = 1000
SCREEN_Y = 500

class Dinosaur(pygame.sprite.Sprite):
	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("data:image/jpeg;base64,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")
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
		self.image = pygame.image.load("cactus.jpeg")
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
