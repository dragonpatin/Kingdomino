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
boolQuitter = boolRegle = boolJouer = bool2Joueur = bool3Joueur = bool4Joueur = bool3Joueur = bool4Joueur =  boolrelance = Tuile1 = Tuile2 = Tuile3 = Tuile4 = test  = False
AjouterTileJ = False
Tuile1NonUsed = Tuile2NonUsed = Tuile3NonUsed = Tuile4NonUsed = True 
boolMenu = initialisation = True
boolResize = True
regleInt = nb_tour = 0
LT = None
LJ = None
i = 0
j = 0 
L = list()
def Regle():
    updateRegle(mouseX, mouseY)
    global boolResize
    if regleInt == 0:
        image(ImgRegle1, 0, 0)
        image(fleche1, 600, 629)
        image(croix, 335, 665)
        if boolResize:
            this.surface.setSize(ImgRegle1.width, ImgRegle1.height)
            boolResize = False
            rect(regleX, regleY, 200, 50, 20)
            # rect(regleX,regleY,200,50,20)
    if regleInt == 1:
        image(ImgRegle2, 0, 0)
        image(fleche1, 600, 629)
        image(fleche2, 0, 629)
        image(croix, 335, 665)
        if boolResize:
            this.surface.setSize(ImgRegle2.width, ImgRegle2.height)
            boolResize = False
    if regleInt == 2:
        image(ImgRegle3, 0, 0)
        image(fleche1, 600, 629)
        image(fleche2, 0, 629)
        image(croix, 335, 665)
        if boolResize:
            this.surface.setSize(ImgRegle3.width, ImgRegle3.height)
            boolResize = False
    if regleInt == 3:
        image(ImgRegle4, 0, 0)
        image(fleche2, 0, 629)
        image(croix, 335, 665)
        if boolResize:
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
    rect(jouerX, jouerY, 200, 50, 20)
    if regleOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(regleX, regleY, 200, 50, 20)
    if quitterOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(quitterX, quitterY, 200, 50, 20)
    fill(color(255, 0, 0))
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
    rect(jouerX, jouerY, 200, 50, 20)
    if regleOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(regleX, regleY, 200, 50, 20)
    if quitterOver:
        fill(color(204))
    else:
        fill(color(255))
    rect(quitterX, quitterY, 200, 50, 20)
    fill(color(255, 0, 0))
    textSize(40)
    text("2 Joueurs", 255, 244)
    text("3 Joueurs", 255, 344)
    text("4 Joueurs", 255, 444)
    
def affiche_tuile(List_Plateau):
    #position tuiles
    # [(70,70)(130,70)]  [(220,70)(280,70)]  [(370,70)(430,70)]  [(520,70)(580,70)]
    i = 1
    pos1y = 70
    pos2y = 70
    #width,height
    for T in List_Plateau:
        if((i == 1 and Tuile1NonUsed) or (i == 2 and Tuile2NonUsed) or (i == 3 and Tuile3NonUsed) or (i == 4 and Tuile4NonUsed)):
            if bool3Joueur :
                pos1x = width * 0.09 + 0.33 * (i-1) * width
                pos2x = (width * 0.17 + 0.33 * (i-1) * width ) - 1
            else : 
                pos1x = width * 0.045 + 0.25 * (i-1) * width
                pos2x = (width * 0.125 + 0.25 * (i-1) * width ) - 1
            textSize(15)
            text("Tuile : {a}".format(a=T.numero),pos2x, 58)
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
                    image(marai1,pos1x,pos1y)
                elif T.couronne_1 == 2:
                    image(marai2,pos1x,pos1y)
                else :
                    image(marai0,pos1x,pos1y)
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
        i = i+1
        
