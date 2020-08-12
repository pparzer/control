#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Control Task"""

from psychopy import visual, core, event, gui
import random, time, os

# configuration variables
totalTime = 60          # duration of the task
switchTime = 20         # time when to reverse mouse effect (only difficult version)
dataStep = 0.1          # intervals for saving data
smooth = 0.99           # smoothing of the random walk
instructionText = u"""
Use the mouse to keep the red dot as close as possible to the center of the cross.

You can interrupt the task by pressing the ESC key.

Press any key to start."""

# get ID and task version
info = {'ID':'', 'Version':['easy', 'difficult']}
infoDlg = gui.DlgFromDict(dictionary=info, 
    title='Control Task', 
    order=['ID', 'Version'])

if not infoDlg.OK:
    core.quit()
    
# for easy version set switchTime to a time > totalTime,
# thus preventing the reverse of the mouse effect
if info['Version'] == 'easy':
    switchTime = totalTime + 1

# create filename from subject ID and timestamp of experiment 
if not os.path.isdir("data"):
    os.mkdir("data")
dataFile = 'data/' + info['ID'] + '.csv'
f = open(dataFile, 'w')
f.write('time,mouse_x,mouse_y,noise_x,noise_y,target_x,target_y,reverse\n')

# create window
#win = visual.Window(size=(1024,800), units='height')
win = visual.Window(fullscr=True, units='height')
mouse = event.Mouse(visible=False)

# set range of coordinates: y range is defined to (-0.5, 0.5),
# x range is calculated from window size
sizeX = win.size[0]
sizeY = win.size[1]
maxY = 0.5
minY = -0.5
maxX = 0.5 * sizeX / sizeY
minX = -maxX

# init visuals
instruction = visual.TextStim(win, wrapWidth=1.5, height=0.03, pos=(0,0),
    text=instructionText)
hline = visual.Line(win, start=(-0.05, 0), end=(0.05, 0), lineWidth=3)
vline = visual.Line(win, start=(0, 0.05), end=(0, -0.05), lineWidth=3)
target = visual.Circle(win, radius=0.01, fillColor='OrangeRed', lineColor='OrangeRed') 

# create timer
timer = core.Clock()

# show instruction
event.clearEvents()
instruction.draw()
win.flip()
event.waitKeys()
win.flip()
core.wait(0.5)

# show visuals
hline.autoDraw = True
vline.autoDraw = True
target.autoDraw = True

# initialize variables
mouse.setPos()
nextData = 0
mouseX = 0
mouseY = 0
noiseX = 0
noiseY = 0
deltaX = 0
deltaY = 0
reverse = 0

# start timer
timer.reset()
time = 0

# run main loop
while True:
    # check if we are done
    if time > totalTime:
        break
    if event.getKeys(['escape']):
        break
    lastTime = time
    time = timer.getTime()
    pos = mouse.getPos()
    mouseX = pos[0]
    mouseY = pos[1]
    deltaTime = time - lastTime

    # create a smoothed random walk
    deltaX = (1-smooth) * random.gauss(0, deltaTime) + smooth * deltaX
    deltaY = (1-smooth) * random.gauss(0, deltaTime) + smooth * deltaY
    noiseX += deltaX
    noiseY += deltaY
    noiseX = max(min(maxX, noiseX), minX)
    noiseY = max(min(maxY, noiseY), minY)
    
    if reverse == 0:
        targetX = noiseX + mouseX
        targetY = noiseY + mouseY
        if time > switchTime:
            reverse = 1
            mouse.setPos((-mouseX, -mouseY))
    else:
        targetX = noiseX - mouseX
        targetY = noiseY - mouseY
     
    targetX = max(min(maxX, targetX), minX)
    targetY = max(min(maxY, targetY), minY)
    target.pos = (targetX, targetY)
    win.flip()
    if time >= nextData:
        # write data record
        nextData = time + dataStep
        f.write(str(round(time, 3)) 
            + ',' + str(mouseX)
            + ',' + str(mouseY)
            + ',' + str(noiseX)
            + ',' + str(noiseY)
            + ',' + str(targetX)
            + ',' + str(targetY)
            + ',' + str(reverse)
            + '\n')

# hide visuals
hline.autoDraw = False
vline.autoDraw = False
target.autoDraw = False
win.flip()

# clean up
f.close()
core.wait(0.3)
win.close()
core.quit()
