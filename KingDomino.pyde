from test.ListCreator import *
from test.Game import *
from test.RandomTileGenerator import *

rectSize = 90
jouerOver = regleOver = quitterOver = Joueur1Over = Joueur2Over = Joueur4Over = False
reglePrecOver = regleSuivOver = regleMenuOver = False
regleColor = color(255)
jouerColor = color(255)
quitterColor = color(255)
fps = 30
boolQuitter = boolRegle = boolJouer = bool2Joueur = bool3Joueur = bool4Joueur = bool2Joueur = bool3Joueur = bool4Joueur = False
boolMenu = True
boolResize = True
regleInt = 0
LT = None
LJ = None

def Regle():
    updateRegle(mouseX, mouseY)
    global boolResize
    if regleInt == 0:
        image(ImgRegle1, 0, 0)
        image(fleche1,600, 629)
        image(croix,335,665)
        if boolResize :
            this.surface.setSize(ImgRegle1.width, ImgRegle1.height)
            boolResize = False
            rect(regleX,regleY,200,50,20)  
            #rect(regleX,regleY,200,50,20)  
    if regleInt == 1:
        image(ImgRegle2, 0, 0)
        image(fleche1,600, 629)
        image(fleche2,0, 629)
        image(croix,335,665)
        if boolResize :
            this.surface.setSize(ImgRegle2.width, ImgRegle2.height)
            boolResize = False
    if regleInt == 2:
        image(ImgRegle3, 0, 0)
        image(fleche1,600, 629)
        image(fleche2,0, 629)
        image(croix,335,665)
        if boolResize :
            this.surface.setSize(ImgRegle3.width, ImgRegle3.height)
            boolResize = False
    if regleInt == 3:
        image(ImgRegle4, 0, 0)
        image(fleche2,0, 629)
        image(croix,335,665)
        if boolResize :
            this.surface.setSize(ImgRegle4.width, ImgRegle4.height)
            boolResize = False
    
def Acceuil():
    # Displays the image at its actual size at point (0,0)
    image(imgMenue, 0, 0)
    update(mouseX, mouseY)
    stroke(0)
    if jouerOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(jouerX,jouerY,200,50,20)
    if regleOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(regleX,regleY,200,50,20)   
    if quitterOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(quitterX,quitterY,200,50,20)    
    fill(color(255,0,0))
    textSize(40)
    text("Jouer", 300, 242) 
    text("Regle", 300, 342) 
    text("Quitter", 280, 442)
    
def Jouer():
    image(imgMenue, 0, 0)
    update(mouseX, mouseY)
    stroke(0)
    if jouerOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(jouerX,jouerY,200,50,20)
    if regleOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(regleX,regleY,200,50,20)   
    if quitterOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(quitterX,quitterY,200,50,20)      
    fill(color(255,0,0))
    textSize(40)
    text("2 Joueurs", 255, 244) 
    text("3 Joueurs", 255, 344) 
    text("4 Joueurs", 255, 444)

def Jeu2Joueurs():
    clear()
    background(255,255,255)
    global boolJouer, LT, LJ
    boolJouer = False
    LC = Game(2)
    LJ = LC.createListJoueurs()
    RTG = RandomTileGenerator()
    fill(color(255,0,0))
    for i in range(0, RTG.taille):
        T = RTG.generate()
        print("la tuile {a} est : {b} {c} {d} {e}".format(a=T.numero,b=T.tuile_1,c=T.couronne_1,d=T.tuile_2,e=T.couronne_2))
    fill(color(0,0,0))
    textSize(20)
    for player in LJ :
        print("Joueur {a}".format(a = player.nom))
        textAlign(CENTER, CENTER)
        text("Joueur {a}".format(a = player.nom), 350, 400 + player.nom * 30)
    fill(color(0,0,0))
    textSize(20)
    textAlign(CENTER, CENTER)
    text("Vous jouez actuellement a 2 joueurs", 350, 60)
    text("la tuile {a} est : {b} {c} {d} {e}".format(a=T.numero,b=T.tuile_1,c=T.couronne_1,d=T.tuile_2,e=T.couronne_2), 350, 350)
    
    


