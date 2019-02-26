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
		if(not(self.position_x == 0 or self.getPos2x() == 0)):
			self.position_x -= 1
			
	def right(self):
		if(not(self.position_x == 4 or self.getPos2x() == 4)):
			self.position_x += 1	

	def up(self):
		if(not(self.position_y == 0 or self.getPos2y() == 0)):
			self.position_y -= 1
			
	def down(self):
		if(not(self.position_y == 4 or self.getPos2y() == 4)):
			self.position_y += 1
			
	def getPos2y(self):
		if(self.orientation == 0 or self.orientation == 2):
			return self.position_y
		elif(self.orientation == 1):
			return self.position_y + 1
		else :
			return self.position_y - 1
			
	def getPos2x(self):
		if(self.orientation == 1 or self.orientation == 3):
			return self.position_x
		elif(self.orientation == 2):
			return self.position_x - 1
		else :
			return self.position_x +1

	def orient(self):
		if(not(self.orientation == 0 and self.position_y == 4) and not(self.orientation == 1 and self.position_x == 0) 
		and not(self.orientation == 2 and self.position_y == 0) and not(self.orientation == 3 and self.position_x == 4)):
			self.orientation = (self.orientation + 1)%4
		