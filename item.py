class item():
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.equipped = False
		self.location = None
		self.image = None
	def description(self):
		print(description)
	def equip(self):
		whereTo = input("Where do you want to equip it to?: ")
		self.equipped = True
		self.location = whereTo
