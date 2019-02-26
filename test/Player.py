class Player:
	def __init__(self, nom):
		self.nom = nom
		self.nbpoint = 0
		self.list_tuile = list()
		self.castle_x = 0
		self.castle_y = 0
		self.lastTile = None

	def setLastTile(self,T):
		self.lastTile = T
		
	def tileLeft(self):
		self.lastTile.left()
		
	def tileRight(self):
		self.lastTile.right()
		
	def tileDown(self):
		self.lastTile.down()
		
	def tileUp(self):
		self.lastTile.up()
		
	def autorisationDeplacementPlateauLeft(self):
		if(self.castle_x == 0):
			return False
		for T in self.list_tuile :
			if(T.position_x == 0 or T.getPos2x() == 0):
				return False
		return True
		
	def autorisationDeplacementPlateauRight(self):
		if(self.castle_x == 4):
			return False
		for T in self.list_tuile :
			if(T.position_x == 4 or T.getPos2x() == 4):
				return False
		return True
		
	def autorisationDeplacementPlateauUp(self):
		if(self.castle_y == 0):
			return False
		for T in self.list_tuile :
			if(T.position_y == 0 or T.getPos2y() == 0):
				return False
		return True

	def autorisationDeplacementPlateauDown(self):
		if(self.castle_y == 4):
			return False
		for T in self.list_tuile :
			if(T.position_y == 4 or T.getPos2y() == 4):
				return False
		return True
		
	def plateauLeft(self):
		if(self.autorisationDeplacementPlateauLeft()):
			self.castle_x -= 1
			for T in self.list_tuile :
				T.left()
				
	def plateauRight(self):
		if(self.autorisationDeplacementPlateauRight()):
			self.castle_x += 1
			for T in self.list_tuile :
				T.right()
				
	def plateauDown(self):
		if(self.autorisationDeplacementPlateauDown()):
			self.castle_y += 1
			for T in self.list_tuile :
				T.down()
				
	def plateauUp(self):
		if(self.autorisationDeplacementPlateauUp()):
			self.castle_y -= 1
			for T in self.list_tuile :
				T.up()
	
	def tileOrientation(self):
		self.lastTile.orient()
		
		