import numpy as np
import pygame, sys
import pong
import agent
import random

GENERATION_SIZE = 100
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
def get_winner(p1): # p1 and p2 are both agents
	run = True
	game = pong.PongGame()

	res = 0

	cnt = 0

	while run:
		cnt += 1
		# move_num_left = np.argmax(np.dot(agnts[0].params, game.getState(0)))-1
		move_num_left = p1.get_move(game.getState(-1))

		res = game.transition(move_num_left)

		run = (res == 0)

		if(cnt > 1000):
			break

	if cnt > 35:
		print('We exceeded 35 with',cnt)

	return res

def show_game(p1, p2): # p1 and p2 are both agents
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
		move_num_right = p2.get_move(game.getState(1))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False



		res = game.transition(move_num_left, move_num_right)

		run = (res == 0)
		pygame.display.update()



	pygame.quit()
	# sys.exit()

def compete(p1, p2): # return -1 for p1, 1 for p2
	winner = get_winner(p1, p2) # -1 if p1 wins, 1 if p2 wins
	# winner -= get_winner(p2, p1)
	# winner += get_winner(p1, p2)
	# winner -= get_winner(p2, p1)

	if winner < 0:
		return -1
	elif winner > 0:
		return 1
	return 0


cnt = 0
while True:
	if(cnt % 100 == 0):
		print('Generation ',cnt)
	if(cnt % 1000 == 0):
		show_game(agnts[0], agnts[1])



	for i in range(0, len(agnts)-2, 2):
		result = compete(agnts[i], agnts[i+1])
		if result < 0:
			agnts[i+1] = agent.Agent(agnts[i])
		else:
			agnts[i] = agent.Agent(agnts[i+1])

	# random.shuffle(agnts)

	for i in range(20):
		agnts[i] = agent.Agent(False)


	# result = compete(agnts[0], agnts[1])

	# if result < 0: # p1 won
	# 	agnts[1] = agent.Agent(agnts[0])
	# elif result > 0:
	# 	agnts[0] = agent.Agent(agnts[1])
	# else:
	# 	print('they tied!?')
	# 	show_game(agnts[0], agnts[1])

	cnt += 1

	
