import random
from enemy import *

class Battle:
	def __init__(self, location):
		probability = random.randint(0,100)
		self.enemy = None
		if (location.lower() == "field"):
			if (probability <= 40):
				self.enemy = "Slime"
				slime = Enemy("Slime","A slimy creature",20,10)
			elif ((probability > 40) and (probability <= 50)):
				self.enemy = "Thief"
				thief = Enemy("Thief","A cunning trickster",30,15)
			else:
				self.enemy = "Mimic"
				mimic = Enemy("Mimic","Mistook for a treasure chest",15,40)