def affiche_list_tile(player,i):
    for T in player.list_tuile :
        if i == 0:
            if bool2Joueur : 
                pos1x = width/4 - 100 + T.position_x*40 
                pos1y = width*0.08 + 70 + height*0.1 + T.position_y*40
            elif bool3Joueur:
                pos1x = width/6 - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1 + T.position_y*40
            else :
                pos1x = width/8 - 100 + T.position_x*40  
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if i == 1:
            if bool2Joueur : 
                pos1x = width/4 + width/2 *i- 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
            elif bool3Joueur:
                pos1x = width/6 + width/3 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
            else :
                pos1x = width/8 + width/4 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if i == 2:
            if bool3Joueur:
                pos1x = width/6 + width/3 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
            else :
                pos1x = width/8 + width/4 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if i == 3:
            pos1x = width/8 + width/4 *i - 100 + T.position_x*40
            pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if(T.orientation == 0):
            pos2y = pos1y
            pos2x = pos1x + 40
        if(T.orientation == 1):
            pos2x = pos1x
            pos2y = pos1y + 40
        if(T.orientation == 2):
            pos2y = pos1y
            pos2x = pos1x - 40
        if(T.orientation == 3):
            pos2x = pos1x
            pos2y = pos1y - 40
        # #Champs
        if T.tuile_1 == 1: 
            if T.couronne_1 == 1:
                image(champ1x40,pos1x,pos1y)
            else:
                image(champ0x40,pos1x,pos1y)
        #plaines
        if T.tuile_1 == 2:
            if T.couronne_1 == 1:
                image(plaine1x40,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(plaine2x40,pos1x,pos1y)
            else :
                image(plaine0x40,pos1x,pos1y)
        #oceans
        if T.tuile_1 == 3:
            if T.couronne_1 == 1:
                image(ocean1x40,pos1x,pos1y)
            else:
                image(ocean0x40,pos1x,pos1y)
        #marais
        if T.tuile_1 == 4:
            if T.couronne_1 == 1:
                image(marai1x40,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(marai2x40,pos1x,pos1y)
            else :
                image(marai0x40,pos1x,pos1y)
        #Forets
        if T.tuile_1 == 5:
            if T.couronne_1 == 1:
                image(foret1x40,pos1x,pos1y)
            else :
                image(foret0x40,pos1x,pos1y)
        #Mines
        if T.tuile_1 == 6:
            if T.couronne_1 == 1:
                image(mine1x40,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(mine2x40,pos1x,pos1y)
            elif T.couronne_1 == 3:
                image(mine3x40,pos1x,pos1y)
            else :
                image(mine0x40,pos1x,pos1y)
        #--------------------------- Tuile 2 -------------------
        #Champs
        if T.tuile_2 == 1: 
            if T.couronne_2 == 1:
                image(champ1x40,pos2x,pos2y)
            else:
                image(champ0x40,pos2x,pos2y)
        #plaines
        if T.tuile_2 == 2:
            if T.couronne_2 == 1:
                image(plaine1x40,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(plaine2x40,pos2x,pos2y)
            else :
                image(plaine0x40,pos2x,pos2y)
        #oceans
        if T.tuile_2 == 3:
            if T.couronne_2 == 1:
                image(ocean1x40,pos2x,pos2y)
            else:
                image(ocean0x40,pos2x,pos2y)
        #marais
        if T.tuile_2 == 4:
            if T.couronne_2 == 1:
                image(marai1x40,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(marai2x40,pos2x,pos2y)
            else :
                image(marai0x40,pos2x,pos2y)
        #Forets
        if T.tuile_2 == 5:
            if T.couronne_2 == 1:
                image(foret1x40,pos2x,pos2y)
            else :
                image(foret0x40,pos2x,pos2y)
        #Mines
        if T.tuile_2 == 6:
            if T.couronne_2 == 1:
                image(mine1x40,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(mine2x40,pos2x,pos2y)
            elif T.couronne_2 == 3:
                image(mine3x40,pos2x,pos2y)
            else :
                image(mine0x40,pos2x,pos2y)

def affiche_last_tile(player,i):
    if(player.lastTile!=None):
        T = player.lastTile
        if i == 0:
            if bool2Joueur : 
                pos1x = width/4 - 100 + T.position_x*40 
                pos1y = width*0.08 + 70 + height*0.1 + T.position_y*40
            elif bool3Joueur:
                pos1x = width/6 - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1 + T.position_y*40
            else :
                pos1x = width/8 - 100 + T.position_x*40  
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if i == 1:
            if bool2Joueur : 
                pos1x = width/4 + width/2 *i- 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
            elif bool3Joueur:
                pos1x = width/6 + width/3 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
            else :
                pos1x = width/8 + width/4 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if i == 2:
            if bool3Joueur:
                pos1x = width/6 + width/3 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
            else :
                pos1x = width/8 + width/4 *i - 100 + T.position_x*40
                pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if i == 3:
            pos1x = width/8 + width/4 *i - 100 + T.position_x*40
            pos1y = width*0.08 + 70 + height*0.1+ T.position_y*40
        if(T.orientation == 0):
            pos2y = pos1y
            pos2x = pos1x + 40
        if(T.orientation == 1):
            pos2x = pos1x
            pos2y = pos1y + 40
        if(T.orientation == 2):
            pos2y = pos1y
            pos2x = pos1x - 40
        if(T.orientation == 3):
            pos2x = pos1x
            pos2y = pos1y - 40
        # #Champs
        if T.tuile_1 == 1: 
            if T.couronne_1 == 1:
                image(champ1x40,pos1x,pos1y)
            else:
                image(champ0x40,pos1x,pos1y)
        #plaines
        if T.tuile_1 == 2:
            if T.couronne_1 == 1:
                image(plaine1x40,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(plaine2x40,pos1x,pos1y)
            else :
                image(plaine0x40,pos1x,pos1y)
        #oceans
        if T.tuile_1 == 3:
            if T.couronne_1 == 1:
                image(ocean1x40,pos1x,pos1y)
            else:
                image(ocean0x40,pos1x,pos1y)
        #marais
        if T.tuile_1 == 4:
            if T.couronne_1 == 1:
                image(marai1x40,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(marai2x40,pos1x,pos1y)
            else :
                image(marai0x40,pos1x,pos1y)
        #Forets
        if T.tuile_1 == 5:
            if T.couronne_1 == 1:
                image(foret1x40,pos1x,pos1y)
            else :
                image(foret0x40,pos1x,pos1y)
        #Mines
        if T.tuile_1 == 6:
            if T.couronne_1 == 1:
                image(mine1x40,pos1x,pos1y)
            elif T.couronne_1 == 2:
                image(mine2x40,pos1x,pos1y)
            elif T.couronne_1 == 3:
                image(mine3x40,pos1x,pos1y)
            else :
                image(mine0x40,pos1x,pos1y)
        #--------------------------- Tuile 2 -------------------
        #Champs
        if T.tuile_2 == 1: 
            if T.couronne_2 == 1:
                image(champ1x40,pos2x,pos2y)
            else:
                image(champ0x40,pos2x,pos2y)
        #plaines
        if T.tuile_2 == 2:
            if T.couronne_2 == 1:
                image(plaine1x40,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(plaine2x40,pos2x,pos2y)
            else :
                image(plaine0x40,pos2x,pos2y)
        #oceans
        if T.tuile_2 == 3:
            if T.couronne_2 == 1:
                image(ocean1x40,pos2x,pos2y)
            else:
                image(ocean0x40,pos2x,pos2y)
        #marais
        if T.tuile_2 == 4:
            if T.couronne_2 == 1:
                image(marai1x40,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(marai2x40,pos2x,pos2y)
            else :
                image(marai0x40,pos2x,pos2y)
        #Forets
        if T.tuile_2 == 5:
            if T.couronne_2 == 1:
                image(foret1x40,pos2x,pos2y)
            else :
                image(foret0x40,pos2x,pos2y)
        #Mines
        if T.tuile_2 == 6:
            if T.couronne_2 == 1:
                image(mine1x40,pos2x,pos2y)
            elif T.couronne_2 == 2:
                image(mine2x40,pos2x,pos2y)
            elif T.couronne_2 == 3:
                image(mine3x40,pos2x,pos2y)
            else :
                image(mine0x40,pos2x,pos2y)
    
def affiche_chateau(player,i):
    croix.resize(40,40)
    if i == 0:
        if bool2Joueur : 
            image(croix,width/4 - 100 + player.castle_x*40 ,width*0.08 + 70 + height*0.1 + player.castle_y*40)
        elif bool3Joueur:
            image(croix,width/6 - 100 + player.castle_x*40,width*0.08 + 70 + height*0.1 + player.castle_y*40)
        else :
            image(croix,width/8 - 100 + player.castle_x*40 ,width*0.08 + 70 + height*0.1+ player.castle_y*40)
    if i == 1:
        if bool2Joueur : 
            image(croix,width/4 + width/2 *i- 100 + player.castle_x*40,width*0.08 + 70 + height*0.1+ player.castle_y*40)
        elif bool3Joueur:
            image(croix,width/6 + width/3 *i - 100 + player.castle_x*40,width*0.08 + 70 + height*0.1+ player.castle_y*40)
        else :
            image(croix,width/8 + width/4 *i - 100 + player.castle_x*40,width*0.08 + 70 + height*0.1+ player.castle_y*40)
    if i == 2:
        if bool3Joueur:
            image(croix,width/6 + width/3 *i - 100 + player.castle_x*40,width*0.08 + 70 + height*0.1+ player.castle_y*40)
        else :
            image(croix,width/8 + width/4 *i - 100 + player.castle_x*40,width*0.08 + 70 + height*0.1+ player.castle_y*40)
    if i == 3:
        image(croix,width/8 + width/4 *i - 100 + player.castle_x*40,width*0.08 + 70 + height*0.1+ player.castle_y*40)


def affiche_joueur():
    if bool2Joueur :
        text("Joueur {a}".format(a=LJ[j%2].nom), int(width /2), 25)
    else : 
        text("Joueur {a}".format(a=LJ[j].nom), int(width /2), 25)
    for player in LJ :
        i = player.nom - 1
        affiche_chateau(player,i)
        affiche_last_tile(player,i)
        affiche_list_tile(player,i)
        if(i == 0) :
            textAlign(CENTER, CENTER)
            if bool2Joueur : 
                text("Joueur {a}".format(a = player.nom), width*0.25, width*0.08 + 70 + height*0.05)
            elif bool3Joueur:
                text("Joueur {a}".format(a = player.nom), width*0.165, width*0.08 + 70 + height*0.05)
            else :
                text("Joueur {a}".format(a = player.nom), width*0.125, width*0.08 + 70 + height*0.05)
        elif(i == 1) :
            textAlign(CENTER, CENTER)
            if bool2Joueur : 
                text("Joueur {a}".format(a = player.nom), width*0.75, width*0.08 + 70 + height*0.05)
            elif bool3Joueur:
                text("Joueur {a}".format(a = player.nom), width*0.165 + i * 0.33 * width, width*0.08 + 70 + height*0.05)
            else :
                text("Joueur {a}".format(a = player.nom), width*0.125 + i * 0.25 * width, width*0.08 + 70 + height*0.05)
        elif(i == 2) :
            textAlign(CENTER, CENTER)
            if bool3Joueur:
                text("Joueur {a}".format(a = player.nom), width*0.165 + i * 0.33 * width, width*0.08 + 70 + height*0.05)
            else :
                text("Joueur {a}".format(a = player.nom), width*0.125 + i * 0.25 * width, width*0.08 + 70 + height*0.05)
        elif(i == 3):
            textAlign(CENTER, CENTER)
            text("Joueur {a}".format(a = player.nom), width*0.125 + i * 0.25 * width, width*0.08 + 70 + height*0.05)
        i += 1
def affichePlateau(List_Plateau):
    affiche_tuile(List_Plateau)
    affiche_joueur();
    if RTG.taille - 1 < 0 or nb_tour == 0:
        fill(color(255, 0, 0))
        textSize(15)
        textAlign(CENTER, CENTER)
        text("Fin du Game", 300, 300)
    fill(color(0,0,0))
    textSize(15)
    textAlign(CENTER, CENTER)

    
def inserer(T,L):
    L.append(0)
    k = len(L)-2
    while k >= 0 and L[k].numero >= T.numero:
        L[k+1] = L[k]
        k = k - 1

    L[k+1] = T
    return L

def loadTuilex40():
    global champ0x40, champ1x40, plaine0x40, plaine1x40, plaine2x40, ocean0x40, ocean1x40, mine0x40, mine1x40, mine2x40, mine3x40, marai0x40, marai1x40, marai2x40, foret0x40, foret1x40

#-------------------------------------- Load img tuile -------------------
    # Champs
    champ0x40 = loadImage("data/Champ.PNG")
    champ0x40.resize(40, 40)
    champ1x40 = loadImage("data/Champcouronne.PNG")
    champ1x40.resize(40, 40)
    # Plaines
    plaine0x40 = loadImage("data/Plaine.PNG")
    plaine0x40.resize(40, 40)
    plaine1x40 = loadImage("data/Plaine1couronne.PNG")
    plaine1x40.resize(40, 40)
    plaine2x40 = loadImage("data/Plaine2couronne.PNG")
    plaine2x40.resize(40, 40)
    # Océan
    ocean0x40 =loadImage("data/Ocean.PNG")
    ocean0x40.resize(40, 40)
    ocean1x40 = loadImage("data/Ocean1couronne.PNG")
    ocean1x40.resize(40, 40)
    # Mines
    mine0x40 = loadImage("data/Mine.PNG")
    mine0x40.resize(40, 40)
    mine1x40 = loadImage("data/Mine1couronne.PNG")
    mine1x40.resize(40, 40)
    mine2x40 = loadImage("data/Mine2couronne.PNG")
    mine2x40.resize(40, 40)
    mine3x40 =loadImage("data/Mine3couronne.PNG")
    mine3x40.resize(40, 40)
    # Marais
    marai0x40 = loadImage("data/Marai.PNG")
    marai0x40.resize(40, 40)
    marai1x40 = loadImage("data/Marai1couronne.PNG")
    marai1x40.resize(40, 40)
    marai2x40 = loadImage("data/Marai2couronne.PNG")
    marai2x40.resize(40, 40)
    # Forets
    foret0x40 = loadImage("data/Foret.PNG")
    foret0x40.resize(40, 40)
    foret1x40 = loadImage("data/Foret1couronne.PNG")
    foret1x40.resize(40, 40)

def loadTuile(boolResize):
    global champ0, champ1, plaine0, plaine1, plaine2, ocean0, ocean1, mine0, mine1, mine2, mine3, marai0, marai1, marai2, foret0, foret1
    if boolResize :
        taillex1 = int( width * 0.08)
    else :
        taillex1 = int( displayWidth * 0.08)
    print(taillex1)
    #-------------------------------------- Load img tuile -------------------
    # Champs
    champ0 = loadImage("data/Champ.PNG")
    champ0.resize(taillex1, taillex1)
    champ1 = loadImage("data/Champcouronne.PNG")
    champ1.resize(taillex1, taillex1)
    # Plaines
    plaine0 = loadImage("data/Plaine.PNG")
    plaine0.resize(taillex1, taillex1)
    plaine1 = loadImage("data/Plaine1couronne.PNG")
    plaine1.resize(taillex1, taillex1)
    plaine2 = loadImage("data/Plaine2couronne.PNG")
    plaine2.resize(taillex1, taillex1)
    # Océan
    ocean0 = loadImage("data/Ocean.PNG")
    ocean0.resize(taillex1,taillex1)
    ocean1 = loadImage("data/Ocean1couronne.PNG")
    ocean1.resize(taillex1, taillex1)
    # Mines
    mine0 = loadImage("data/Mine.PNG")
    mine0.resize(taillex1, taillex1)
    mine1 = loadImage("data/Mine1couronne.PNG")
    mine1.resize(taillex1, taillex1)
    mine2 = loadImage("data/Mine2couronne.PNG")
    mine2.resize(taillex1, taillex1)
    mine3 = loadImage("data/Mine3couronne.PNG")
    mine3.resize(taillex1, taillex1)
    # Marais
    marai0 = loadImage("data/Marai.PNG")
    marai0.resize(taillex1,taillex1)
    marai1 = loadImage("data/Marai1couronne.PNG")
    marai1.resize(taillex1, taillex1)
    marai2 = loadImage("data/Marai2couronne.PNG")
    marai2.resize(taillex1, taillex1)
    # Forets
    foret0 = loadImage("data/Foret.PNG")
    foret0.resize(taillex1, taillex1)
    foret1 = loadImage("data/Foret1couronne.PNG")
    foret1.resize(taillex1, taillex1)

def DeroulementTour():
    background(255, 255, 255)
    global LJ, j
    if bool2Joueur:
        nb_generation = 4
    elif bool3Joueur:
        nb_generation = 3
    elif bool4Joueur:
        nb_generation = 4
    #fill(color(0, 0, 0))
    #textSize(20)
    #textAlign(CENTER, CENTER)
    #text("Joueur {a}".format(a=LJ[j].nom), 350, 25)
    List_Plateau = list()
    # Prend une tuile aleatoire
    for i in range(1, nb_generation + 1):
        T = RTG.generate()
        inserer(T, List_Plateau)
        print("la tuile {a} est : {b} {c} {d} {e}".format(a=T.numero,b=T.tuile_1,c=T.couronne_1,d=T.tuile_2,e=T.couronne_2))
    if RTG.taille - 1 < 0 or nb_tour == 0:
        fill(color(255, 0, 0))
        textSize(20)
        textAlign(CENTER, CENTER)
        text("Fin du Game", 300, 300)
        fill(color(0, 0, 0))
    for player in LJ :
        print("Joueur {a}".format(a = player.nom))
        textAlign(CENTER, CENTER)
        text("Joueur {a}".format(a = player.nom), 350, 400 + player.nom * 30)
    return List_Plateau

def resizeTuile(force):
    global sizeSave_x
    if not(sizeSave_x == width) and not(force):
        loadTuile(True)
        sizeSave_x = displayWidth
        
def setup():
    LC = ListCreator()
    global LT, RTG
    LT = LC.createList()
    RTG = RandomTileGenerator()
    for tile in LT:
        print("la tuile {a} est : {b} {c} {d} {e}".format(
            a=tile.numero, b=tile.tuile_1, c=tile.couronne_1, d=tile.tuile_2, e=tile.couronne_2))
    # The image file must be in the data folder of the current sketch
    # to load successfully
    size(700, 700)
    global imgMenue, ImgRegle1, ImgRegle2, ImgRegle3, ImgRegle4, fleche1, fleche2, croix, champ0, champ1, plaine0, plaine1, plaine2, ocean0, ocean1, mine0, mine1, mine2, mine3, marai0, marai1, marai2, foret0, foret1, champ0x40, champ1x40, plaine0x40, plaine1x40, plaine2x40, ocean0x40, ocean1x40, mine0x40, mine1x40, mine2x40, mine3x40, marai0x40, marai1x40, marai2x40, foret0x40, foret1x40
    # Load the image into the program
    imgMenue = loadImage("data/Kingdomino.png")
    imgMenue.resize(700, 700)
    ImgRegle1 = loadImage("data/Help1.PNG")
    ImgRegle1.resize(700, 700)
    ImgRegle2 = loadImage("data/Help2.PNG")
    ImgRegle2.resize(700, 700)
    ImgRegle3 = loadImage("data/Help3.PNG")
    ImgRegle3.resize(700, 700)
    ImgRegle4 = loadImage("data/Help4.PNG")
    ImgRegle4.resize(700, 700)
    fleche1 = loadImage("data/flechedroite.png")
    fleche1.resize(100, 100)
    fleche2 = loadImage("data/flechegauche.png")
    fleche2.resize(100, 100)
    croix = loadImage("data/multiply.png")
    croix.resize(25, 25)
    global sizeSave_x
    sizeSave_x = displayWidth
    loadTuile(False)
    loadTuilex40()
    global jouerX, jouerY, regleX, regleY, quitterX, quitterY
    jouerX = width / 2 - rectSize - 10
    jouerY = (height - 200) / 2 - rectSize / 2
    regleX = width / 2 - rectSize - 10
    regleY = (height) / 2 - rectSize / 2
    quitterX = width / 2 - rectSize - 10
    quitterY = (height + 200) / 2 - rectSize / 2
    ellipseMode(CENTER)
    frameRate(fps)
    this.surface.setResizable(True)

def draw():
    background(255, 255, 255)
    global boolrelance, nb_tour, LJ,test,L,initialisation
    if boolRegle:
        Regle()
    if boolMenu:
        Acceuil()
    if boolJouer:
        if bool2Joueur:
            if initialisation:
                nb_tour = 5
                LC = Game(2)
                LJ = LC.createListJoueurs()
                L = DeroulementTour()
                initialisation=False
                this.surface.setSize(displayWidth,displayHeight)
                resizeTuile(True)
            else : 
                resizeTuile(False)
            updateJouer2_4(mouseX,mouseY)
            affichePlateau(L)
        elif bool3Joueur:
            if initialisation:
                nb_tour = 11
                LC = Game(3)
                LJ = LC.createListJoueurs()
                L = DeroulementTour()
                initialisation=False
                this.surface.setSize(displayWidth,displayHeight)
                resizeTuile(True)
            else :
                resizeTuile(False)
            updateJouer3(mouseX,mouseY)
            affichePlateau(L)
        elif bool4Joueur:
            if initialisation:
                nb_tour = 11
                LC = Game(4)
                LJ = LC.createListJoueurs()
                L = DeroulementTour()
                initialisation=False
                this.surface.setSize(displayWidth,displayHeight)
                resizeTuile(True)
            else:
                resizeTuile(False)
            updateJouer2_4(mouseX,mouseY)
            affichePlateau(L)
            
        else : 
            Jouer()
    if boolrelance :
        nb_tour = nb_tour - 1
        L = DeroulementTour()
        affiche_tuile(L)
        boolrelance = False
    if boolQuitter:
        exit()


def update(x, y):
    global jouerOver, regleOver, quitterOver, Joueur2Over, Joueur3Over, Joueur4Over, tuile1Over, tuile2Over, tuile3Over, tuile4Over
    jouerOver = Joueur2Over = overRect(jouerX, jouerY, 200, 50)
    regleOver = Joueur3Over = overRect(regleX, regleY, 200, 50)
    quitterOver = Joueur4Over = overRect(quitterX, quitterY, 200, 50)

def updateRegle(x, y):
    global reglePrecOver, regleSuivOver, regleMenuOver
    reglePrecOver = overRect(0, 629, 100, 100)
    regleSuivOver = overRect(600, 629, 100, 100)
    regleMenuOver = overRect(335, 665, 25, 25)
    
def updateJouer2_4(x, y):
    global Tuile1, Tuile2,Tuile3,Tuile4
    Tuile1 = overRect(width * 0.045 + 0.25 * 0 * width, 70,  2 * int(width*0.08), int(width*0.08))
    Tuile2 = overRect(width * 0.045 + 0.25 * 1 * width, 70,  2 * int(width*0.08), int(width*0.08))
    Tuile3 = overRect(width * 0.045 + 0.25 * 2 * width, 70,  2 * int(width*0.08), int(width*0.08))
    Tuile4 = overRect(width * 0.045 + 0.25 * 3 * width, 70,  2 * int(width*0.08), int(width*0.08))
  
def updateJouer3(x, y):
    global Tuile1, Tuile2,Tuile3
    Tuile1 = overRect(width * 0.09 + 0.33 * 0 * width, 70, 2 * int(width*0.08), int(width*0.08))
    Tuile2 = overRect(width * 0.09 + 0.33 * 1 * width, 70, 2 * int(width*0.08), int(width*0.08))
    Tuile3 = overRect(width * 0.09 + 0.33 * 2 * width, 70, 2 * int(width*0.08), int(width*0.08))
  
def tourSuivant():
    global boolrelance, test,Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed
    Tuile1NonUsed = Tuile2NonUsed = Tuile3NonUsed = Tuile4NonUsed = True
    if RTG.taille > 0 and nb_tour != 0:
        test = True
        boolrelance = True

def mousePressed():
    global currentColor, boolQuitter, boolRegle, boolJouer, boolMenu, bool2Joueur, bool3Joueur, bool4Joueur, reglePrecOver, regleSuivOver, regleMenuOver, regleInt, boolrelance,j
    global Tuile1NonUsed,Tuile2NonUsed,Tuile3NonUsed,Tuile4NonUsed,AjouterTileJ
    ###Faire Fonction chaque if.
    if boolJouer:
        print(j)
        if Joueur2Over and (AjouterTileJ == False):
            currentColor = regleColor
            bool2Joueur = True
            if Tuile1 and Tuile1NonUsed:
                LJ[j%2].setLastTile(L[0])
                j = (j+1) % 4
                Tuile1NonUsed = False
                AjouterTileJ = True
            if Tuile2 and Tuile2NonUsed:
                LJ[j%2].setLastTile(L[1])
                j = (j+1) % 4
                Tuile2NonUsed = False
                AjouterTileJ = True
            if Tuile3 and Tuile3NonUsed:
                LJ[j%2].setLastTile(L[2])
                j = (j+1) % 4
                Tuile3NonUsed = False
                AjouterTileJ = True
            if Tuile4 and Tuile4NonUsed:
                LJ[j%2].setLastTile(L[3])
                j = (j+1) % 4
                Tuile4NonUsed = False
                AjouterTileJ = True
                
                
        if Joueur3Over and (AjouterTileJ == False) :
            currentColor = regleColor
            bool3Joueur = True
            if Tuile1 and Tuile1NonUsed:
                LJ[j].setLastTile(L[0])
                j = (j+1) % 3
                Tuile1NonUsed = False
                AjouterTileJ = True
            if Tuile2 and Tuile2NonUsed:
                LJ[j].setLastTile(L[1])
                j = (j+1) % 3
                Tuile2NonUsed = False
                AjouterTileJ = True
            if Tuile3 and Tuile3NonUsed:
                LJ[j].setLastTile(L[2])
                j = (j+1) % 3
                Tuile3NonUsed = False
                AjouterTileJ = True
                
        if Joueur4Over and (AjouterTileJ == False) :
            currentColor = regleColor
            bool4Joueur = True
            print(j)
            if Tuile1 and Tuile1NonUsed:
                LJ[j].setLastTile(L[0])
                j = (j+1) % 4
                Tuile1NonUsed = False
                AjouterTileJ = True
            if Tuile2 and Tuile2NonUsed:
                LJ[j].setLastTile(L[1])
                j = (j+1) % 4
                Tuile2NonUsed = False
                AjouterTileJ = True
            if Tuile3 and Tuile3NonUsed:
                LJ[j].setLastTile(L[2])
                j = (j+1) % 4
                Tuile3NonUsed = False
                AjouterTileJ = True
            if Tuile4 and Tuile4NonUsed:
                LJ[j].setLastTile(L[3])
                j = (j+1) % 4
                Tuile4NonUsed = False
                AjouterTileJ = True
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
            if not(regleInt == 3):
                regleInt += 1
        if reglePrecOver:
            if not(regleInt == 0):
                regleInt -= 1
        if regleMenuOver:
            regleMenuOver = False
            boolMenu = True
            boolRegle = False

def keyPressed():
    global boolrelance, test,AjouterTileJ,LJ
    if bool3Joueur:
        i = (j-1)%3
    if bool4Joueur:
        i = (j-1)%4
    if bool2Joueur:
        i = (j-1)%2
    if AjouterTileJ :
        if keyCode == LEFT:
            print(1)
            LJ[i].tileLeft()
        if keyCode == RIGHT:
            LJ[i].tileRight()
        if keyCode == UP:
            LJ[i].tileUp()
        if keyCode == DOWN:
            LJ[i].tileDown()
        if keyCode == CONTROL:
            LJ[i].tileOrientation()
        if key == ENTER:
            LJ[i].list_tuile.append(LJ[i].lastTile)
            LJ[i].lastTile = None
            AjouterTileJ = False
            if j == 0:
                    tourSuivant()

def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height
