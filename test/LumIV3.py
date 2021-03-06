class LumIV3:
	def __init__(self, numero):
		self.nom = "LumIV3"
		self.numero = numero
		self.nbpoint = 0
		self.list_tuile = list()
		self.castle_x = 0
		self.castle_y = 0
		self.lastTile = None
		self.nextPos = numero
		self.tabPoint = None
		self.tabTile = None
		self.nbTile = 0
		self.jouer = False
		self.tourJouer2Joueur = 0
		self.list_tuile_tmp = list()
		self.tmpTile = None
		self.nbpoint_tmp = 0
		self.tabPoint_tmp = None

	def setLastTile(self,T):
		self.lastTile = T

	def setTmpTile(self, T):
		self.tmpTile = T
		
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

	def initListTileTmp(self):
		self.list_tuile_tmp = list()
		for T in self.list_tuile:
			self.list_tuile_tmp.append(T)
		
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
				
	def testSuperpositionChateau(self,T):
		if(T.position_x == self.castle_x and T.position_y == self.castle_y) :
			return True
		if(T.getPos2x() == self.castle_x and T.getPos2y() == self.castle_y) :
			return True
		return False
		
	def testSuperpositionList(self,Tile,lt):
		for T in lt :
			if(Tile.position_x == T.position_x and Tile.position_y == T.position_y) :
				return True
			if(Tile.getPos2x() == T.position_x and Tile.getPos2y() == T.position_y) :
				return True
			if(Tile.position_x == T.getPos2x() and Tile.position_y == T.getPos2y()) :
				return True
			if(Tile.getPos2x() == T.getPos2x() and Tile.getPos2y() == T.getPos2y()) :
				return True
		return False
		
	def testSuperposition(self,T,lt):
		if(self.testSuperpositionChateau(T) or self.testSuperpositionList(T,lt)):
			return True
		return False
		
	def isNotNextCastle(self, Tile) :
		if(Tile.position_x + 1 == self.castle_x and Tile.position_y == self.castle_y) :
			return False
		if(Tile.position_x - 1 == self.castle_x and Tile.position_y == self.castle_y) :
			return False
		if(Tile.position_x == self.castle_x and Tile.position_y + 1 == self.castle_y) :
			return False
		if(Tile.position_x == self.castle_x and Tile.position_y - 1 == self.castle_y) :
			return False
		if(Tile.getPos2x() + 1 == self.castle_x and Tile.getPos2y() == self.castle_y) :
			return False
		if(Tile.getPos2x() - 1 == self.castle_x and Tile.getPos2y() == self.castle_y) :
			return False
		if(Tile.getPos2x() == self.castle_x and Tile.getPos2y() - 1 == self.castle_y) :
			return False
		if(Tile.getPos2x() == self.castle_x and Tile.getPos2y() + 1 == self.castle_y) :
			return False
		return True
		
	def isNextGoodTile(self, Tile, lt):
		for T in lt :
			if T.tuile_1 == Tile.tuile_1 :
				if(Tile.position_x + 1 == T.position_x and Tile.position_y == T.position_y) :
					return True
				if(Tile.position_x - 1 == T.position_x and Tile.position_y == T.position_y) :
					return True
				if(Tile.position_x == T.position_x and Tile.position_y + 1 == T.position_y) :
					return True
				if(Tile.position_x == T.position_x and Tile.position_y - 1 == T.position_y) :
					return True
			if T.tuile_1 == Tile.tuile_2 :
				if(Tile.getPos2x() + 1 == T.position_x and Tile.getPos2y() == T.position_y) :
					return True
				if(Tile.getPos2x() - 1 == T.position_x and Tile.getPos2y() == T.position_y) :
					return True
				if(Tile.getPos2x() == T.position_x and Tile.getPos2y() - 1 == T.position_y) :
					return True
				if(Tile.getPos2x() == T.position_x and Tile.getPos2y() + 1 == T.position_y) :
					return True
			if T.tuile_2 == Tile.tuile_1 :
				if(Tile.position_x + 1 == T.getPos2x() and Tile.position_y == T.getPos2y()) :
					return True
				if(Tile.position_x - 1 == T.getPos2x() and Tile.position_y == T.getPos2y()) :
					return True
				if(Tile.position_x == T.getPos2x() and Tile.position_y + 1 == T.getPos2y()) :
					return True
				if(Tile.position_x == T.getPos2x() and Tile.position_y - 1 == T.getPos2y()) :
					return True
			if T.tuile_2 == Tile.tuile_2 :
				if(Tile.getPos2x() + 1 == T.getPos2x() and Tile.getPos2y() == T.getPos2y()) :
					return True
				if(Tile.getPos2x() - 1 == T.getPos2x() and Tile.getPos2y() == T.getPos2y()) :
					return True
				if(Tile.getPos2x() == T.getPos2x() and Tile.getPos2y() - 1 == T.getPos2y()) :
					return True
				if(Tile.getPos2x() == T.getPos2x() and Tile.getPos2y() + 1 == T.getPos2y()) :
					return True
		return False
	
	def autorisationSauveguarde(self):
		if self.testSuperposition(self.lastTile, self.list_tuile) :
			return False
		if self.isNotNextCastle(self.lastTile) :
			if not(self.isNextGoodTile(self.lastTile, self.list_tuile)) :
				return False
		return True
                
	def tileOrientation(self):
		self.lastTile.orient()

	def initTabPoint(self):
		n = 5
		m = 3
		self.tabPoint = [[[0 for k in xrange(m)] for j in xrange(n)] for i in xrange(n)]
		self.tabPoint[0][0][0] = 7
		
	def initTabPointTmp(self):
		n = 5
		m = 3
		self.tabPoint_tmp = [[[0 for k in xrange(m)] for j in xrange(n)] for i in xrange(n)]
		self.tabPoint_tmp[0][0][0] = 7

	def setTabPointTmp(self):
		for i in range(0,5):
			for j in range(0,5):
				for k in range(0,3):
					self.tabPoint_tmp[i][j][k] = self.tabPoint[i][j][k]

	def resetTabPoint(self):
		for i in range (0,5):
			for j in range (0,5):
				for k in range (0,3):
					self.tabPoint[i][j][k] = 0

	def resetTabPointTmp(self):
		for i in range (0,5):
			for j in range (0,5):
				for k in range (0,3):
					self.tabPoint_tmp[i][j][k] = 0
					
	def ajoutTileTabPoint(self):
		self.tabPoint[self.lastTile.position_y][self.lastTile.position_x][0] = self.lastTile.tuile_1
		self.tabPoint[self.lastTile.position_y][self.lastTile.position_x][1] = self.lastTile.couronne_1
		
		self.tabPoint[self.lastTile.getPos2y()][self.lastTile.getPos2x()][0] = self.lastTile.tuile_2
		self.tabPoint[self.lastTile.getPos2y()][self.lastTile.getPos2x()][1] = self.lastTile.couronne_2

	def ajoutTileTabPointTmp(self):
		self.tabPoint_tmp[self.tmpTile.position_y][self.tmpTile.position_x][0] = self.tmpTile.tuile_1
		self.tabPoint_tmp[self.tmpTile.position_y][self.tmpTile.position_x][1] = self.tmpTile.couronne_1

		self.tabPoint_tmp[self.tmpTile.getPos2y()][self.tmpTile.getPos2x()][0] = self.tmpTile.tuile_2
		self.tabPoint_tmp[self.tmpTile.getPos2y()][self.tmpTile.getPos2x()][1] = self.tmpTile.couronne_2

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

	def nbVoisins_tmp(self,y,x,c):
		global nb_couronne_tmp, nb_voisins_tmp
		nb_couronne_tmp = c
		nb_voisins_tmp = 0
		self.tabPoint_tmp[y][x][2] = 1
		if y - 1 >= 0 and self.tabPoint_tmp[y - 1][x][2] == 0 and self.tabPoint_tmp[y - 1][x][0] == self.tabPoint_tmp[y][x][0]:
			if self.tabPoint_tmp[y - 1][x][1] != 0:
				nb_couronne_tmp = nb_couronne_tmp + self.tabPoint_tmp[y - 1][x][1]
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y-1,x,nb_couronne_tmp)
			else:
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y-1,x,nb_couronne_tmp)
		
		if x + 1 <= 4 and self.tabPoint_tmp[y][x + 1][2] == 0 and self.tabPoint_tmp[y][x + 1][0] == self.tabPoint_tmp[y][x][0]:
			if self.tabPoint_tmp[y][x + 1][1] != 0:
				nb_couronne_tmp = nb_couronne_tmp + self.tabPoint_tmp[y][x + 1][1]
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y,x+1,nb_couronne_tmp)
			else:
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y,x+1,nb_couronne_tmp)
		
		if y + 1 <= 4 and self.tabPoint_tmp[y + 1][x][2] == 0 and self.tabPoint_tmp[y + 1][x][0] == self.tabPoint_tmp[y][x][0]:
			if self.tabPoint_tmp[y + 1][x][1] != 0:
				nb_couronne_tmp = nb_couronne_tmp + self.tabPoint_tmp[y + 1][x][1]
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y+1,x,nb_couronne_tmp)
			else:
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y+1,x,nb_couronne_tmp)
				
		if x - 1 >= 0 and self.tabPoint_tmp[y][x - 1][2] == 0 and self.tabPoint_tmp[y][x - 1][0] == self.tabPoint_tmp[y][x][0]:
			if self.tabPoint_tmp[y][x - 1][1] != 0:
				nb_couronne_tmp = nb_couronne_tmp + self.tabPoint_tmp[y][x - 1][1]
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y,x-1,nb_couronne_tmp)
			else:
				nb_voisins_tmp = nb_voisins_tmp + self.nbVoisins_tmp(y,x-1,nb_couronne_tmp)
		return 1 + nb_voisins_tmp
		
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

	def comptagePointTmp(self):
		global nb_couronne_tmp
		self.nbpoint_tmp = 0
		for i in range(0,5):
			for j in range(0,5):
				if self.tabPoint_tmp[i][j][2] == 0:
					if self.tabPoint_tmp[i][j][0] != 0 and self.tabPoint_tmp[i][j][0] != 7:
						total_tmp = self.nbVoisins_tmp(i,j,self.tabPoint_tmp[i][j][1])
						self.nbpoint_tmp = self.nbpoint_tmp + (total_tmp * nb_couronne_tmp)
						nb_couronne_tmp = 0
		for i in range (0,5):
			for j in range (0,5):
				self.tabPoint_tmp[i][j][2] = 0
	
	def ordreChoix(self,S1,S2,S3,S4,LJ,L):
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
		scoreT1Autre = scoreT2Autre = scoreT3Autre = scoreT4Autre = 0
		if(not bool2joueur):
			self.joueur = True
		else:
			self.tourJouer2Joueur = self.tourJouer2Joueur + 1
			if (self.tourJouer2Joueur == 2):
				self.joueur = True
				self.tourJouer2Joueur = 0
		if(self.nbTile == 0):
			self.tabTile = [0,0,0,0,0,0]
			
			if Tuile1NonUsed :
				scoreT1 = L[0].couronne_1 + L[0].couronne_2
				if(scoreT1 == 0):
					scoreT1 = 1
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
			#recupere personne plus de point
			numero = 0
			point = -1
			egaux = 0
			numeroAutre = 0
			pointAutre = -1
			egauxAutre = 0
			for i in range(0,len(LJ)):
				if LJ[i].nbpoint > point:
					if(not bool2joueur):
						numeroAutre = point
						pointAutre = numero
						egauxAutre = egaux
					point = LJ[i].nbpoint
					numero = i+1
					egaux = 0	
				elif LJ[i].nbpoint == point :
					egaux += 1
			
			if Tuile1NonUsed :
				self.setTmpTile(L[0])
				self.initListTileTmp()
				self.initTabPointTmp()
				self.resetTabPointTmp()
				self.setTabPointTmp()
				self.nbpoint_tmp = 0
				self.test_deplacer()
				if(self.nbpoint_tmp > scoreT1):
					scoreT1 = self.nbpoint_tmp
			else :
				scoreT1 = -1
			if Tuile2NonUsed :
				self.setTmpTile(L[1])
				self.initListTileTmp()
				self.initTabPointTmp()
				self.resetTabPointTmp()
				self.setTabPointTmp()
				self.nbpoint_tmp = 0
				self.test_deplacer()
				if(self.nbpoint_tmp > scoreT2):
					scoreT2 = self.nbpoint_tmp
			else :
				scoreT2 = -1
			if Tuile3NonUsed :
				self.setTmpTile(L[2])
				self.initListTileTmp()
				self.initTabPointTmp()
				self.resetTabPointTmp()
				self.setTabPointTmp()
				self.nbpoint_tmp = 0
				self.test_deplacer()
				if(self.nbpoint_tmp > scoreT3):
					scoreT3 = self.nbpoint_tmp
			else :
				scoreT3 = -1
			if Tuile4NonUsed and (bool3joueur == False):
				self.setTmpTile(L[3])
				self.initListTileTmp()
				self.initTabPointTmp()
				self.resetTabPointTmp()
				self.setTabPointTmp()
				self.nbpoint_tmp = 0
				self.test_deplacer()
				if(self.nbpoint_tmp > scoreT4):
					scoreT4 = self.nbpoint_tmp
			else :
				scoreT4 = -1
			#print("1  {a} 2 : {b} 3 : {c} 4 : {d} ".format(a=scoreT1, b=scoreT2, c=scoreT3, d=scoreT4))
			if(egaux == 0 and self.numero != numero):
				if Tuile1NonUsed :
					for i in range(0,len(LJ)):
						if (LJ[i].nom == "Humain"):
							c = LJ[i].penseChoisir(Mpressed,Tuile1,Tuile2,Tuile3,Tuile4,Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed,AjouterTileJ,bool2joueur,bool3joueur,bool4joueur,L,LJ)
							if(c > scoreT1Autre):
								scoreT1Autre = c
						elif((LJ[i].numero != self.numero and LJ[i].numero == numero and not LJ[i].jouer)):
							LJ[i].setTmpTile(L[0])
							LJ[i].initListTileTmp()
							LJ[i].initTabPointTmp()
							LJ[i].resetTabPointTmp()
							LJ[i].setTabPointTmp()
							LJ[i].nbpoint_tmp = 0
							LJ[i].test_deplacer()
							LJ[i].nbpoint_tmp
							if(LJ[i].nbpoint_tmp > scoreT1Autre):
								scoreT1Autre = LJ[i].nbpoint_tmp
				else :
					scoreT1Autre = -1
					
				if Tuile2NonUsed :
					for i in range(0,len(LJ)):
						if (LJ[i].nom == "Humain"):
							c = LJ[i].penseChoisir(Mpressed,Tuile1,Tuile2,Tuile3,Tuile4,Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed,AjouterTileJ,bool2joueur,bool3joueur,bool4joueur,L,LJ)
							if(c > scoreT2Autre):
								scoreT2Autre = c
						elif(LJ[i].numero != self.numero and LJ[i].numero == numero and not LJ[i].jouer):
							LJ[i].setTmpTile(L[1])
							LJ[i].initListTileTmp()
							LJ[i].initTabPointTmp()
							LJ[i].resetTabPointTmp()
							LJ[i].setTabPointTmp()
							LJ[i].nbpoint_tmp = 0
							LJ[i].test_deplacer()
							LJ[i].nbpoint_tmp
							if(LJ[i].nbpoint_tmp > scoreT2Autre):
								scoreT2Autre = LJ[i].nbpoint_tmp
				else :
					scoreT2Autre = -1
							
				if Tuile3NonUsed :
					for i in range(0,len(LJ)):
						if (LJ[i].nom == "Humain"):
							c = LJ[i].penseChoisir(Mpressed,Tuile1,Tuile2,Tuile3,Tuile4,Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed,AjouterTileJ,bool2joueur,bool3joueur,bool4joueur,L,LJ)
							if(c > scoreT3Autre):
								scoreT3Autre = c
						elif(LJ[i].numero != self.numero and LJ[i].numero == numero and not LJ[i].jouer):
							LJ[i].setTmpTile(L[2])
							LJ[i].initListTileTmp()
							LJ[i].initTabPointTmp()
							LJ[i].resetTabPointTmp()
							LJ[i].setTabPointTmp()
							LJ[i].nbpoint_tmp = 0
							LJ[i].test_deplacer()
							LJ[i].nbpoint_tmp
							if(LJ[i].nbpoint_tmp > scoreT3Autre):
								scoreT3Autre = LJ[i].nbpoint_tmp
				else :
					scoreT3Autre = -1
				
				if Tuile4NonUsed and (bool3joueur == False) :
					for i in range(0,len(LJ)):
						if (LJ[i].nom == "Humain"):
							c = LJ[i].penseChoisir(Mpressed,Tuile1,Tuile2,Tuile3,Tuile4,Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed,AjouterTileJ,bool2joueur,bool3joueur,bool4joueur,L,LJ)
							if(c > scoreT4Autre):
								scoreT4Autre = c
						elif(LJ[i].numero != self.numero and LJ[i].numero == numero and not LJ[i].jouer):
							LJ[i].setTmpTile(L[3])
							LJ[i].initListTileTmp()
							LJ[i].initTabPointTmp()
							LJ[i].resetTabPointTmp()
							LJ[i].setTabPointTmp()
							LJ[i].nbpoint_tmp = 0
							LJ[i].test_deplacer()
							LJ[i].nbpoint_tmp
							if(LJ[i].nbpoint_tmp > scoreT4Autre):
								scoreT4Autre = LJ[i].nbpoint_tmp
				else :
					scoreT4Autre = -1
				if scoreT1Autre > scoreT1 :
					scoreT1 = scoreT1Autre
				if scoreT2Autre > scoreT2 :
					scoreT2 = scoreT2Autre
				if scoreT3Autre > scoreT3 :
					scoreT3 = scoreT3Autre
				if scoreT4Autre > scoreT4 and (bool3joueur == False):
					scoreT4 = scoreT4Autre

		Choix = self.ordreChoix(scoreT1,scoreT2,scoreT3,scoreT4,LJ,L)
			
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
		
	def updateTabTile(self):
		self.tabTile[self.lastTile.tuile_1 - 1] =+1
		self.tabTile[self.lastTile.tuile_2 - 1] =+1
		
	def recherchePos(self,type,lt):
		l = list()
		x = None
		for x in lt :
			if(x.tuile_1 == type): l.append([x.position_x,x.position_y])
			if(x.tuile_2 == type): l.append([x.getPos2x(),x.getPos2y()])
		return l
		
	def isNotCrossing(self,Tile) :
		if(Tile.position_x < 0 or Tile.position_x > 4): 
			return False
		if(Tile.position_y < 0 or Tile.position_y > 4): 
			return False
		if(Tile.getPos2x() < 0 or Tile.getPos2x() > 4): 
			return False
		if(Tile.getPos2y() < 0 or Tile.getPos2y() > 4): 
			return False
		return True 
			
		
	def deplacer(self,Kpressed,Key,bool2Joueur,bool3Joueur,bool4Joueur,j,AjouterTileJ,DeplacerPlateau,NextTurn,nb_tour,TheEnd):
		w = x = y = z = None
		if self.nbTile == 0 :
			self.tileRight()
			self.updateTabTile()
			self.list_tuile.append(self.lastTile)
			self.ajoutTileTabPoint()
			self.comptagePoint()
			self.lastTile = None
			if bool3Joueur :
				j = (j+1) % 3
			else : 
				j = (j+1) % 4
			if j == 0 and not (nb_tour == 0):
				NextTurn = True
			self.nbTile += 1
			return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
		else :
			for w in range (0,5) :
				if(self.tabTile[self.lastTile.tuile_1 - 1] > self.tabTile[self.lastTile.tuile_2 -1 ]):
					l = self.recherchePos(self.lastTile.tuile_1, self.list_tuile)
					for x in l :
						for y in range(0,4) :
							if(y == 0):
								self.lastTile.setPosistion(x[0]+1,x[1])
							if(y == 1):
								self.lastTile.setPosistion(x[0]-1,x[1])
							if(y == 2):
								self.lastTile.setPosistion(x[0],x[1]+1)
							if(y == 3):
								self.lastTile.setPosistion(x[0],x[1]-1)
							for z in range(0,4) :
								if(z == 0):
									self.lastTile.setOrientation(0)
								if(z == 1):
									self.lastTile.setOrientation(1)
								if(z == 2):
									self.lastTile.setOrientation(2)
								if(z == 3):
									self.lastTile.setOrientation(3)
								if not(self.testSuperposition(self.lastTile, self.list_tuile)) and self.isNextGoodTile(self.lastTile,self.list_tuile) and self.isNotCrossing(self.lastTile):
									self.updateTabTile()
									self.list_tuile.append(self.lastTile)
									self.ajoutTileTabPoint()
									self.comptagePoint()
									self.lastTile = None
									if bool3Joueur :
										j = (j+1) % 3
									else : 
										j = (j+1) % 4
									if j == 0 and not (nb_tour == 0):
										NextTurn = True
									if j == 0 and nb_tour == 0:
										TheEnd = True
									self.nbTile += 1
									return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
					l = self.recherchePos(self.lastTile.tuile_2,self.list_tuile)
					for x in l :
						for y in range(0,12) :
							if(y == 0):
								self.lastTile.setPosistion(x[0]+1,x[1]+1)
								self.lastTile.setOrientation(3)
							if(y == 1):
								self.lastTile.setPosistion(x[0]+1,x[1]+1)
								self.lastTile.setOrientation(2)
							if(y == 2):
								self.lastTile.setPosistion(x[0]-1,x[1]+1)
								self.lastTile.setOrientation(3)
							if(y == 3):
								self.lastTile.setPosistion(x[0]-1,x[1]+1)
								self.lastTile.setOrientation(0)
							if(y == 4):
								self.lastTile.setPosistion(x[0]+1,x[1]-1)
								self.lastTile.setOrientation(1)
							if(y == 5):
								self.lastTile.setPosistion(x[0]+1,x[1]-1)
								self.lastTile.setOrientation(2)
							if(y == 6):
								self.lastTile.setPosistion(x[0]-1,x[1]-1)
								self.lastTile.setOrientation(0)
							if(y == 7):
								self.lastTile.setPosistion(x[0]-1,x[1]-1)
								self.lastTile.setOrientation(1)
							if(y == 8):
								self.lastTile.setPosistion(x[0]-2,x[1])
								self.lastTile.setOrientation(3)
							if(y == 9):
								self.lastTile.setPosistion(x[0]+2,x[1])
								self.lastTile.setOrientation(1)
							if(y == 10):
								self.lastTile.setPosistion(x[0],x[1]-2)
								self.lastTile.setOrientation(0)
							if(y == 11):
								self.lastTile.setPosistion(x[0],x[1]+2)
								self.lastTile.setOrientation(2)
							if not(self.testSuperposition(self.lastTile, self.list_tuile)) and self.isNextGoodTile(self.lastTile,self.list_tuile) and self.isNotCrossing(self.lastTile):
								self.updateTabTile()
								self.list_tuile.append(self.lastTile)
								self.ajoutTileTabPoint()
								self.comptagePoint()
								self.lastTile = None
								if bool3Joueur :
									j = (j+1) % 3
								else : 
									j = (j+1) % 4
								if j == 0 and not (nb_tour == 0):
									NextTurn = True
								if j == 0 and nb_tour == 0:
									TheEnd = True
								self.nbTile += 1
								return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
					for y in range(0,4) :
						if(y == 0):
							self.lastTile.setPosistion(self.castle_x+1,self.castle_y)
						if(y == 1):
							self.lastTile.setPosistion(self.castle_x-1,self.castle_y)
						if(y == 2):
							self.lastTile.setPosistion(self.castle_x,self.castle_y+1)
						if(y == 3):
							self.lastTile.setPosistion(self.castle_x,self.castle_y-1)
						for z in range(0,4) :
							if(z == 0):
								self.lastTile.setOrientation(0)
							if(z == 1):
								self.lastTile.setOrientation(1)
							if(z == 2):
								self.lastTile.setOrientation(2)
							if(z == 3):
								self.lastTile.setOrientation(3)
							if not(self.testSuperposition(self.lastTile, self.list_tuile)) and not(self.isNotNextCastle(self.lastTile)) and self.isNotCrossing(self.lastTile):
								self.updateTabTile()
								self.list_tuile.append(self.lastTile)
								self.ajoutTileTabPoint()
								self.comptagePoint()
								self.lastTile = None
								if bool3Joueur :
									j = (j+1) % 3
								else : 
									j = (j+1) % 4
								if j == 0 and not (nb_tour == 0):
									NextTurn = True
								if j == 0 and nb_tour == 0:
									TheEnd = True
								self.nbTile += 1
								return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
				else :
					l = self.recherchePos(self.lastTile.tuile_2,self.list_tuile)
					for x in l :
						for y in range(0,12) :
							if(y == 0):
								self.lastTile.setPosistion(x[0]+1,x[1]+1)
								self.lastTile.setOrientation(3)
							if(y == 1):
								self.lastTile.setPosistion(x[0]+1,x[1]+1)
								self.lastTile.setOrientation(2)
							if(y == 2):
								self.lastTile.setPosistion(x[0]-1,x[1]+1)
								self.lastTile.setOrientation(3)
							if(y == 3):
								self.lastTile.setPosistion(x[0]-1,x[1]+1)
								self.lastTile.setOrientation(0)
							if(y == 4):
								self.lastTile.setPosistion(x[0]+1,x[1]-1)
								self.lastTile.setOrientation(1)
							if(y == 5):
								self.lastTile.setPosistion(x[0]+1,x[1]-1)
								self.lastTile.setOrientation(2)
							if(y == 6):
								self.lastTile.setPosistion(x[0]-1,x[1]-1)
								self.lastTile.setOrientation(0)
							if(y == 7):
								self.lastTile.setPosistion(x[0]-1,x[1]-1)
								self.lastTile.setOrientation(1)
							if(y == 8):
								self.lastTile.setPosistion(x[0]-2,x[1])
								self.lastTile.setOrientation(3)
							if(y == 9):
								self.lastTile.setPosistion(x[0]+2,x[1])
								self.lastTile.setOrientation(1)
							if(y == 10):
								self.lastTile.setPosistion(x[0],x[1]-2)
								self.lastTile.setOrientation(0)
							if(y == 11):
								self.lastTile.setPosistion(x[0],x[1]+2)
								self.lastTile.setOrientation(2)
							if not(self.testSuperposition(self.lastTile, self.list_tuile)) and self.isNextGoodTile(self.lastTile,self.list_tuile) and self.isNotCrossing(self.lastTile):
								self.updateTabTile()
								self.list_tuile.append(self.lastTile)
								self.ajoutTileTabPoint()
								self.comptagePoint()
								self.lastTile = None
								if bool3Joueur :
									j = (j+1) % 3
								else : 
									j = (j+1) % 4
								if j == 0 and not (nb_tour == 0):
									NextTurn = True
								if j == 0 and nb_tour == 0:
									TheEnd = True
								self.nbTile += 1
								return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
					l = self.recherchePos(self.lastTile.tuile_1, self.list_tuile)
					for x in l :
						for y in range(0,4) :
							if(y == 0):
								self.lastTile.setPosistion(x[0]+1,x[1])
							if(y == 1):
								self.lastTile.setPosistion(x[0]-1,x[1])
							if(y == 2):
								self.lastTile.setPosistion(x[0],x[1]+1)
							if(y == 3):
								self.lastTile.setPosistion(x[0],x[1]-1)
							for z in range(0,4) :
								if(z == 0):
									self.lastTile.setOrientation(0)
								if(z == 1):
									self.lastTile.setOrientation(1)
								if(z == 2):
									self.lastTile.setOrientation(2)
								if(z == 3):
									self.lastTile.setOrientation(3)
								if not(self.testSuperposition(self.lastTile, self.list_tuile)) and self.isNextGoodTile(self.lastTile,self.list_tuile) and self.isNotCrossing(self.lastTile):
									self.updateTabTile()
									self.list_tuile.append(self.lastTile)
									self.ajoutTileTabPoint()
									self.comptagePoint()
									self.lastTile = None
									if bool3Joueur :
										j = (j+1) % 3
									else : 
										j = (j+1) % 4
									if j == 0 and not (nb_tour == 0):
										NextTurn = True
									if j == 0 and nb_tour == 0:
										TheEnd = True
									self.nbTile += 1
									return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
					for y in range(0,4) :
						if(y == 0):
							self.lastTile.setPosistion(self.castle_x+1,self.castle_y)
						if(y == 1):
							self.lastTile.setPosistion(self.castle_x-1,self.castle_y)
						if(y == 2):
							self.lastTile.setPosistion(self.castle_x,self.castle_y+1)
						if(y == 3):
							self.lastTile.setPosistion(self.castle_x,self.castle_y-1)
						for z in range(0,4) :
							if(z == 0):
								self.lastTile.setOrientation(0)
							if(z == 1):
								self.lastTile.setOrientation(1)
							if(z == 2):
								self.lastTile.setOrientation(2)
							if(z == 3):
								self.lastTile.setOrientation(3)
							if not(self.testSuperposition(self.lastTile, self.list_tuile)) and not(self.isNotNextCastle(self.lastTile)) and self.isNotCrossing(self.lastTile):
								self.updateTabTile()
								self.list_tuile.append(self.lastTile)
								self.ajoutTileTabPoint()
								self.comptagePoint()
								self.lastTile = None
								if bool3Joueur :
									j = (j+1) % 3
								else : 
									j = (j+1) % 4
								if j == 0 and not (nb_tour == 0):
									NextTurn = True
								if j == 0 and nb_tour == 0:
									TheEnd = True
								self.nbTile += 1
								return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
				self.plateauRight()
				self.plateauDown()
		self.lastTile = None
		self.plateauUp()
		self.plateauLeft()
		self.plateauUp()
		self.plateauLeft()
		self.plateauUp()
		self.plateauLeft()
		self.plateauUp()
		self.plateauLeft()
		if bool3Joueur :
			j = (j+1) % 3
		else : 
			j = (j+1) % 4
		if j == 0 and not (nb_tour == 0):
			NextTurn = True
		if j == 0 and nb_tour == 0:
			TheEnd = True 
		return False,0,j,AjouterTileJ,DeplacerPlateau,NextTurn,TheEnd
		
		
	def test_deplacer(self):
		x = y = z = None
		if (self.tabTile[self.tmpTile.tuile_1 - 1] > self.tabTile[self.tmpTile.tuile_2 -1 ]):
			l = self.recherchePos(self.tmpTile.tuile_1,self.list_tuile_tmp)
			if (l != []):
				for x in l :
					for y in range(0,4) :
						if(y == 0):
							self.tmpTile.setPosistion(x[0]+1,x[1])
						if(y == 1):
							self.tmpTile.setPosistion(x[0]-1,x[1])
						if(y == 2):
							self.tmpTile.setPosistion(x[0],x[1]+1)
						if(y == 3):
							self.tmpTile.setPosistion(x[0],x[1]-1)
						for z in range(0,4) :
							if(z == 0):
								self.tmpTile.setOrientation(0)
							if(z == 1):
								self.tmpTile.setOrientation(1)
							if(z == 2):
								self.tmpTile.setOrientation(2)
							if(z == 3):
								self.tmpTile.setOrientation(3)
							if not(self.testSuperposition(self.tmpTile, self.list_tuile_tmp)) and self.isNextGoodTile(self.tmpTile,self.list_tuile_tmp) and self.isNotCrossing(self.tmpTile):
								self.list_tuile_tmp.append(self.tmpTile)
								self.ajoutTileTabPointTmp()
								self.comptagePointTmp()
								self.tmpTile = None
								return 0
				for y in range(0,4) :
					if(y == 0):
						self.tmpTile.setPosistion(self.castle_x+1,self.castle_y)
					if(y == 1):
						self.tmpTile.setPosistion(self.castle_x-1,self.castle_y)
					if(y == 2):
						self.tmpTile.setPosistion(self.castle_x,self.castle_y+1)
					if(y == 3):
						self.tmpTile.setPosistion(self.castle_x,self.castle_y-1)
					for z in range(0,4) :
						if(z == 0):
							self.tmpTile.setOrientation(0)
						if(z == 1):
							self.tmpTile.setOrientation(1)
						if(z == 2):
							self.tmpTile.setOrientation(2)
						if(z == 3):
							self.tmpTile.setOrientation(3)
						if not(self.testSuperposition(self.tmpTile, self.list_tuile_tmp)) and not(self.isNotNextCastle(self.tmpTile)) and self.isNotCrossing(self.tmpTile):
							self.list_tuile_tmp.append(self.tmpTile)
							self.ajoutTileTabPointTmp()
							self.comptagePointTmp()
							self.tmpTile = None
							return 1
		else:
			l = self.recherchePos(self.tmpTile.tuile_2,self.list_tuile_tmp)
			if(l == []) :
				for y in range(0,4) :
					if(y == 0):
						self.tmpTile.setPosistion(self.castle_x+1,self.castle_y)
					if(y == 1):
						self.tmpTile.setPosistion(self.castle_x-1,self.castle_y)
					if(y == 2):
						self.tmpTile.setPosistion(self.castle_x,self.castle_y+1)
					if(y == 3):
						self.tmpTile.setPosistion(self.castle_x,self.castle_y-1)
					for z in range(0,4) :
						if(z == 0):
							self.tmpTile.setOrientation(0)
						if(z == 1):
							self.tmpTile.setOrientation(1)
						if(z == 2):
							self.tmpTile.setOrientation(2)
						if(z == 3):
							self.tmpTile.setOrientation(3)
						if not(self.testSuperposition(self.tmpTile, self.list_tuile_tmp)) and not(self.isNotNextCastle(self.tmpTile)) and self.isNotCrossing(self.tmpTile):
							self.list_tuile_tmp.append(self.tmpTile)
							self.ajoutTileTabPointTmp()
							self.comptagePointTmp()
							self.tmpTile = None
							return 0
			else :
				for x in l :
					for y in range(0,8) :
						if(y == 0):
							self.tmpTile.setPosistion(x[0]+1,x[1]+1)
							self.tmpTile.setOrientation(3)
						if(y == 1):
							self.tmpTile.setPosistion(x[0]+1,x[1]+1)
							self.tmpTile.setOrientation(2)
						if(y == 2):
							self.tmpTile.setPosistion(x[0]-1,x[1]+1)
							self.tmpTile.setOrientation(3)
						if(y == 3):
							self.tmpTile.setPosistion(x[0]-1,x[1]+1)
							self.tmpTile.setOrientation(0)
						if(y == 4):
							self.tmpTile.setPosistion(x[0]+1,x[1]-1)
							self.tmpTile.setOrientation(1)
						if(y == 5):
							self.tmpTile.setPosistion(x[0]+1,x[1]-1)
							self.tmpTile.setOrientation(2)
						if(y == 6):
							self.tmpTile.setPosistion(x[0]-1,x[1]-1)
							self.tmpTile.setOrientation(0)
						if(y == 7):
							self.tmpTile.setPosistion(x[0]-1,x[1]-1)
							self.tmpTile.setOrientation(1)
						if not(self.testSuperposition(self.tmpTile, self.list_tuile_tmp)) and self.isNextGoodTile(self.tmpTile,self.list_tuile_tmp) and self.isNotCrossing(self.tmpTile):
							self.list_tuile_tmp.append(self.tmpTile)
							self.ajoutTileTabPointTmp()
							self.comptagePointTmp()
							self.tmpTile = None
							return 0
				for y in range(0,4) :
					if(y == 0):
						self.tmpTile.setPosistion(self.castle_x+1,self.castle_y)
					if(y == 1):
						self.tmpTile.setPosistion(self.castle_x-1,self.castle_y)
					if(y == 2):
						self.tmpTile.setPosistion(self.castle_x,self.castle_y+1)
					if(y == 3):
						self.tmpTile.setPosistion(self.castle_x,self.castle_y-1)
					for z in range(0,4) :
						if(z == 0):
							self.tmpTile.setOrientation(0)
						if(z == 1):
							self.tmpTile.setOrientation(1)
						if(z == 2):
							self.tmpTile.setOrientation(2)
						if(z == 3):
							self.tmpTile.setOrientation(3)
						if not(self.testSuperposition(self.tmpTile, self.list_tuile_tmp)) and not(self.isNotNextCastle(self.tmpTile)) and self.isNotCrossing(self.tmpTile):
							self.list_tuile_tmp.append(self.tmpTile)
							self.ajoutTileTabPointTmp()
							self.comptagePointTmp()
							self.tmpTile = None
							return 0
		self.tmpTile = None
		return 0
