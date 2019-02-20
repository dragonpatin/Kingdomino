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
boolQuitter = boolRegle = boolJouer = bool2Joueur = bool3Joueur = bool4Joueur = bool3Joueur = bool4Joueur =  boolrelance = False
boolMenu = True
boolResize = True
regleInt = 0
LT = None
LJ = None
i = 0
j = 0

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
    
def affiche_tuile(numero,List_Plateau):
    pos1x = 50
    pos1y = 70*numero
    pos2x = 110
    pos2y = 70*numero
    for T in List_Plateau:
        # #Champs
        if T.tuile_1 == 1: 
            if T.couronne_1 == 1:
                image(champ1,pos1x,pos1y)
            else:
                image(champ0,pos1x,pos1y)
        #plaines
        if T.tuile_1 == 2:
            if T.couronne_1 == 1:
                image(plaine1,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(plaine2,pos1x,pos1y)
            else :
                image(plaine0,pos1x,pos1y)
        #oceans
        if T.tuile_1 == 3:
            if T.couronne_1 == 1:
                image(ocean1,pos1x,pos1y)
            else:
                image(ocean0,pos1x,pos1y)
        #marais
        if T.tuile_1 == 4:
            if T.couronne_1 == 1:
                image(plaine1,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(plaine2,pos1x,pos1y)
            else :
                image(plaine0,pos1x,pos1y)
        #Forets
        if T.tuile_1 == 5:
            if T.couronne_1 == 1:
                image(foret1,pos1x,pos1y)
            else :
                image(foret0,pos1x,pos1y)
        #Mines
        if T.tuile_1 == 6:
            if T.couronne_1 == 1:
                image(mine1,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(mine2,pos1x,pos1y)
            elif T.couronne_1 == 3:
                image(mine3,pos1x,pos1y)
            else :
                image(mine0,pos1x,pos1y)
        #--------------------------- Tuile 2 -------------------
        #Champs
        if T.tuile_2 == 1: 
            if T.couronne_2 == 1:
                image(champ1,pos2x,pos2y)
            else:
                image(champ0,pos2x,pos2y)
        #plaines
        if T.tuile_2 == 2:
            if T.couronne_2 == 1:
                image(plaine1,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(plaine2,pos2x,pos2y)
            else :
                image(plaine0,pos2x,pos2y)
        #oceans
        if T.tuile_2 == 3:
            if T.couronne_2 == 1:
                image(ocean1,pos2x,pos2y)
            else:
                image(ocean0,pos2x,pos2y)
        #marais
        if T.tuile_2 == 4:
            if T.couronne_2 == 1:
                image(marai1,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(marai2,pos2x,pos2y)
            else :
                image(marai0,pos2x,pos2y)
        #Forets
        if T.tuile_2 == 5:
            if T.couronne_2 == 1:
                image(foret1,pos2x,pos2y)
            else :
                image(foret0,pos2x,pos2y)
        #Mines
        if T.tuile_2 == 6:
            if T.couronne_2 == 1:
                image(mine1,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(mine2,pos2x,pos2y)
            elif T.couronne_2 == 3:
                image(mine3,pos2x,pos2y)
            else :
                image(mine0,pos2x,pos2y)
    
def DeroulementTour():
    clear()
    background(255,255,255)
    global boolJouer, LJ, j
    boolJouer = False
    if bool2Joueur:
        nb_generation = 4
        j = j % 2
    elif bool3Joueur:
        nb_generation = 3
        j = j % 3
    elif bool4Joueur:
        nb_generation = 4
        j = j % 4
    fill(color(0,0,0))
    textSize(20)
    textAlign(CENTER, CENTER)
    text("Joueur {a}".format(a = LJ[j].nom), 350, 25)
    List_Plateau = list()
    #Prend une tuile aleatoire
    for i in range(1, nb_generation+1):
        T = RTG.generate()
        List_Plateau.append(T)
        affiche_tuile(i,List_Plateau)
        print("la tuile {a} est : {b} {c} {d} {e}".format(a=T.numero,b=T.tuile_1,c=T.couronne_1,d=T.tuile_2,e=T.couronne_2))
    if RTG.taille - 1 < 0 or nb_tour == 0:
        fill(color(255,0,0))
        textSize(20)
        textAlign(CENTER, CENTER)
        text("Fin du Game", 300, 300)
    print("taille : {a}".format(a=len(List_Plateau)))
    
    print("taille : {a}".format(a=len(List_Plateau)))
    fill(color(0,0,0))
    textSize(20)
    for player in LJ :
        print("Joueur {a}".format(a = player.nom))
        textAlign(CENTER, CENTER)
        text("Joueur {a}".format(a = player.nom), 350, 400 + player.nom * 30)
    fill(color(0,0,0))
    textSize(20)
    textAlign(CENTER, CENTER)
    text("la tuile {a} est : {b} {c} {d} {e}".format(a=T.numero,b=T.tuile_1,c=T.couronne_1,d=T.tuile_2,e=T.couronne_2), 350, 350)


def setup():
    LC = ListCreator()
    global LT, RTG
    LT = LC.createList()
    RTG = RandomTileGenerator()
    for tile in LT :
        print("la tuile {a} est : {b} {c} {d} {e}".format(a=tile.numero,b=tile.tuile_1,c=tile.couronne_1,d=tile.tuile_2,e=tile.couronne_2))
    # The image file must be in the data folder of the current sketch
    # to load successfully
    size(700, 700)
    global imgMenue,ImgRegle1,ImgRegle2,ImgRegle3,ImgRegle4,fleche1,fleche2,croix,champ0,champ1,plaine0,plaine1,plaine2,ocean0,ocean1,mine0,mine1,mine2,mine3,marai0,marai1,marai2,foret0,foret1
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
    
    #-------------------------------------- Load img tuile --------------------------------------
    #Champs
    champ0 = loadImage("data/Champ.PNG")
    champ0.resize(60,60)
    champ1 = loadImage("data/Champcouronne.PNG")
    champ1.resize(60,60)
    #Plaines
    plaine0 = loadImage("data/Plaine.PNG")
    plaine0.resize(60,60)
    plaine1 = loadImage("data/Plaine1couronne.PNG")
    plaine1.resize(60,60)
    plaine2 = loadImage("data/Plaine2couronne.PNG")
    plaine2.resize(60,60)
    #Océan
    ocean0 = loadImage("data/Ocean.PNG")
    ocean0.resize(60,60)
    ocean1 = loadImage("data/Ocean1couronne.PNG")
    ocean1.resize(60,60)
    #Mines
    mine0 = loadImage("data/Mine.PNG")
    mine0.resize(60,60)
    mine1 = loadImage("data/Mine1couronne.PNG")
    mine1.resize(60,60)
    mine2 = loadImage("data/Mine2couronne.PNG")
    mine2.resize(60,60)
    mine3 = loadImage("data/Mine3couronne.PNG")
    mine3.resize(60,60)
    #Marais
    marai0 = loadImage("data/Marai.PNG")
    marai0.resize(60,60)
    marai1 = loadImage("data/Marai1couronne.PNG")
    marai1.resize(60,60)
    marai2 = loadImage("data/Marai2couronne.PNG")
    marai2.resize(60,60)
    #Forets
    foret0 = loadImage("data/Foret.PNG")
    foret0.resize(60,60)
    foret1 = loadImage("data/Foret1couronne.PNG")
    foret1.resize(60,60)
    
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
    global boolrelance, nb_tour, LJ
    if boolRegle:
        Regle()
    if boolMenu:
        Acceuil()
    if boolJouer:
        Jouer()
    if bool2Joueur and boolJouer:
        nb_tour = 5
        LC = Game(2)
        LJ = LC.createListJoueurs()
        DeroulementTour()
    if bool3Joueur and boolJouer:
        nb_tour = 11
        LC = Game(3)
        LJ = LC.createListJoueurs()
        DeroulementTour()
    if bool4Joueur and boolJouer:
        nb_tour = 11
        LC = Game(4)
        LJ = LC.createListJoueurs()
        DeroulementTour()
    if boolrelance :
        nb_tour = nb_tour - 1
        DeroulementTour()
        boolrelance = False
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
    global currentColor, boolQuitter, boolRegle, boolJouer, boolMenu, bool2Joueur, bool3Joueur, bool4Joueur,reglePrecOver, regleSuivOver,regleMenuOver,regleInt,boolrelance
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

def keyPressed():
    global boolrelance, j
    if key == 'a' and RTG.taille > 0 and nb_tour != 0:
        j = j + 1
        boolrelance = True
        print(boolrelance)       

def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height
