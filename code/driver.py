import numpy as np
import pygame, sys
import pong
import agent

agnts = [agent.Agent(), agent.Agent()]

# print(agnts[0].params)


def draw(game_):
	print('Player One: ',np.dot(agnts[0].params, game_.getState(0)))
	print('Player Two: ',np.dot(agnts[1].params, game_.getState(0)))
	DISP.fill((10, 10, 20))
	pygame.draw.rect(DISP, (200, 200, 255), (0, 600, 800, 200))

	pygame.draw.rect(DISP, (255, 255, 255), (game_.ball_x, game_.ball_y, game_.ball_size, game_.ball_size))
	pygame.draw.rect(DISP, (255, 255, 200), (game_.padding, game_.playerLeft, game_.playerSize[0], game_.playerSize[1]))
	pygame.draw.rect(DISP, (255, 255, 200), (game_.width-game_.playerSize[0]-game_.padding, game_.playerRight, game_.playerSize[0], game_.playerSize[1]))

def show_game(p1, p2): #p1 and p2 are both agents
	pygame.init()

	DISP = pygame.display.set_mode((800, 800))
	pygame.display.set_caption('PONG!')

	game = pong.PongGame()

	run = True

	res = True

	move_num = 0
	while run:
		draw(game)

		# move_num_left = np.argmax(np.dot(agnts[0].params, game.getState(0)))-1
		move_num_left = p1.get_move(game.getState(0))
		move_num_right = p2.get_move(game.getState(1))
		print('Left player: ',  move_num_left)
		print('Right player: ',  move_num_right)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False



		res = game.transition(move_num_left, move_num_right)

		run = (res == 0)
		pygame.display.update()



	pygame.quit()
	sys.exit()


show_game(agnts[0], agnts[1])
