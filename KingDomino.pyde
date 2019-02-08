circleSize = 93
circleOver = False
 
def setup():
    size(888, 900)
    # The image file must be in the data folder of the current sketch
    # to load successfully
    global img
    img = loadImage("data/Kingdomino.png")    # Load the image into the program
    global circleX, circleY, i 
    circleX = width / 2 + circleSize / 2 + 10
    circleY = height / 2
    i = 0
    ellipseMode(CENTER)

def draw():
    # Displays the image at its actual size at point (0,0)
    image(img, 0, 0)
    ellipse(circleX, circleY, circleSize, circleSize)


def mousePressed():
    print(i)
    global currentColor
    if circleOver: 
        currentColor = circleColor
        
        
        
def update(x, y):
    global circleOver, rectOver
    circleOver = overCircle(circleX, circleY, circleSize)
    
def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height


def overCircle(x, y, diameter):
    distance = dist(x, y, mouseX, mouseY)
    return distance < diameter / 2
