"""A Class to represent a single alien in the fleet"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self, ai_game):
		"""Initialize the alien and set it's starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		# Load the alien image and set it's rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top right of the screen.
		self.rect.x =  self.rect.width
		self.rect.y = .75 * self.rect.height

		# Store the alien's exact vertical position.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the alien down"""
		self.y += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.y = self.y


	def check_edges(self):
		"""Return true if alien is at edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
			return True