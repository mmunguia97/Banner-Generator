from PIL import Image, ImageDraw
import random


#############3#
# PREPARATION #
###############


# Randomly selects a background for the banner
def chooseBackground():
    randomBackground = random.randint(1, 6)
    backgroundColors = {1: ('red', 'thanks'),    2: ('blue', 'xmas'),
                        3: ('yellow', 'thanks'), 4: ('purple', 'scary'),
                        5: ('orange', 'scary'),  6: ('green', 'xmas')}

    return backgroundColors[randomBackground]


# Open the background from the 'backgrounds' directory 
def openBackground(color):
    return Image.open('backgrounds/' + color + '.jpg')


# Prepare the background for drawing
def prepareBackground(background):
    return ImageDraw.Draw(background)


##########
# WEAVES #
##########


# Decides whether or not to draw weaves along the edges
# as well as which edges and what style of weaves
def drawWeaves(draw, theme):
    # i is used to determine which side the program is considering
    for i in range(4):
        # 33% chance of no weave, 33% chance of arced, 33# of normal
        drawWeaves = random.randint(1, 9)
        if drawWeaves >= 4 and drawWeaves <= 6:
            if i == 0:
                draw = drawUpperWeave(draw, theme)
            elif i == 1:
                draw = drawRightWeave(draw, theme)
            elif i == 2:
                draw = drawLowerWeave(draw, theme)
            else:
                draw = drawLeftWeave(draw, theme)
        elif drawWeaves >= 7:
            if i == 0:
                draw = drawUpperArcedWeave(draw, theme)
            elif i == 1:
                draw = drawRightArcedWeave(draw, theme)
            elif i == 2:
                draw = drawLowerArcedWeave(draw, theme)
            else:
                draw = drawLeftArcedWeave(draw, theme)
        else:
            continue

    return draw


# Draws a weaved pattern at the top of the banner
def drawUpperWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    for i in range(8):
        draw.line(((576+(i*96)),162,(672+(i*96)),54),fill=weaveColor[0],width=5)
        draw.line(((576+(i*96)),54,(672+(i*96)),162),fill=weaveColor[1],width=5)

    return draw


# Draws a weaved pattern at the bottom of the banner
def drawLowerWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    for i in range(8):
        draw.line(((576+(i*96)),1026,(672+(i*96)),918),fill=weaveColor[0],width=5)
        draw.line(((576+(i*96)),918,(672+(i*96)),1026),fill=weaveColor[1],width=5)

    return draw


# Draws a weaved pattern on the left of the banner
def drawLeftWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    for i in range(8):
        draw.line((144,(324+(i*54)),240,(378+(i*54))),fill=weaveColor[0],width=5)
        draw.line((144,(378+(i*54)),240,(324+(i*54))),fill=weaveColor[1],width=3)

    return draw


# Draws a weaved pattern on the right of the banner
def drawRightWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    for i in range(8):
        draw.line((1680,(324+(i*54)),1776,(378+(i*54))),fill=weaveColor[0],width=5)
        draw.line((1680,(378+(i*54)),1776,(324+(i*54))),fill=weaveColor[1],width=3)

    return draw


