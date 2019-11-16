#import the randop package so that we can generate a random choice
from random import randint
from gameFunctions import winlose
from gameFunctions import gameVars
from gameFunctions import compare

# define a function that takes an argument


while gameVars.player is False:
	#say player to true
	print("*********************************\n")
	print("player lives: ", gameVars.player_lives, "/",gameVars.total_lives,"\n")
	print("computer lives: ", gameVars.computer_lives, "/",gameVars.total_lives,"\n")
	print("choose your weapon!\n")
	print("*********************************\n")
	
	gameVars.player = input("choose rock, paper or scissors\n")

	print("computer chose ", gameVars.computer, "\n")
	print("player choose ", gameVars.player, "\n")
	# handle all lives lost for gameVars.player or AI
	compare.compareChoices(gameVars.computer,gameVars.player) 

	if gameVars.player_lives is 0:
		winlose.winorlose("lost")
			

	elif gameVars.computer_lives is 0:
		winlose.winorlose("win")

	else:
		# need to check all of our conditions after checking for a tie
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]