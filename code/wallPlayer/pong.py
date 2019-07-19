import pygame
import math
import numpy as np 
import random

class PongGame:
	def __init__(self):
		# self.ball_x = random.random()*100+100
		# self.ball_y = random.random()*100+100
		self.ball_x = 100+100
		self.ball_y = 100+100
		self.ball_vx = 15
		self.ball_vy = 10
		self.ball_maxv = 25
		self.ball_size = 40

		self.width = 800
		self.height = 600

		self.playerSpeed = 40

		self.playerLeft = self.height/2
		self.playerRight = self.height/2
		self.playerSize = [40, 100]

		self.padding = 15

	def getState(self, player): # -1 = left, 1 = right player
		if player == -1: # left player's perspective
			return np.array([self.playerLeft, self.ball_x, self.ball_y, self.ball_vx, self.ball_vy, self.playerRight])
		elif player == 1:
			return np.array([self.playerRight, self.ball_x*-1, self.ball_y, self.ball_vx*-1, self.ball_vy, self.playerLeft])

	def transition(self, moveLeft): # return 0 for alive; -1 left won, 1 for right won
		# moves: 1 = up, 0 = still, -1 = down
		# if self.ball_x < 0 or self.ball_x+self.ball_size > self.width:
		# 	self.ball_vx *= -1
		if self.ball_y < 0 or self.ball_y+self.ball_size > self.height:
			self.ball_vy *= -1

		if self.ball_x < self.padding+self.playerSize[0]:
			if self.playerLeft < self.ball_y+self.ball_size/2 and self.playerLeft+self.playerSize[1] > self.ball_y-(self.ball_size/2):
				self.ball_x = self.playerSize[0]+self.padding
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
				return 1

		self.ball_x += self.ball_vx
		self.ball_y += self.ball_vy

		if moveLeft == 1 and self.playerLeft > 0:
			self.playerLeft -= self.playerSpeed
		elif moveLeft == -1 and self.playerLeft+self.playerSize[1] < self.height:
			self.playerLeft += self.playerSpeed

		if(self.playerLeft < 0):
			self.playerLeft = 0
		elif(self.playerLeft+self.playerSize[1] > self.height):
			self.playerLeft = self.height - self.playerSize[1]

		return 0

