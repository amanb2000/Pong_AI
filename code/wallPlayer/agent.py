import numpy as np
import math
import random
import pygame

alpha = 0.1

class Agent:
	def __init__(self, params_in):
		if(params_in == False):
			self.params = np.random.rand(3, 6)
			with np.nditer(self.params, op_flags=['readwrite']) as it:
				for x in it:
					x -= 0.5
			return

		self.params = np.array(params_in.params)
		with np.nditer(self.params, op_flags=['readwrite']) as it:
			for x in it:
				x -= random.random()*alpha


	def get_move(self, game_state):
		return(np.argmax(np.dot(self.params, game_state)-1))