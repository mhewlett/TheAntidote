import numpy as np
import random as rd

def updateLab(layout):
    lab = np.array(layout)
    return lab

def boardReset():
    bluePrint = [['A1','A2','A3','A4','A5'],
                 ['B1','B2','B3','B4','B5'],
                 ['C1','C2','C3','C4','C5'],
                 ['D1','D2','D3','D4','D5'],
                 ['E1','E2','E3','E4','E5']]
    return bluePrint

def msStarter(layout):
    for x in layout:
        for i in range(len(x)):
            if x[i] == madScientistLoc:
                x.remove(madScientistLoc)
                x.insert(i,'[X]')

def antidote(layout):
    for x in layout:
        for i in range(len(x)):
            if x[i] == antidoteLoc:
                x.remove(antidoteLoc)
                x.insert(i,'[A]')

def playerPos(playerStart, layout, visit):
    for x in bluePrint:
        for i in range(len(x)):
            if x[i] == playerStart:
                x.remove(x[i])
                x.insert(i, '[o]')
        for i in range(len(x)):
            if x[i] in visit:
                x.remove(x[i])
                x.insert(i, '[-]')
    return bluePrint

loop = 'y'

while loop.lower() == 'y':
    visited = []
    bluePrint = boardReset()
    updateLab(bluePrint)
    msX, msY = rd.randint(0, 4), rd.randint(0, 2)
    aX, aY = rd.randint(0, 4), rd.randint(0, 1)
    antidoteLoc = bluePrint[aY][aX]
    madScientistLoc = bluePrint[msY][msX]
    currentPos = bluePrint[4][2]

    while True:
        visited.append(currentPos)
        #print(visited)
        if madScientistLoc == currentPos:
            antidote(bluePrint)
            msStarter(bluePrint)
            print(updateLab(bluePrint))
            print('Oh no! The Mad Scientist found you!')
            print('The antidote was in room ' + str(antidoteLoc))
            break
        elif antidoteLoc == currentPos:
            antidote(bluePrint)
            msStarter(bluePrint)
            print(updateLab(bluePrint))
            print('Hooray! You found the antidote in time!')
            break
        else:
            bluePrint = boardReset()
            playerPos(currentPos, bluePrint,visited)
            print(updateLab(bluePrint))
            print('Enter the next room you wish to visit.')
            currentPos = input('> ').upper()
            continue

    print('Would you like to play again? (y or n)')
    loop = input('> ')





