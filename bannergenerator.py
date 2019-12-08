from PIL import Image, ImageDraw
import random, tweepy

#--------------------------------------#
#---------OAuth Authentication---------#
#--------------------------------------#

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# check if successful authentication
print("Account: " + api.me().name)

#--------------------------------------#
#---------Function Definitions---------#
#--------------------------------------#

# returns one of six backgrounds and its theme for the poster
def chooseBackground():
    randomBackground = random.randint(1,6)
    backgroundColors = {1: "red", 2: "blue", 3: "yellow",
                        4: "purple", 5: "orange", 6: "green"}
    posterThemes = {1: "thanks", 2: "xmas", 3: "thanks",
                    4: "scary", 5: "scary", 6: "xmas"}
    return backgroundColors[randomBackground], posterThemes[randomBackground]

# chooses a theme appropriate image to be placed in the foreground 
def chooseImage():
    randomImage = str(random.randint(1,10))
    print(theme + "/" + randomImage + ".png")
    return(theme + "/" + randomImage + ".png")

# resize image while preseriving its aspect ratio and enforcing a max size
# the banner's central messsage is not restricted in vertical size
def resizeImage(imageToResize,desiredWidth,message=0):
    resizeRatio = (desiredWidth/float(imageToResize.size[0]))
    heightSize = int(float(imageToResize.size[1])*float(resizeRatio))
    while (heightSize > 270) and (message == 0):
        desiredWidth-=1
        resizeRatio = (desiredWidth/float(imageToResize.size[0]))
        heightSize = int(float(imageToResize.size[1])*float(resizeRatio))
    return imageToResize.resize((desiredWidth,heightSize))

def placeImageTopLeft():
    background.paste(image,(96,54),image)

def placeImageTopRight():
    background.paste(image,(1440,54),image)

def placeImageBottomLeft():
    background.paste(image,(96,810),image)

def placeImageBottomRight():
    background.paste(image,(1440,810),image)

# creates a specified number of rows over the background with equal spacing
def drawRows(numberOfRows,lineWidth):
    for i in range (0, (numberOfRows-1)):
            draw.line((0,((1080/numberOfRows)*(i+1)),
                        1920,((1080/numberOfRows)*(i+1))),fill=128,width=lineWidth)

# creates a specified number of columns over the background with equal spacing
def drawColumns(numberOfColumns,lineWidth):
    for i in range (0, (numberOfColumns-1)):
        draw.line((((1920/numberOfColumns)*(i+1)),0,
                    ((1920/numberOfColumns)*(i+1)),1080),fill=128,width=lineWidth)

# draws lines over the background to visualize equally sized sections
def segmentBackground(numberOfRows,numberOfColumns,lineWidth=5):
    drawRows(numberOfRows,lineWidth)
    drawColumns(numberOfColumns,lineWidth)

# returns the stitch color depending on the banner's theme
def getWeaveColor():
    if theme == "scary":
        return "green", "black"
    elif theme == "xmas":
        return "gold", "red"
    elif theme == "thanks":
        return "green", "blue"

# draws an ellipse surrounding the center
def drawCenterEllipse():
    weaveColor = getWeaveColor()
    color = random.randint(0,1)
    draw.ellipse((576,216,1344,864),outline=weaveColor[color])

# draws a box around the center message
def drawCenterBox():
    weaveColor = getWeaveColor()
    color = random.randint(0,1)
    draw.rectangle((576,216,1344,864),outline=weaveColor[color])

# draws a weaved pattern at the top of the banner
def drawUpperWeave():
    weaveColor = getWeaveColor()
    for i in range(0,8):
        draw.line(((576+(i*96)),162,(672+(i*96)),54),fill=weaveColor[0],width=5)
        draw.line(((576+(i*96)),54,(672+(i*96)),162),fill=weaveColor[1],width=5)

# draws a weaved pattern at the bottom of the banner
def drawLowerWeave():
    weaveColor = getWeaveColor()
    for i in range(0,8):
        draw.line(((576+(i*96)),1026,(672+(i*96)),918),fill=weaveColor[0],width=5)
        draw.line(((576+(i*96)),918,(672+(i*96)),1026),fill=weaveColor[1],width=5)

# draws a weaved pattern at the left of the banner
def drawLeftWeave():
    weaveColor= getWeaveColor()
    for i in range(0,8):
        draw.line((144,(324+(i*54)),240,(378+(i*54))),fill=weaveColor[0],width=5)
        draw.line((144,(378+(i*54)),240,(324+(i*54))),fill=weaveColor[1],width=3)

# draws a weaved pattern at the right of the banner
def drawRightWeave():
    weaveColor = getWeaveColor()
    for i in range(0,8):
        draw.line((1680,(324+(i*54)),1776,(378+(i*54))),fill=weaveColor[0],width=5)
        draw.line((1680,(378+(i*54)),1776,(324+(i*54))),fill=weaveColor[1],width=3)

