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
				
	def testSuperpositionChateau(self):
		if(self.lastTile.position_x == self.castle_x and self.lastTile.position_y == self.castle_y) :
			return True
		if(self.lastTile.getPos2x() == self.castle_x and self.lastTile.getPos2y() == self.castle_y) :
			return True
		return False
	def testSuperpositionList(self):
		for T in self.list_tuile :
			if(self.lastTile.position_x == T.position_x and self.lastTile.position_y == T.position_y) :
				return True
			if(self.lastTile.getPos2x() == T.position_x and self.lastTile.getPos2y() == T.position_y) :
				return True
			if(self.lastTile.position_x == T.getPos2x() and self.lastTile.position_y == T.getPos2y()) :
				return True
			if(self.lastTile.getPos2x() == T.getPos2x() and self.lastTile.getPos2y() == T.getPos2y()) :
				return True
		return False
	def testSuperposition(self):
		if(self.testSuperpositionChateau() or self.testSuperpositionList()):
			return True
		return False
		
	def isNotNextCastle(self) :
		if(self.lastTile.position_x + 1 == self.castle_x and self.lastTile.position_y == self.castle_y) :
			return False
		if(self.lastTile.position_x - 1 == self.castle_x and self.lastTile.position_y == self.castle_y) :
			return False
		if(self.lastTile.position_x == self.castle_x and self.lastTile.position_y + 1 == self.castle_y) :
			return False
		if(self.lastTile.position_x == self.castle_x and self.lastTile.position_y - 1 == self.castle_y) :
			return False
		if(self.lastTile.getPos2x() + 1 == self.castle_x and self.lastTile.getPos2y() == self.castle_y) :
			return False
		if(self.lastTile.getPos2x() - 1 == self.castle_x and self.lastTile.getPos2y() == self.castle_y) :
			return False
		if(self.lastTile.getPos2x() == self.castle_x and self.lastTile.getPos2y() - 1 == self.castle_y) :
			return False
		if(self.lastTile.getPos2x() == self.castle_x and self.lastTile.getPos2y() + 1 == self.castle_y) :
			return False
		return True
		
	def isNextGoodTile(self):
		for T in self.list_tuile :
			if T.tuile_1 == self.lastTile.tuile_1 :
				if(self.lastTile.position_x + 1 == T.position_x and self.lastTile.position_y == T.position_y) :
					return True
				if(self.lastTile.position_x - 1 == T.position_x and self.lastTile.position_y == T.position_y) :
					return True
				if(self.lastTile.position_x == T.position_x and self.lastTile.position_y + 1 == T.position_y) :
					return True
				if(self.lastTile.position_x == T.position_x and self.lastTile.position_y - 1 == T.position_y) :
					return True
			if T.tuile_1 == self.lastTile.tuile_2 :
				if(self.lastTile.getPos2x() + 1 == T.position_x and self.lastTile.getPos2y() == T.position_y) :
					return True
				if(self.lastTile.getPos2x() - 1 == T.position_x and self.lastTile.getPos2y() == T.position_y) :
					return True
				if(self.lastTile.getPos2x() == T.position_x and self.lastTile.getPos2y() - 1 == T.position_y) :
					return True
				if(self.lastTile.getPos2x() == T.position_x and self.lastTile.getPos2y() + 1 == T.position_y) :
					return True
			if T.tuile_2 == self.lastTile.tuile_1 :
				if(self.lastTile.position_x + 1 == T.getPos2x() and self.lastTile.position_y == T.getPos2y()) :
					return True
				if(self.lastTile.position_x - 1 == T.getPos2x() and self.lastTile.position_y == T.getPos2y()) :
					return True
				if(self.lastTile.position_x == T.getPos2x() and self.lastTile.position_y + 1 == T.getPos2y()) :
					return True
				if(self.lastTile.position_x == T.getPos2x() and self.lastTile.position_y - 1 == T.getPos2y()) :
					return True
			if T.tuile_2 == self.lastTile.tuile_2 :
				if(self.lastTile.getPos2x() + 1 == T.getPos2x() and self.lastTile.getPos2y() == T.getPos2y()) :
					return True
				if(self.lastTile.getPos2x() - 1 == T.getPos2x() and self.lastTile.getPos2y() == T.getPos2y()) :
					return True
				if(self.lastTile.getPos2x() == T.getPos2x() and self.lastTile.getPos2y() - 1 == T.getPos2y()) :
					return True
				if(self.lastTile.getPos2x() == T.getPos2x() and self.lastTile.getPos2y() + 1 == T.getPos2y()) :
					return True
		return False
	
	def autorisationSauveguarde(self):
		if self.testSuperposition() :
			return False
		if self.isNotNextCastle() :
			if not(self.isNextGoodTile()) :
				return False
		return True
		
	def tileOrientation(self):
		self.lastTile.orient()
		
		