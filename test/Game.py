from Player import *
from RandomTileGenerator import *

class Game : 
	def __init__(self, joueurs):
		self.nbjoueurs = joueurs
		
	def createListJoueurs(self):
		lj = list()
		for i in range(1,self.nbjoueurs+1):
			player = Player(i)
			lj.append(player)
		return lj