# Draws an arced pattern at the top of the banner
def drawUpperArcedWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    draw.arc((576,54,672,162),270,90,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse(((576+(i*96)),54,(672+(i*96)),162),outline=weaveColor[i%2])
    draw.arc((1248,54,1344,162),90,270,fill=weaveColor[1])

    return draw


# Draws an arced pattern at the bottom of the banner
def drawLowerArcedWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    draw.arc((576,918,672,1026),270,90,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse(((576+(i*96)),918,(672+(i*96)),1026),outline=weaveColor[i%2])
    draw.arc((1248,918,1344,1026),90,270,fill=weaveColor[1])

    return draw


# Draws an arced pattern on the left of the banner
def drawLeftArcedWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    draw.arc((144,324,240,378),0,180,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse((144,(324+(i*54)),240,(378+(i*54))),outline=weaveColor[i%2])
    draw.arc((144,702,240,756),180,0,fill=weaveColor[1])

    return draw


# Draws an arced pattern on the right of the banner
def drawRightArcedWeave(draw, theme):
    weaveColor = getWeaveColor(theme)
    draw.arc((1680,324,1776,378),0,180,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse((1680,(324+(i*54)),1776,(378+(i*54))),outline=weaveColor[i%2])
    draw.arc((1680,702,1776,756),180,0,fill=weaveColor[1])

    return draw


# Return weave colors according to the banner theme
def getWeaveColor(theme):
    if theme == 'scary':
        return 'green', 'black'
    elif theme == 'xmas':
        return 'gold', 'red'
    elif theme == 'thanks':
        return 'green', 'blue'


#########
# GRIDS #
#########

# Decides whether or not to draw grids in the corners of the banner
# If so, which corners
def drawGrids(draw, theme):
    # i determines which corner the program is considering
    for i in range(4):
        # 50% chance to draw a grid in a given corner
        drawGrids = random.randint(1, 10)
        if drawGrids >= 6:
            if i == 0:
                draw = drawGridTopLeft(draw, theme)
            elif i == 1:
                draw = drawGridTopRight(draw, theme)
            elif i == 2:
                draw = drawGridBottomRight(draw, theme)
            else:
                draw = drawGridBottomLeft(draw, theme)
        else:
            continue

    return draw


# Draws a grid in the upper left corner
def drawGridTopLeft(draw, theme):
    weaveColor = getWeaveColor(theme)
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((0,(54*x),480,(54*x)),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((96*y),0,(96*y),270),fill=weaveColor[color],width=lineWidth)

    return draw


# Draws a grid in the upper right corner
def drawGridTopRight(draw, theme):
    weaveColor = getWeaveColor(theme)
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((1440,(54*x),1920,(54*x)),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((1920-(96*y)),0,(1920-(96*y)),270),fill=weaveColor[color],width=lineWidth)

    return draw


# Draws a grid in the bottom left corner
def drawGridBottomLeft(draw, theme):
    weaveColor = getWeaveColor(theme)
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((0,(1080-(54*x)),480,(1080-(54*x))),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((96*y),810,(96*y),1080),fill=weaveColor[color],width=lineWidth)

    return draw


# Draws a grid in the bottom right corner
def drawGridBottomRight(draw, theme):
    weaveColor = getWeaveColor(theme)
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((1440,(1080-(54*x)),1920,(1080-(54*x))),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((1920-(96*y)),810,(1920-(96*y)),1080),fill=weaveColor[color],width=lineWidth)

    return draw


##########
# CENTER #
##########


# Decides whether or not to surround the message with a shape
# If so, which shape
def drawCenterShape(draw, theme):
    # 33% chance of box, 33% chance ellipse, 33% chance of nothing
    drawCenter = random.randint(1,9)
    if drawCenter >= 7:
        draw = drawCenterEllipse(draw, theme)
    elif drawCenter <= 3:
        draw = drawCenterSquare(draw, theme)

    return draw


# Draw an ellipse in the center of the banner
def drawCenterEllipse(draw, theme):
    weaveColor = getWeaveColor(theme)
    color = random.randint(0, 1)
    draw.ellipse((576,216,1344,864),outline=weaveColor[color])

    return draw

# Draw a square in the center of the banner
def drawCenterSquare(draw, theme):
    weaveColor = getWeaveColor(theme)
    color = random.randint(0, 1)
    draw.rectangle((576,216,1344,864),outline=weaveColor[color])

    return draw


##########
# IMAGES #
##########


# Place the banner's message in the center
def placeCenterMessage(background, theme):
    randomMessage = str(random.randint(1, 3))
    print(f'{theme}/centertext/{randomMessage}.png')
    randomMessage = Image.open(theme + '/centertext/' + randomMessage + '.png')
    randomMessage = resizeImage(randomMessage, 640, 1)
    y = int((1080 - randomMessage.size[1]) / 2)
    background.paste(randomMessage, (640, y), randomMessage)
    randomMessage.close()

    return background


# Resize an image while preserving its aspect ratio and enforcing max size
# The banner's central message is not restricted in height
def resizeImage(image, desiredWidth, message=0):
    resizeRatio = (desiredWidth / float(image.size[0]))
    heightSize = int(float(image.size[1]) * float(resizeRatio))

    while heightSize > 270 and message == 0:
        desiredWidth -= 1
        resizeRatio = (desiredWidth / float(image.size[0]))
        heightSize = int(float(image.size[1]) * float(resizeRatio))

    return image.resize((desiredWidth, heightSize))


# Decides which corners to paste what images onto
def placeImages(background, theme):
    for i in range(4):
        # 30% chance of an image being placed in a corner
        placeImage = random.randint(1, 10)
        if placeImage >= 3:
            image = Image.open(chooseImage(theme))
            image = resizeImage(image, 384)
            if i == 0:
                background = placeImageTopLeft(background, image)
            elif i == 1:
                background = placeImageTopRight(background, image)
            elif i == 2:
                background = placeImageBottomLeft(background, image)
            else:
                background = placeImageBottomRight(background, image)

            image.close()

    return background


# Chooses a theme-appropriate image to be placed in the foreground
def chooseImage(theme):
    randomImage = str(random.randint(1, 10))
    print(f'{theme}/{randomImage}.png')
    return theme + '/' + randomImage + '.png'


def placeImageTopLeft(background, image):
    background.paste(image, (96, 54), image)
    return background


def placeImageTopRight(background, image):
    background.paste(image, (1440, 54), image)
    return background


def placeImageBottomLeft(background, image):
    background.paste(image, (96, 810), image)
    return background


def placeImageBottomRight(background, image):
    background.paste(image, (1440, 810), image)
    return background
