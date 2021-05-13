from helpers import *
import twitter


# Authenticate with Twitter API
api = twitter.authenticate()


# Open a random background
color, theme = chooseBackground()
print(f'Color: {color}, Theme: {theme}')
background = openBackground(color)

# Prepare background for drawing
draw = prepareBackground(background)

# Draws different weaves along the edges
draw = drawWeaves(draw, theme)

# Draws different grids in the corners
draw = drawGrids(draw, theme)

# Draw a shape in the center
draw = drawCenterShape(draw, theme)

# Place the banner's message in the center
background = placeCenterMessage(background, theme)

# Place images in different corners
background = placeImages(background, theme)

# Save a copy of the banner locally
background.save('background.jpg')

# Upload to Twitter
twitter.upload('background.jpg', api)

# View the final poster
background.show()
