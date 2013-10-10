import random

print("Welcome to the quest game, the best text game ever!")
hero= input("What is your name?: ")
inventory=[]
dead= False
location = "town"

#Equipment
iHead = None
iArmR = None
iArmL = None
iChest = None
iLegs = None
iShoes = None

def death():
	print("You are dead.")
	print("Game over")

#Like DnD, very simple 
def rolldice(difficulty):
	print("You roll the dice...")
	roll = random.randint(1,20)
	print("You roll:",roll)
	if(roll > difficulty):
		pass
	else:
		print("You travel safely.")
	
#The choices for going to town
def travel():
	options = ["Town","Cave","Forest","Mountains"]
	print("Code\tLocation\n")
	for i in range(0,len(options)):
		print(i,"\t"+options[i])
	print("\n")
	whereto = input("Where do you wish to travel?: ")
	if((whereto.lower() == "town") or (whereto == "0")):
		location = "town"
	elif(whereto.lower() == "cave"):
		location = "cave"
	elif(whereto.lower() == "forest"):
		location = "forest"
	elif(whereto.lower() == "mountains"):
		location = "mountains"
		print("You travel to the mountains...")
		rolldice(12)
	else:
		print("I don't understand")
		mainloop()
	
def mainloop():
	whatDo = input("What should you do?: ")
	if(whatDo.lower() == "travel"):
		clear()
		travel()
	else:
		print("I don't understand")
		mainloop()

def clear():
	import os
	clear = lambda: os.system('cls')
	clear()

def init():
	clear()
	print("Hello",hero + "!","you are the chosen one who will save the world!")
	mainloop()

init()
