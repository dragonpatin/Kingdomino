class Tile :
	def __init__(self, numero, tuile_1, couronne_1, tuile_2, couronne_2):
		self.numero = numero
		self.tuile_1 = tuile_1
		self.couronne_1 = couronne_1
		self.tuile_2 = tuile_2
		self.couronne_2 = couronne_2
		self.position_x = 0
		self.position_y = 0
		self.orientation = 0
		
	def setPosistion(self,x,y):
		self.position_x = x
		self.position_y = y
		
	def setOrientation(self,o):
		self.orientation = o
		
	def left(self):
		if(self.position_x != 0):
			self.position_x -= 1
			
	def right(self):
		if(self.position_x != 4):
			self.position_x += 1	

	def up(self):
		if(self.position_y != 0):
			self.position_y -= 1
			
	def down(self):
		if(self.position_y != 4):
			self.position_y += 1

	def orient(self):
		self.orientation = (self.orientation + 1)%4
		