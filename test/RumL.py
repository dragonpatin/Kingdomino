class RumL:
	"""docstring for RumL"""
	def __init__(self, nom):
		self.nom = nom
		self.nbpoint = 0
		self.list_tuile = list()
		self.castle_x = 0
		self.castle_y = 0
		self.lastTile = None
		self.nextPos = nom
		self.tabPoint = None
		self.tabTile = None
		self.nbTile = 0

	def setLastTile(self,T):
		self.lastTile = T
		
	def setNextPos(self,pos):
		self.nextPos = pos
		
	def getNextPos(self):
		return self.nextPos
		
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

def ordreChoix(self,S1,S2,S3,S4):
		Choix = 0
		S = -1
		if S1 > S :
			Choix = 1
			S = S1
		if S2 > S :
			Choix = 2
			S = S2
		if S3 > S :
			Choix = 3
			S = S3
		if S4 > S :
			Choix = 4
			S = S4
		return Choix
	

	def choisir(self,Mpressed,Tuile1,Tuile2,Tuile3,Tuile4,Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed,AjouterTileJ,bool2joueur,bool3joueur,bool4joueur,L,LJ):
		scoreT1 = scoreT2 = scoreT3 = scoreT4 = 0
		if(self.nbTile == 0):
			self.tabTile = [0,0,0,0,0,0];
			
			if Tuile1NonUsed :
				scoreT1 = L[0].couronne_1 + L[0].couronne_2
			else :
				scoreT1 = -1
				
			if Tuile2NonUsed :
				scoreT2 = L[1].couronne_1 + L[1].couronne_2
			else :
				scoreT2 = -1
				
			if Tuile3NonUsed :
				scoreT3 = L[2].couronne_1 + L[2].couronne_2
			else :
				scoreT3 = -1
			
			if Tuile4NonUsed and (bool3joueur == False) :
				scoreT4 = L[3].couronne_1 + L[3].couronne_2
			else :
				scoreT4 = -1
				
		else :
			if Tuile1NonUsed :
				scoreT1 = self.tabTile[L[0].tuile_1 - 1] + self.tabTile[L[0].tuile_2 - 1]
			else :
				scoreT1 = -1
				
			if Tuile2NonUsed :
				scoreT2 = self.tabTile[L[1].tuile_1 - 1] + self.tabTile[L[1].tuile_2 - 1]
			else :
				scoreT2 = -1
				
			if Tuile3NonUsed :
				scoreT3 = self.tabTile[L[2].tuile_1 - 1] + self.tabTile[L[2].tuile_2 - 1]
			else :
				scoreT3 = -1
			
			if Tuile4NonUsed and (bool3joueur == False) :
				scoreT4 = self.tabTile[L[3].tuile_1 - 1] + self.tabTile[L[3].tuile_2 - 1]
			else :
				scoreT4 = -1
				
		
		Choix = self.ordreChoix(scoreT1,scoreT2,scoreT3,scoreT4)
			
		if Choix == 1:
			Tuile1NonUsed = False
			self.setLastTile(L[0])
			self.setNextPos(1)
		elif Choix == 2 :
			Tuile2NonUsed = False
			self.setLastTile(L[1])
			self.setNextPos(2)
		elif Choix == 3 :
			Tuile3NonUsed = False
			self.setLastTile(L[2])
			self.setNextPos(3)
		elif Choix == 4 :
			Tuile4NonUsed = False
			self.setLastTile(L[3])
			self.setNextPos(4)
				
		return False,Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed,AjouterTileJ
		