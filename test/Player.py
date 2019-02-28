class Player:
	def __init__(self, nom):
		self.nom = nom
		self.nbpoint = 0
		self.list_tuile = list()
		self.castle_x = 0
		self.castle_y = 0
		self.lastTile = None
		self.tabPoint = None

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
			self.resetTabPoint()
			for T in self.list_tuile :
				T.left()
				self.constructionTabPoint(T)
				self.comptagePoint()
				
	def plateauRight(self):
		if(self.autorisationDeplacementPlateauRight()):
			self.castle_x += 1
			self.resetTabPoint()
			for T in self.list_tuile :
				T.right()
				self.constructionTabPoint(T)
				self.comptagePoint()
				
	def plateauDown(self):
		if(self.autorisationDeplacementPlateauDown()):
			self.castle_y += 1
			self.resetTabPoint()
			for T in self.list_tuile :
				T.down()
				self.constructionTabPoint(T)
				self.comptagePoint()
				
	def plateauUp(self):
		if(self.autorisationDeplacementPlateauUp()):
			self.castle_y -= 1
			self.resetTabPoint()
			for T in self.list_tuile :
				T.up()
				self.constructionTabPoint(T)
				self.comptagePoint()
				
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

	def initTabPoint(self):
                n = 5
                m = 3
                self.tabPoint = [[[0 for k in xrange(m)] for j in xrange(n)] for i in xrange(n)]
                self.tabPoint[0][0][0] = 7
                
        def resetTabPoint(self):
                for i in range (0,5):
                        for j in range (0,5):
                                for k in range (0,3):
                                        self.tabPoint[i][j][k] = 0

        def ajoutTileTabPoint(self):
                self.tabPoint[self.lastTile.position_y][self.lastTile.position_x][0] = self.lastTile.tuile_1
                self.tabPoint[self.lastTile.position_y][self.lastTile.position_x][1] = self.lastTile.couronne_1
                
                self.tabPoint[self.lastTile.getPos2y()][self.lastTile.getPos2x()][0] = self.lastTile.tuile_2
                self.tabPoint[self.lastTile.getPos2y()][self.lastTile.getPos2x()][1] = self.lastTile.couronne_2

        def constructionTabPoint(self,T):
                self.tabPoint[T.position_y][T.position_x][0] = T.tuile_1
                self.tabPoint[T.position_y][T.position_x][1] = T.couronne_1
                
                self.tabPoint[T.getPos2y()][T.getPos2x()][0] = T.tuile_2
                self.tabPoint[T.getPos2y()][T.getPos2x()][1] = T.couronne_2

                self.tabPoint[self.castle_y][self.castle_x][0] = 7 

        def nbVoisins(self,y,x,c):
                global nb_couronne, nb_voisins
                nb_couronne = c
                nb_voisins = 0
                self.tabPoint[y][x][2] = 1
                if y - 1 >= 0 and self.tabPoint[y - 1][x][2] == 0 and self.tabPoint[y - 1][x][0] == self.tabPoint[y][x][0]:
                        if self.tabPoint[y - 1][x][1] != 0:
                                nb_couronne = nb_couronne + self.tabPoint[y - 1][x][1]
                                nb_voisins = nb_voisins + self.nbVoisins(y-1,x,nb_couronne)
                        else:
                                nb_voisins = nb_voisins + self.nbVoisins(y-1,x,nb_couronne)
                                
                if x + 1 <= 4 and self.tabPoint[y][x + 1][2] == 0 and self.tabPoint[y][x + 1][0] == self.tabPoint[y][x][0]:
                        if self.tabPoint[y][x + 1][1] != 0:
                                nb_couronne = nb_couronne + self.tabPoint[y][x + 1][1]
                                nb_voisins = nb_voisins + self.nbVoisins(y,x+1,nb_couronne)
                        else:
                                nb_voisins = nb_voisins + self.nbVoisins(y,x+1,nb_couronne)
                                
                if y + 1 <= 4 and self.tabPoint[y + 1][x][2] == 0 and self.tabPoint[y + 1][x][0] == self.tabPoint[y][x][0]:
                        if self.tabPoint[y + 1][x][1] != 0:
                                nb_couronne = nb_couronne + self.tabPoint[y + 1][x][1]
                                nb_voisins = nb_voisins + self.nbVoisins(y+1,x,nb_couronne)
                        else:
                                nb_voisins = nb_voisins + self.nbVoisins(y+1,x,nb_couronne)
                        
                if x - 1 >= 0 and self.tabPoint[y][x - 1][2] == 0 and self.tabPoint[y][x - 1][0] == self.tabPoint[y][x][0]:
                        if self.tabPoint[y][x - 1][1] != 0:
                                nb_couronne = nb_couronne + self.tabPoint[y][x - 1][1]
                                nb_voisins = nb_voisins + self.nbVoisins(y,x-1,nb_couronne)
                        else:
                                nb_voisins = nb_voisins + self.nbVoisins(y,x-1,nb_couronne)
                        
                return 1 + nb_voisins
                
        def comptagePoint(self):
                global nb_couronne
                self.nbpoint = 0
                for i in range(0,5):
                        for j in range(0,5):
                                if self.tabPoint[i][j][2] == 0:
                                        if self.tabPoint[i][j][0] != 0 and self.tabPoint[i][j][0] != 7:
                                                total = self.nbVoisins(i,j,self.tabPoint[i][j][1])
                                                self.nbpoint = self.nbpoint + (total * nb_couronne)
                                                nb_couronne = 0
                for i in range (0,5):
                        for j in range (0,5):
                                self.tabPoint[i][j][2] = 0
                
