import random
import os
import time
from item import *
from enemy import *
from battle import *

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
curLoc = ""
_map = ["Town","Field","Cave","Mountain","Swamp",]

slime = Enemy("slime","a slimy creature",20,10)
slime.image = """
        /\\
      /    \\      
    /        \\
  /            \\
/                \\
|   (0)     (0)   |
|       |  |      |
\       \  /      /
 \   __________  /
  \_____________/
"""
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
		battle = Battle()

def init():
	clr()
	for i in xrange(0,len(logo)):
		print(logo[i])
		time.sleep(0.25)
	pause()
	clr()
	main()
init()
