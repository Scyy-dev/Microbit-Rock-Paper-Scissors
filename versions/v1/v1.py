from microbit import *
import random

rock = Image("03330:"
             "36963:"
             "39993:"
             "36963:"
             "03330")

paper = Image("39993:"
              "09690:"
              "09690:"
              "09690:"
              "39993")

scissors = Image("99099:"
                 "99099:"
                 "00600:"
                 "06060:"
                 "60006")

shapes = [rock, paper, scissors]
image = random.choice(shapes)
display.show(image)
