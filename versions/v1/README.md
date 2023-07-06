# Objective

This version will explore a more creative side to create art on the 5x5 display. While the game itself is restricted
to 'rock', 'paper' and 'scissors', there should be no limit to the images created using the Micro:bit.

# Line-by-line Explanation

### Important Libraries

Before we can begin our rock paper scissors adventure, we'll need to make sure our code works with the Micro:bit and add
a needed library to make our game work as well.

```python
from microbit import *
import random
```

### Game Basics

Instead of letting the player choose their option, we're going to randomise it for them. This is because the device only
has 2 buttons, and it gets complicated fast to try and wrap 3 options into 2 buttons. The most feasible way forward if
we wanted to let them choose would be to make the 3rd option be pressing both buttons at the same time. However, this
will lead to either complex code to track how each button is pressed, lead to delays between actions, or create a really
obvious way for players to tell what their opponent will pick. In all cases, it's much easier to let the Micro:bit do
the hard work and have the player rely on luck to get the win.

### Get Creative

Now that we understand how our game will flow, we need to think about how we tell the player what they got. There are 3
options - rock, paper, and scissors.

The hard thing is that we only have a 5x5 pixel display, and can only change the brightness. We have to model something
that is obvious to the player is a particular shape.

This is a great opportunity to get creative - try researching pixel art and see if you can find anything that will be
convincing, or use it as a guide and scale it down.

To create your shape, you'll need to create an `Image` using a particular format. The following example is a circle:

```python
circle = Image("03330:"
               "36963:"
               "39993:"
               "36963:"
               "03330")
```

Before reading any further - give it a shot and see how you go. My recommendation to get started is scissors - there's a
pixel shape out there that already sorta looks like scissors!

### The Art - Scissors

These scissors are inspired from shears - they definitely aren't great, but it's still clear that they're scissors.

```python
scissors = Image("06060:"
                 "06060:"
                 "06060:"
                 "99699:"
                 "99099")
```

These scissors come from the 'x' shape, and I then added a handle to them. This is definitely my preferred pair of
scissors.

```python
scissors = Image("99099:"
                 "99099:"
                 "00600:"
                 "06060:"
                 "60006")
```

### The Art - Paper

This piece of paper is simple, but effective. Can't go wrong with a square piece of paper.

```python
paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")
```

This piece of paper is actually more like a scroll - a very different approach, but distinct and I think I did alright!

```python
paper = Image("39993:"
              "09690:"
              "09690:"
              "09690:"
              "39993")
```

### The Art - Rock

This rock is also simple, but effective. Diamonds are definitely a rock!

```python
rock = Image("00900:"
             "09090:"
             "90009:"
             "09090:"
             "00900")
```

This rock is sorta like a sphere. It's a bit too smooth and abstract to be a 'rock', but I did what I could with a 5x5
space.

```python
rock = Image("03330:"
             "36963:"
             "39993:"
             "36963:"
             "03330")
```

### Randomising the Shapes

Now we've got our shapes, it's time to add our 'random' element and get our rock, paper or scissors chosen!

We do this by putting *all* of our shapes into a list, and then randomly picking an item from that list.

```python
shapes = [rock, paper, scissors]
image = random.choice(shapes)
```

### Finishing it off

Now we've got our randomly chosen shape (our rock, paper or scissors!) we need to display what got chosen. Remove
any `display.show()` lines left and add one at the end, so only our randomly chosen shape is shown!

```python
display.show(image)
```

# Next Version

Great! We've added a way to randomly pick rock, paper scissors. We've also added a really cool image to represent each
of the shapes. You can see the full code [here](./v1.py)

The next version will add an animation to make the coin flip a bit more interesting. You can access
that [here](../v2/README.md)