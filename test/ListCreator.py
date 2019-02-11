from Tile import *

class ListCreator :
    def __init__(self):
        self.fic = "data/KingDomino.txt"
        
    def createList(self) :
        lt = list()
        with open(self.fic,"r") as f:
            for line in f :
                tile = Tile(10*(ord(line[0])-48)+ord(line[1])-48,ord(line[3])-48,ord(line[5])-48,ord(line[7])-48,ord(line[9])-48)
                lt.append(tile)
            f.close()
        return lt