def setup():
    LC = ListCreator()
    global LT
    LT = LC.createList()
    for tile in LT :
        print("la tuile {a} est : {b} {c} {d} {e}".format(a=tile.numero,b=tile.tuile_1,c=tile.couronne_1,d=tile.tuile_2,e=tile.couronne_2))
    # The image file must be in the data folder of the current sketch
    # to load successfully
    size(700, 700)
    global imgMenue,ImgRegle1,ImgRegle2,ImgRegle3,ImgRegle4,fleche1,fleche2,croix
    imgMenue = loadImage("data/Kingdomino.png")    # Load the image into the program
    imgMenue.resize( 700 , 700 )
    ImgRegle1 = loadImage("data/Help1.PNG")
    ImgRegle1.resize( 700 , 700 )
    ImgRegle2 = loadImage("data/Help2.PNG")
    ImgRegle2.resize( 700 , 700 )
    ImgRegle3 = loadImage("data/Help3.PNG")
    ImgRegle3.resize( 700 , 700 )
    ImgRegle4 = loadImage("data/Help4.PNG")
    ImgRegle4.resize( 700 , 700 )
    fleche1 = loadImage("data/flechedroite.png")
    fleche1.resize(100,100)
    fleche2 = loadImage("data/flechegauche.png")
    fleche2.resize(100,100)
    croix = loadImage("data/multiply.png")
    croix.resize(25,25)
    global jouerX, jouerY, regleX, regleY, quitterX, quitterY 
    jouerX = width / 2 - rectSize - 10
    jouerY = (height - 200 )/ 2 - rectSize / 2
    regleX = width / 2 - rectSize - 10
    regleY = (height  )/ 2 - rectSize / 2
    quitterX = width / 2 - rectSize - 10
    quitterY = (height + 200 )/ 2 - rectSize / 2
    ellipseMode(CENTER)
    frameRate(fps)
    this.surface.setResizable(True);

def draw():
    if boolRegle:
        Regle()
    if boolMenu:
        Acceuil()
    if boolJouer:
        Jouer()
    if bool2Joueur and boolJouer:
        Jeu2Joueurs()
    if boolQuitter:
        exit()
          
def update(x, y):
    global jouerOver, regleOver, quitterOver, Joueur2Over, Joueur3Over, Joueur4Over
    jouerOver = Joueur2Over = overRect(jouerX, jouerY, 200, 50)
    regleOver = Joueur3Over = overRect(regleX, regleY, 200, 50)
    quitterOver = Joueur4Over = overRect(quitterX, quitterY, 200, 50)

def updateRegle(x, y):
    global reglePrecOver, regleSuivOver,regleMenuOver
    reglePrecOver = overRect(0, 629, 100, 100)
    regleSuivOver = overRect(600, 629, 100, 100)
    regleMenuOver = overRect(335, 665, 25, 25)
    
def mousePressed():
    global currentColor, boolQuitter, boolRegle, boolJouer, boolMenu, bool2Joueur, bool3Joueur, bool4Joueur,reglePrecOver, regleSuivOver,regleMenuOver,regleInt
    if boolJouer:
        if Joueur2Over:
            currentColor = regleColor
            bool2Joueur = True
            print(2)
        if Joueur3Over:
            currentColor = regleColor
            bool3Joueur = True
            print(3)
        if Joueur4Over:
            currentColor = regleColor
            bool4Joueur = True
            print(4)
            
    if boolMenu:
        if jouerOver:
            currentColor = regleColor
            boolJouer = True
            boolMenu = False
        if regleOver:
            currentColor = regleColor
            boolRegle = True
            boolMenu = False
        if quitterOver:
            currentColor = regleColor
            boolQuitter = True
            
    if boolRegle:
        if regleSuivOver:
            regleInt+=1
        if reglePrecOver:
            regleInt-=1
        if regleMenuOver:
            boolMenu = True
            boolRegle = False
            

def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height
