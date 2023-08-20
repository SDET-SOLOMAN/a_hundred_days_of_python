###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from random import choice
from turtle import Turtle, Screen

# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('sweet_pic.jpg', 6)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

rgb_colors = []
colors = colorgram.extract('image.jpg', 50)

for color in colors:
    new_color = (color.rgb[0:])
    rgb_colors.append(new_color)

sdet_soloman = Turtle('turtle')
sdet_soloman.speed(4)
sdet_soloman.penup()
sdet_soloman.setposition(-340, -300)
sdet_soloman.shapesize(2)

screen = Screen()
screen.colormode(255)

for char in range(0, 13):

    for num in range(0, 12):
        sdet_soloman.color(choice(rgb_colors))
        sdet_soloman.stamp()
        sdet_soloman.forward(60)

    sdet_soloman.setposition(-340, sdet_soloman.ycor() + 50)



screen.exitonclick()
