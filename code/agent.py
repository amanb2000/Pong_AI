import numpy as np
import math
import pygame

class Agent:
	def __init__(self):
		self.params = np.random.rand(3, 6)
		with np.nditer(self.params, op_flags=['readwrite']) as it:
			for x in it:
				x -= 0.5

		print(self.params)

	def get_move(self, game_state):
		return(np.argmax(np.dot(self.params, game_state)-1))