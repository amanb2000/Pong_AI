import pygame
class PongGame:
	def __init__(self):
		self.ball_x = 0
		self.ball_y = 0
		self.ball_vx = 20
		self.ball_vy = 0
		self.ball_maxv = 20
		self.ball_size = 25

		self.width = 800
		self.height = 600

		self.playerSpeed = 10

		self.playerLeft = self.height/2
		self.playerRight = self.height/2
		self.playerSize = [5, 100]

		self.padding = 5

	def transition(self, moveLeft, moveRight):
		# moves: 1 = up, 0 = still, -1 = down
		if self.ball_x < 0 or self.ball_x+self.ball_size > self.width:
			self.ball_vx *= -1
		if self.ball_y < 0 or self.ball_y+self.ball_size > self.height:
			self.ball_vy *= -1

		self.ball_x += self.ball_vx
		self.ball_y += self.ball_vy

	

