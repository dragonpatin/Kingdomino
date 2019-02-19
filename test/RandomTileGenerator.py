from Tile import *
from ListCreator import *
from random import randint

class RandomTileGenerator:
    def __init__(self):
        self.taille = 48
        self.lc = ListCreator()
        self.l = self.lc.createList()
        
    def generate(self):
        r = randint(0,self.taille-1)
        t = self.l[r]
        del self.l[r]
        self.taille = self.taille - 1
        return t
