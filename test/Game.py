from Player import *
from RandomTileGenerator import *

class Game : 
	def __init__(self, joueurs):
		self.nbjoueurs = joueurs
		
	def createListJoueurs(self,ChoixJ1 = -1,ChoixJ2 = -1,ChoixJ3 = -1,ChoixJ4 = -1):
		lj = list()
		if ChoixJ1 == 0:
			lj.append(Player(1))
		if ChoixJ2 == 0:
			lj.append(Player(2))
		if ChoixJ3 == 0:
			lj.append(Player(3))
		if ChoixJ4 == 0:
			lj.append(Player(4))
		return lj
