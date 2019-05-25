from Player import *
from DumE import *
from DumEV2 import *
from DumEV3 import *
from NumP import *
from MumC import *
from RumL import *
from DumA import *
from LumI import *
from RandomTileGenerator import *

class Game : 
	def __init__(self, joueurs):
		self.nbjoueurs = joueurs
		
	def createListJoueurs(self,ChoixJ1 = -1,ChoixV1 = -1,ChoixJ2 = -1,ChoixV2 = -1,ChoixJ3 = -1,ChoixV3 = -1,ChoixJ4 = -1,ChoixV4 = -1):
		lj = list()
		if ChoixJ1 == 0:
			lj.append(Player(1))
		if ChoixJ1 == 1:
			if(ChoixV1 == 0):
				lj.append(DumE(1))
			if(ChoixV1 == 1):
				lj.append(DumEV2(1))
			if(ChoixV1 == 2):
				lj.append(DumEV3(1))
		if ChoixJ1 == 2:
			lj.append(NumP(1))
		if ChoixJ1 == 3:
			lj.append(MumC(1))
		if ChoixJ1 == 4:
			lj.append(RumL(1))
		if ChoixJ1 == 5:
			lj.append(LumI(1))
		if ChoixJ1 == 6:
			lj.append(DumA(1))
        
		if ChoixJ2 == 0:
			lj.append(Player(2))
		if ChoixJ2 == 1:
			if(ChoixV2 == 0):
				lj.append(DumE(2))
			if(ChoixV2 == 1):
				lj.append(DumEV2(2))
			if(ChoixV2 == 2):
				lj.append(DumEV3(2))
		if ChoixJ2 == 2:
			lj.append(NumP(2))
		if ChoixJ2 == 3:
			lj.append(MumC(2))
		if ChoixJ2 == 4:
			lj.append(RumL(2))
		if ChoixJ2 == 5:
			lj.append(LumI(2))
		if ChoixJ2 == 6:
			lj.append(DumA(2))
        
		if ChoixJ3 == 0:
			lj.append(Player(3))
		if ChoixJ3 == 1:
			if(ChoixV3 == 0):
				lj.append(DumE(3))
			if(ChoixV3 == 1):
				lj.append(DumEV2(3))
			if(ChoixV3 == 2):
				lj.append(DumEV3(3))
		if ChoixJ3 == 2:
			lj.append(NumP(3))
		if ChoixJ3 == 3:
			lj.append(MumC(3))
		if ChoixJ3 == 4:
			lj.append(RumL(3))
		if ChoixJ3 == 5:
			lj.append(LumI(3))
		if ChoixJ3 == 6:
			lj.append(DumA(3))

		if ChoixJ4 == 0:
			lj.append(Player(4))
		if ChoixJ4 == 1:
			if(ChoixV1 == 0):
				lj.append(DumE(4))
			if(ChoixV1 == 1):
				lj.append(DumEV2(4))
			if(ChoixV1 == 2):
				lj.append(DumEV3(4))
		if ChoixJ4 == 2:
			lj.append(NumP(4))
		if ChoixJ4 == 3:
			lj.append(MumC(4))
		if ChoixJ4 == 4:
			lj.append(RumL(4))
		if ChoixJ4 == 5:
			lj.append(LumI(4))
		if ChoixJ4 == 6:
			lj.append(DumA(4))

		return lj
