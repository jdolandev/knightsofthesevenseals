import random
from enemy import *

class Battle:
	"""docstring for battle"""
	def __init__(self):
		probability = random.randint(0,100)
		if (location = "Field"):
			if (probability <= 40):
				self.enemy = "Slime"
				slime = Enemy("Slime","A slimy creature",20,10)
			elif ((probability > 40) and (probability <= 50)):
				self.enemy = "Theif"
				thief = Enemy("Thief","A cunning trickster",30,15)
			elif ((probability > 50) and (probability <= 55)):
				self.enemy = "Mimic"
				mimic = Enemy("Mimic","Mistook for a treasure chest",15,40)
		print(self.enemy)
		yourTurn = True
	def phases(self):
		if not yourTurn:
			self.enemy.attack()
			yourTurn = True
