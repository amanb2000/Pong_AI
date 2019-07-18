import pygame
import math
import numpy as np 

class PongGame:
	def __init__(self):
		self.ball_x = 100
		self.ball_y = 100
		self.ball_vx = 20
		self.ball_vy = 5
		self.ball_maxv = 25
		self.ball_size = 40

		self.width = 800
		self.height = 600

		self.playerSpeed = 40

		self.playerLeft = self.height/2
		self.playerRight = self.height/2
		self.playerSize = [40, 100]

		self.padding = 15

	def getState(self, player): # 0 = left, 1 = right player
		if player == 0: # left player's perspective
			return np.array([self.playerLeft, self.ball_x, self.ball_y, self.ball_vx, self.ball_vy, self.playerRight])
		elif player == 1:
			return np.array([self.playerRight, self.ball_x*-1, self.ball_y, self.ball_vx*-1, self.ball_vy, self.playerLeft])
		print('Invalid player numer '+player+' please enter either 0 (left) or 1 (right)')

	def transition(self, moveLeft, moveRight): # return 0 for alive; -1 for left ded, 1 for right ded
		# moves: 1 = up, 0 = still, -1 = down
		# if self.ball_x < 0 or self.ball_x+self.ball_size > self.width:
		# 	self.ball_vx *= -1
		if self.ball_y < 0 or self.ball_y+self.ball_size > self.height:
			self.ball_vy *= -1

		if self.ball_x < self.padding+self.playerSize[0]:
			if self.playerLeft < self.ball_y+self.ball_size/2 and self.playerLeft+self.playerSize[1] > self.ball_y-(self.ball_size/2):
				self.ball_x = self.playerSize[0]+self.padding
				print('bouncing left') 
				self.ball_vx *= -1
				xNeg = (self.ball_vx < 0)
				yNeg = (self.ball_vy < 0)

				self.ball_vx = abs(self.ball_vx)
				self.ball_vy = abs(self.ball_vy)

				d = abs((self.ball_y+self.ball_size/2)-(self.playerLeft+self.playerSize[1]/2))
				ratio = d/self.playerSize[1]

				self.ball_vy = ratio*self.ball_maxv*1.5
				self.ball_vx = math.sqrt(abs(self.ball_maxv*self.ball_maxv - self.ball_vy*self.ball_vy))

				if xNeg:
					self.ball_vx *= -1
				if yNeg:
					self.ball_vy *= -1
				# DONE: Implement weird bouncing
			else:
				print('ded left');
				return -1

		if self.ball_x > self.width-self.padding-self.playerSize[0]-self.ball_size:
			print('passed right')
			if self.playerRight < self.ball_y+self.ball_size/2 and self.playerRight+self.playerSize[1] > self.ball_y-(self.ball_size/2):
				self.ball_x = self.width-self.ball_size-self.padding-self.playerSize[0]
				print('bouncing to the left') 
				self.ball_vx *= -1
				xNeg = (self.ball_vx < 0)
				yNeg = (self.ball_vy < 0)

				self.ball_vx = abs(self.ball_vx)
				self.ball_vy = abs(self.ball_vy)

				d = abs((self.ball_y+self.ball_size/2)-(self.playerRight+self.playerSize[1]/2))
				ratio = d/self.playerSize[1]

				self.ball_vy = ratio*self.ball_maxv*1.5
				self.ball_vx = math.sqrt(abs(self.ball_maxv*self.ball_maxv - self.ball_vy*self.ball_vy))

				if xNeg:
					self.ball_vx *= -1
				if yNeg:
					self.ball_vy *= -1
				# DONE: Implement weird bouncing
			else:
				print('ded right');
				return 1

		self.ball_x += self.ball_vx
		self.ball_y += self.ball_vy

		if moveLeft == 1 and self.playerLeft > 0:
			self.playerLeft -= self.playerSpeed
			print('left up')
		elif moveLeft == -1 and self.playerLeft+self.playerSize[1] < self.height:
			self.playerLeft += self.playerSpeed

		if moveRight == 1 and self.playerRight > 0:
			self.playerRight -= self.playerSpeed
		elif moveRight == -1 and self.playerRight+self.playerSize[1] < self.height:
			self.playerRight += self.playerSpeed
			print('right down')

		if(self.playerLeft < 0):
			self.playerLeft = 0
		elif(self.playerLeft+self.playerSize[1] > self.height):
			self.playerLeft = self.height - self.playerSize[1]

		if(self.playerRight < 0):
			self.playerRight = 0
		elif(self.playerRight+self.playerSize[1] > self.height):
			self.playerRight = self.height - self.playerSize[1]

		return 0

