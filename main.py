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
_map = ["town","field","cave","mountain","Swamp"]
inventory = []
defaultops = ["Inventory","Map","Stats",""]

hp = 100

isBattling = False
"""
Location details
"""
town = Location()
town.name = "Town"
town.description = "A quiet toww"
town.options = ["Pub","Shop","Inn","Blacksmith"]

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

def battleloop(enemy):
	battleChoices = ["Attack","Defend","Equip","Run"]
	print "Oh no, you've been attacked by a", enemy
	while(isBattling == True):
		battlePlan = raw_input("What should you do?: ")
		if(battlePlan.lower == "stats"):
			print "Enemy HP:", enemy.hp
		elif((battlePlan.lower() == "exit") or (battlePlan.lower() == "quit")):
			really = raw_input("Are you sure you want to exit? [y/n]: ")
			if really.lower() == "y":
				exit()
		elif((battlePlan.lower() == "options") or (battlePlan.lower() == "help")):
			print("OPTIONS:")
			for i in xrange(0,len(battleChoices)):
				print battleChoices[i]

def travel(location):
	print "You venture off to", location
	success = rollDice(10)
	if(success == True):
		print"You successfully traveled to: ", location
		curLoc = location
	else:
		battle = Battle(location)
		isBattling = True
		battleloop(battle.enemy)

def main():
	while (dead == False):
		whatDo = raw_input("What should you do?: ")
		if(whatDo.lower() == "travel"):
			whereTo = raw_input("Where do you wish to travel to?: ")
			if(whereTo.lower() == "town"):
				travel("Town")
			elif(whereTo.lower() == "field"):
				travel("Field")
			elif((whereTo.lower() == "options") or (whereTo.lower() == "help")):
				print("Locations:")
				for i in xrange(0,len(_map)):
					print _map[i]
			elif(whereTo.lower() == curLoc):
				print("You're already at that location.")
			else:
				print("That location does not exist.")

		elif((whatDo.lower() == "options") or (whatDo.lower() == "help")):
			clr()
			print("\n\t\t\033[91mOptions:\033[0m")
			if(curLoc == "Town"):
				for i in xrange(0,len(town.options)):
					print("\033[93m" + town.options[i])
				print "\033[0m"
				for i in xrange(0,len(defaultops)):
					print("\033[92m" + defaultops[i])
				print "\033[0m"

		elif(whatDo.lower() == "map"):
			clr()
			town.gmap()

		elif(whatDo.lower() == "inventory"):
			if (len(inventory) > 0):
				for i in xrange(0,len(inventory)):
					print(inventory[i])
			else:
				print "\033[91mYou have no items.\033[0m"

		elif(whatDo.lower() == "stats"):
			print "HP:\t",hp
		elif((whatDo.lower() == "exit") or (whatDo.lower() == "quit")):
			really = raw_input("Are you sure you want to exit? [y/n]: ")
			if really.lower() == "y":
				exit()
			else:
				print "Okay, cool."
				main()
		elif(whatDo.lower() == ""):
			print "Type something next time."
		else:
			print "I don't know how to", "'" + whatDo + "'"

def init():
	clr()
	for i in xrange(0,len(logo)):
		print(logo[i])
		time.sleep(0.1)
	pause()
	clr()
	print("You wake up in a town, ")
	main()
init()
