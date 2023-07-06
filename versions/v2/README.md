# Objective

This version makes the random choice replayable whenever the Micro:bit is shaken.

# Line-by-line Explanation

### Shake it up!

A cool feature about Micro:bits is the accelerometer. It detects when the Micro:bit is moving!

We're going to use this to our advantage by using it to detect whenever the Micro:bit is shaken.

To do this, we need to check if the accelerometer detected a particular type of movement, called a 'gesture'. The
gesture we're after is 'shake'.

Since we want our random choice to happen every time the Micro:bit is shaken, we'll put all of the random choice and
display logic into an if statement.

```python
if accelerometer.was_gesture("shake"):
    shapes = [rock, paper, scissors]
    image = random.choice(shapes)
    display.show(image)
```

...but that doesn't quite work. When we run this code and shake the Micro:bit, nothing happens! If you've done
the [Coin Flip](https://github.com/Scyy-dev/Microbit-Coin-Flip) activity, you might recognise this problem.

### To Infinity!

For our shaking to work, we need to check if the device is being shaken, *forever*. So, we wrap it all up inside an
infinite loop and try it again!

```python
while True:
    if accelerometer.was_gesture("shake"):
        shapes = [rock, paper, scissors]
        image = random.choice(shapes)
        display.show(image)
```

Yay! That works now. It's a bit awkward to use because sometimes the image changes really fast, so we're going to try
and fix that.

### Slowing it all down

Now we've got our image being shown, we want the time to actually see it being displayed before it changes to a new one.
So we're going to just pause the Micro:bit for a few seconds so our player gets to see what they got. We'll then also
clear the display so they know it's ready to be shaken again!

```python
display.show(image)
sleep(2000)
display.clear()
```

# Further Challenges

Great job for making it this far! If you've managed to get everything working up to this point, you should have a rock
paper scissors chooser that runs every time you shake the Micro:bit.

If you got stuck, you can see the full code [here](./v2.py)

For an extra challenge - try adding an animation! There's a great starter guide on animations available in v3 of
the [Coin Flip](https://github.com/Scyy-dev/Microbit-Coin-Flip) activity.
