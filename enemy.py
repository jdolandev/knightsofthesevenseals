import random

class Enemy:
	_enemies = ["Slime","Theif","Mimic","Enraged Slime","Green Dragon"]
	def __init__(self, name, description, hp, maxAtk, probability):
		self.name = name
		self.description = description
		self.hp = hp
		self.maxAtk = maxAtk
	def attack(self):
		print("The",name,"attacks...")
		if(random.randint(0,20) > 5):
			damage = random.randint(0, maxAtk)
			if (damage == maxAtk):
				print """
				\033[93m _______ _                       _    _ 
				|__   __| |                     | |  | |
				   | |  | |____      ____ _  ___| | _| |
				   | |  | '_ \ \ /\ / / _` |/ __| |/ / |
				   | |  | | | \ V  V / (_| | (__|   <|_|
				   |_|  |_| |_|\_/\_/ \__,_|\___|_|\_(_)\033[0m
				"""
			print("It hits with", damage, "damage!")
		else:
			print("The",name,"Misses.")

slime = Enemy("slime","A slimy creature.", 20,10)
