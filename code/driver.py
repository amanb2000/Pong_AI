import numpy as np
import pygame, sys
import pong

pygame.init()

DISP = pygame.display.set_mode((800, 800))
pygame.display.set_caption('PONG!')

game = pong.PongGame()

def draw(game_):
	DISP.fill((10, 10, 20))
	pygame.draw.rect(DISP, (255, 255, 255), (game_.ball_x, game_.ball_y, game_.ball_size, game_.ball_size))
	pygame.draw.rect(DISP, (255, 255, 200), (game_.padding, game_.playerLeft, game_.playerSize[0], game_.playerSize[1]))
	pygame.draw.rect(DISP, (255, 255, 200), (game_.width-game_.playerSize[0]-game_.padding, game_.playerLeft, game_.playerSize[0], game_.playerSize[1]))

run = True

move_num = 0;

while run:
	draw(game)



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				move_num = 1

			if event.key == pygame.K_DOWN:
				move_num = -1

	game.transition(move_num, move_num)
	pygame.display.update()



pygame.quit()
sys.exit()
