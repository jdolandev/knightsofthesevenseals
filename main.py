import random
import os
import time
from item import *
from enemy import *
from battle import *
from location import *

logo = ["",
		"		   |^^^|        __         _       __    __      ",
		"		    }_{        / /______  (_)___ _/ /_  / /______",
		"		    }_{       / //_/ __ \/ / __ `/ __ \/ __/ ___/",
		"		/|_/---\_|\  / ,< / / / / / /_/ / / / / /_(__  ) ",
		"		I _|\_/|_ I /_/|_/_/ /_/_/\__, /_/ /_/\__/____/	",
		"		\| |   | |/  ____  / __/  / /_/ /_  ___   		",
		"		   |   |    / __ \/ /_   / __/ __ \/ _ \ 		",
		"		   |   |   / /_/ / __/  / /_/ / / /  __/  		",
		"		   |   |   \__________ _\________/____/ 		",
		"		   |   |    / ___/ _ \ | / / _ \/ __ \  		",
		"		   |   |   (__  )  __/ |/ /  __/ / / /			",
		"		   |   |  /____/\___/|___/\___/// /_/			",
		"		   |   |     ________  ____ _/ /____  			",
		"		   |   |    / ___/ _ \/ __ `/ / ___/			",
		"		   |   |   (__  )  __/ /_/ / (__  )				",
		"		   |   |  /____/\___/\__,_/_/____/ 				",
		"		   |   |      									",
		"		   |   |  \033[93m---Created by Joe Dolan---\033[0m	",
		"		   \   /										",
		"		    \ /											",
		"		     Y                                         	"]

dead = False
curLoc = "Town"
_map = ["Town","Field","Cave","Mountain","Swamp"]
inventory = []

"""
Location details
"""
town = Location()
town.name = "Town"
town.description = "A quiet toww"
town.options = ["Pub","Shop","Inn","Blacksmith","Travel"]

def clr():
	if os.name == 'nt':
		os.system("cls")
	else:
		os.system("clear")
def pause():
	throwaway = raw_input("Press any key to continue...")
	del(throwaway)

"""Very similar to D&D, you roll the dice and hope for the best"""
def rollDice(difficulty):
	diceRoll = random.randint(1,20)
	if diceRoll > difficulty:
		return True #You were successful
	else:
		return False #You failed

def _options():
	for i in xrange(0,len(options)):
		print(options[i])

def travel(location):
	if(rollDice(15) == True):
		print("You successfully traveled to: ", location)
		curLoc = location
	else:
		battle()

def main():
	while (dead == False):
		whatDo = raw_input("What should you do?: ")
		if(whatDo.lower() == "travel"):
			whereTo = raw_input("Where do you wish to travel to?: ")
			if any(whatDo in s for s in _map):
				travel()
			else:
				print("That location does not exist.")
		elif(whatDo.lower() == "options"):
			if(curLoc == "Town"):
				for i in xrange(0,len(town.options)):
					print(town.options[i])
		elif((whatDo.lower() == "exit") or (whatDo.lower == "quit")):
			really = raw_input("Are you sure you want to exit? [y/n]: ")
			if really.lower() == "y":
				exit()
			else:
				print "Okay, cool."
				main()
		else:
			print "I don't know how to", whatDo

def init():
	clr()
	for i in xrange(0,len(logo)):
		print(logo[i])
		time.sleep(0.25)
	pause()
	clr()
	print("You wake up in a town, ")
	main()
init()