# draws an arced weaved pattern at the top of the banner
def drawUpperArcedWeave():
    weaveColor = getWeaveColor()
    draw.arc((576,54,672,162),270,90,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse(((576+(i*96)),54,(672+(i*96)),162),outline=weaveColor[i%2])
    draw.arc((1248,54,1344,162),90,270,fill=weaveColor[1])

# draws an arced weaved pattern at the bottom of the banner
def drawLowerArcedWeave():
    weaveColor = getWeaveColor()
    draw.arc((576,918,672,1026),270,90,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse(((576+(i*96)),918,(672+(i*96)),1026),outline=weaveColor[i%2])
    draw.arc((1248,918,1344,1026),90,270,fill=weaveColor[1])

# draws an arced weaved pattern at the left of the banner
def drawLeftArcedWeave():
    weaveColor = getWeaveColor()
    draw.arc((144,324,240,378),0,180,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse((144,(324+(i*54)),240,(378+(i*54))),outline=weaveColor[i%2])
    draw.arc((144,702,240,756),180,0,fill=weaveColor[1])

# draws an arced weaved pattern at the left of the banner
def drawRightArcedWeave():
    weaveColor = getWeaveColor()
    draw.arc((1680,324,1776,378),0,180,fill=weaveColor[0])
    for i in range(1,7):
        draw.ellipse((1680,(324+(i*54)),1776,(378+(i*54))),outline=weaveColor[i%2])
    draw.arc((1680,702,1776,756),180,0,fill=weaveColor[1])

# draws a grid in the top left corner
def drawGridTopLeft():
    weaveColor = getWeaveColor()
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((0,(54*x),480,(54*x)),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((96*y),0,(96*y),270),fill=weaveColor[color],width=lineWidth)

# draws a grid in the top right corner
def drawGridTopRight():
    weaveColor = getWeaveColor()
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((1440,(54*x),1920,(54*x)),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((1920-(96*y)),0,(1920-(96*y)),270),fill=weaveColor[color],width=lineWidth)

# draws a grid in the bottom left corner
def drawGridBottomLeft():
    weaveColor = getWeaveColor()
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((0,(1080-(54*x)),480,(1080-(54*x))),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((96*y),810,(96*y),1080),fill=weaveColor[color],width=lineWidth)

# draws a grid in the bottom right corner
def drawGridBottomRight():
    weaveColor = getWeaveColor()
    for x in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line((1440,(1080-(54*x)),1920,(1080-(54*x))),fill=weaveColor[color],width=lineWidth)
    for y in range(1,random.randint(2,5)):
        lineWidth = random.randint(1,2)
        color = random.randint(0,1)
        draw.line(((1920-(96*y)),810,(1920-(96*y)),1080),fill=weaveColor[color],width=lineWidth)

# places the banner's message in the center of the background
def placeCenterMessage():
    randomMessage = str(random.randint(1,3))
    print(theme + "/centertext/" + randomMessage + ".png")
    randomMessage = Image.open(theme + "/centertext/" + randomMessage + ".png")
    randomMessage = resizeImage(randomMessage,640,1)
    y = int((1080-randomMessage.size[1])/2)
    background.paste(randomMessage,(640,y),randomMessage)

#---------------------------------------#
#------------Creative Design------------#
#---------------------------------------#

# open the selected background image
color, theme = chooseBackground()
print("Color: " + color + ", Theme: " + theme)
background = Image.open("backgrounds/" + color + ".jpg")

# prepares the background to draw patterns
draw = ImageDraw.Draw(background)

# decides whether or not to draw weaves on the edges
# if so, which weaves on which edges
for i in range(0,4):
    drawWeaves = random.randint(1,10)
    if (drawWeaves >= 3) and (drawWeaves <= 6):
        if i == 0:
            drawUpperWeave()
        elif i == 1:
            drawRightWeave()
        elif i == 2:
            drawLowerWeave()
        else:
            drawLeftWeave()
    elif drawWeaves >= 7:
        if i == 0:
            drawUpperArcedWeave()
        elif i == 1:
            drawRightArcedWeave()
        elif i == 2:
            drawLowerArcedWeave()
        elif i == 3:
            drawLeftArcedWeave()

# decides whether or not to draw grids in the corners
# if so, which corners
for i in range(0,4):
    drawGrids = random.randint(1,10)
    if drawGrids >= 6:
        if i == 0:
            drawGridTopLeft()
        elif i == 1:
            drawGridTopRight()
        elif i == 2:
            drawGridBottomRight()
        else:
            drawGridBottomLeft()

# decides whether or not to surround the message with a shape
# if so, which shape
drawCenter = random.randint(0,10)
if (drawCenter >= 3) and (drawCenter <= 6):
    drawCenterBox()
elif drawCenter >= 7:
    drawCenterEllipse()

# place message in the center of the image
placeCenterMessage()

# decides which corners to paste images onto
for i in range (0,4):
    placeImages = random.randint(1,10)
    if placeImages >= 3:
        image = Image.open(chooseImage())
        image = resizeImage(image, 384)
        if i == 0:
            placeImageTopLeft()
        if i == 1:
            placeImageTopRight()
        if i == 2:
            placeImageBottomLeft()
        if i == 3:
            placeImageBottomRight()
        image.close()

# save the poster locally
background.save("background.jpg")

# upload the poster to twitter
api.update_with_media("background.jpg")

# opens the final poster for viewing
background.show()
