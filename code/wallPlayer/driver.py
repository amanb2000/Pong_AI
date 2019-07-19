import numpy as np
import pygame, sys
import pong
import agent
import random

GENERATION_SIZE = 1000
agnts = []

for i in range(GENERATION_SIZE):
	agnts+=[agent.Agent(False)]

DISP = pygame.display.set_mode((800, 800))



def draw(game_, DISP_):
	DISP_.fill((10, 10, 20))
	pygame.draw.rect(DISP_, (200, 200, 255), (0, 600, 800, 200))

	pygame.draw.rect(DISP_, (255, 255, 255), (game_.ball_x, game_.ball_y, game_.ball_size, game_.ball_size))
	pygame.draw.rect(DISP_, (255, 255, 200), (game_.padding, game_.playerLeft, game_.playerSize[0], game_.playerSize[1]))
	pygame.draw.rect(DISP_, (255, 255, 200), (game_.width-game_.playerSize[0]-game_.padding, 0, game_.playerSize[0], game_.height))


# returns -1 if p1 wins, 1 if p2 wins
def fitness(p1): # p1 and p2 are both agents
	res = 0

	cnt = 0

	run = True
	game = pong.PongGame()
	while run:
		cnt += 1
		# move_num_left = np.argmax(np.dot(agnts[0].params, game.getState(0)))-1
		move_num_left = p1.get_move(game.getState(-1))

		res = game.transition(move_num_left)

		run = (res == 0)

		if(cnt > 10000):
			# print('reached 10000')
			break


	return cnt

def show_game(p1): # p1 and p2 are both agents
	pygame.init()
	DISP = pygame.display.set_mode((800, 800))
	pygame.display.set_caption('PONG!')

	game = pong.PongGame()

	run = True

	res = True

	move_num = 0
	while run:
		draw(game, DISP)

		# move_num_left = np.argmax(np.dot(agnts[0].params, game.getState(0)))-1
		move_num_left = p1.get_move(game.getState(-1))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False



		res = game.transition(move_num_left)

		run = (res == 0)
		pygame.display.update()



	pygame.quit()
	# sys.exit()


cnt = 0
while True:
	results = []
	avgResult = 0

	for i in range(len(agnts)):
		result = fitness(agnts[i])
		result += fitness(agnts[i])
		result += fitness(agnts[i])
		avgResult += result
		results+=[result]

	avgResult += 0.01
	avgResult /= len(agnts)

	maxFitness = max(results)

	if(cnt % 10 == 0):
		print('Generation: ',cnt)
		print('AvgFitness: ',avgResult)
		print('Max fitness: ', maxFitness)

	if(cnt % 50 == 0):
		max_agent_ind = results.index(max(results))
		show_game(agnts[max_agent_ind])
	

	while len(agnts) > GENERATION_SIZE/2:
		i = 0
		while i < len(agnts)-1:
			if results[i] < avgResult:
				agnts.pop(i)
				results.pop(i)
				i -= 1
			i += 1
		avgResult += 1


	ind = 0
	while len(agnts) < GENERATION_SIZE:
		agnts += [agent.Agent(agnts[ind])]
		ind += 1


	random.shuffle(agnts)

	# result = compete(agnts[0], agnts[1])

	# if result < 0: # p1 won
	# 	agnts[1] = agent.Agent(agnts[0])
	# elif result > 0:
	# 	agnts[0] = agent.Agent(agnts[1])
	# else:
	# 	print('they tied!?')
	# 	show_game(agnts[0], agnts[1])

	cnt += 1

	
