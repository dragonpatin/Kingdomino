<<<<<<< HEAD
rectSize = 90
jouerOver = regleOver = quitterOver = Joueur1Over = Joueur2Over = Joueur4Over = False
regleColor = color(255)
jouerColor = color(255)
quitterColor = color(255)
fps = 30
boolQuitter = boolRegle = boolJouer = bool2Joueur = bool3Joueur = bool4Joueur = bool2Joueur = bool3Joueur = bool4Joueur = False
boolMenu = True
boolResize = True
regleInt = 0
def Regle():
    global boolResize
    if regleInt == 0:
        image(ImgRegle1, 0, 0)
        if boolResize :
            this.surface.setSize(ImgRegle1.width, ImgRegle1.height)
            boolResize = False
    if regleInt == 2:
        image(ImgRegle2, 0, 0)
        if boolResize :
            this.surface.setSize(ImgRegle2.width, ImgRegle2.height)
            boolResize = False
    if regleInt == 3:
        image(ImgRegle3, 0, 0)
        if boolResize :
            this.surface.setSize(ImgRegle3.width, ImgRegle3.height)
            boolResize = False
    if regleInt == 4:
        image(ImgRegle4, 0, 0)
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
    text("Jouer", 400, 342) 
    text("Regle", 390, 442) 
    text("Quitter", 380, 542)
    
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
    text("2 Joueurs", 355, 344) 
    text("3 Joueurs", 355, 444) 
    text("4 Joueurs", 355, 544)

=======
from ListCreator import *

circleSize = 93
circleOver = False

circleOve= False
 
>>>>>>> c0f429bf9b08a59ce3cc95ee398837797739a2e2
def setup():
    LC = ListCreator()
    LT = LC.createList()
    for tile in LT :
        print("la tuile {a} est : {b} {c} {d} {e}".format(a=tile.numero,b=tile.tuile_1,c=tile.couronne_1,d=tile.tuile_2,e=tile.couronne_2))
    size(888, 900)
    # The image file must be in the data folder of the current sketch
    # to load successfully
    global imgMenue,ImgRegle1,ImgRegle2,ImgRegle3,ImgRegle4
    imgMenue = loadImage("data/Kingdomino.png")    # Load the image into the program
    ImgRegle1 = loadImage("data/Help1.PNG")
    ImgRegle2 = loadImage("data/Help2.PNG")
    ImgRegle3 = loadImage("data/Help3.PNG")
    ImgRegle4 = loadImage("data/Help4.PNG")
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

<<<<<<< HEAD
def draw():
    if boolRegle:
        Regle()
    if boolMenu:
        Acceuil()
    if boolJouer:
        Jouer()
    if boolQuitter:
        exit()
          
def update(x, y):
    global jouerOver, regleOver, quitterOver, Joueur2Over, Joueur3Over, Joueur4Over
    jouerOver = Joueur2Over = overRect(jouerX, jouerY, 200, 50)
    regleOver = Joueur3Over = overRect(regleX, regleY, 200, 50)
    quitterOver = Joueur4Over = overRect(quitterX, quitterY, 200, 50)

def updateRegle(x, y):
    global reglePrecOver, regleSuivOver,regleMenuOver
    reglePrecOver = overRect(jouerX, jouerY, 200, 50)
    regleSuivOver = overRect(regleX, regleY, 200, 50)
    regleMenuOver = overRect(quitterX, quitterY, 200, 50)
    
def mousePressed():ra
    global currentColor, boolQuitter, boolRegle, boolJouer, boolMenu, bool2Joueur, bool3Joueur, bool4Joueur
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

def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height
=======
def draw() :
   # Displays the image at its actual size at point (0,0)
    image(img, 0, 0)
    ellipse(circleX, circleY, circleSize, circleSize)


def mousePressed():
    print(i)
    global currentColor
    if circleOver: 
        currentColor = circleColor
        
        
        
#def update(x, y):
#    global circleOver, rectOver
#    circleOver = overCircle(circleX, circleY, circleSize)
    
#def overRect(x, y, width, height):
#    return x <= mouseX <= x + width and y <= mouseY <= y + height


#def overCircle(x, y, diameter):
#    distance = dist(x, y, mouseX, mouseY)
#    return distance < diameter / 2
>>>>>>> c0f429bf9b08a59ce3cc95ee398837797739a2e2
