import pygame


class Entity(pygame.sprite.Sprite):
	def __init__(self, groups):
		super().__init__(groups)
		self.frame_index = 0
		self.animation_speed = 0.15
		# safe defaults
		self.direction = pygame.math.Vector2()

	def move(self, speed):
		# normalize direction vector if not zero-length
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		# horizontal movement and collision
		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')

		# vertical movement and collision
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')

		# sync rect to hitbox
		self.rect.center = self.hitbox.center

	def collision(self, direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0:  # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0:  # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0:  # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0:  # moving up
						self.hitbox.top = sprite.hitbox.bottom
