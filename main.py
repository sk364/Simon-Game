import pygame
import sys
import random
from pygame.locals import *

pygame.init()

# screen of size 400 by 400
screen = pygame.display.set_mode((400, 400))

# function to get the square number
# if no square is clicked, 0 is returned
def get_square(x,y):
        if x >= 50 and x < 200:
		if y >= 50 and y <= 200:
			return 1
		elif y > 200 and y <= 350:
			return 3
	elif x >= 200 and x <= 350:
		if y >= 50 and y <= 200:
                        return 2
                elif y > 200 and y <= 350:
                        return 4
	return 0


def draw_board(size,x):
	# TODO: display current score 

	BLACK = (0,0,0)
	BLUE = (0,0,200)
	GREEN = (0,200,0)
	RED = (200,0,0)
	YELLOW = (200,200,0)

	blue_x, blue_y = 50,50
	red_x, red_y = 50,200
	green_x, green_y = 200,50
	yellow_x, yellow_y = 200,200

	screen.fill(BLACK)

	# Numbers 1,2,3,4 displays one square color at a time
	# Number 5 displays all square colors for the user

	if x==1:
		pygame.draw.rect(screen, BLUE, ((blue_x,blue_y), (150,150)))
	if x==2:
		pygame.draw.rect(screen, GREEN, ((green_x,green_y), (150,150)))
	if x==3:
		pygame.draw.rect(screen, RED, ((red_x,red_y), (150,150)))
	if x==4:
		pygame.draw.rect(screen, YELLOW, ((yellow_x,yellow_y), (150,150)))
	if x==5:
		pygame.draw.rect(screen, BLUE, ((blue_x,blue_y), (150,150)))
		pygame.draw.rect(screen, GREEN, ((green_x,green_y), (150,150)))
		pygame.draw.rect(screen, RED, ((red_x,red_y), (150,150)))
		pygame.draw.rect(screen, YELLOW, ((yellow_x,yellow_y), (150,150)))

	
	pygame.display.update()



# display of messages on the screen

def display(msg):
	font = pygame.font.SysFont(None, 72)

	label = font.render(msg, 1, (255,255,255))

	p_x = (screen.get_rect().width)/2 - (label.get_rect().width)/2
	p_y = (screen.get_rect().width)/2 - (label.get_rect().height)/2

	screen.blit(label, (p_x,p_y))

	pygame.display.flip()	

	pygame.time.wait(1000)



# main loop

def play_game():
	y=1
	x=1
	state = []					# stores game state - square colors appearing one at a time
	switched = False				# to check if the level has changed
	clicks = -1					# counting the number of clicks by the user if in the square box
	level = 1
	diff = [3, 5, 8, 10, 12]			# difficulty based on number of squares
	speed = 1000					# initial speed - decreases by 20ms each level
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos_x, pos_y = pygame.mouse.get_pos()

				square = get_square(pos_x,pos_y)
				
				if square!=0:
					clicks = clicks+1

					if square != state[clicks]:
						display("GAME OVER!")
						pygame.quit()
						sys.exit()			# quits when GameOver

					if clicks==diff[level-1]-1:
						display("SUCCESS!")

						level = level + 1		# updating level and speed

						speed = speed - 20

						del state[:]			# resetting all variables - state, clicks, switched

						clicks = -1

                                                switched = False


		if not switched:
			draw_board(400,5)
			
			display("Level "+str(level))

			for i in range(diff[level-1]):
				while(y==x):				# avoiding equal numbers generating one after another
					x = random.randint(1,4)	

				draw_board(400, x)

				y = x

				state = state + [x]			# storing states

				pygame.time.wait(speed)			

			switched = True
		else:
			
			draw_board(400,5)
			


if __name__== "__main__":
	play_game()

	sys.exit()
