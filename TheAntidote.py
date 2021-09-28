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
                x.insert(i, '[x]')
    return bluePrint

def validMove1(layout, previous, playerStart):
    for x in range(len(layout)):
        for i in layout[x]:
            if i == playerStart:
                return True
    return False

loop = 'y'

while loop.lower() == 'y':
    prevPos = ''
    visited = []
    bluePrint = boardReset()
    updateLab(bluePrint)
    msX, msY = rd.randint(0, 4), rd.randint(0, 4)
    aX, aY = rd.randint(0, 4), rd.randint(0, 4)
    antidoteLoc = bluePrint[aY][aX]
    madScientistLoc = bluePrint[msY][msX]
    if antidoteLoc == madScientistLoc:
        aX, aY = rd.randint(0, 4), rd.randint(0, 4)
    currentPos = ''

    for attempts in range(1,11):
        if attempts == 10:
            print('Last chance!')
        else:
            print('Attempt: ' + str(attempts) + ' of 10.')
        visited.append(currentPos)
        #print(visited)
        if madScientistLoc == currentPos:
            antidote(bluePrint)
            msStarter(bluePrint)
            playerPos(currentPos, bluePrint, visited)
            print(updateLab(bluePrint))
            print('Oh no! The Mad Scientist found you!')
            print('The antidote was in room ' + str(antidoteLoc) + '.')
            break
        elif antidoteLoc == currentPos:
            antidote(bluePrint)
            msStarter(bluePrint)
            playerPos(currentPos, bluePrint, visited)
            print(updateLab(bluePrint))
            print('Hooray! You found the antidote in time!')
            break
        else:
            bluePrint = boardReset()
            playerPos(currentPos, bluePrint,visited)
            prevPos = currentPos
            print(updateLab(bluePrint))
            while True:
                print('Enter the next room number you wish to check.')
                currentPos = input('> ').upper()
                bluePrint = boardReset()
                valid = validMove1(bluePrint, prevPos, currentPos)
                if currentPos in visited:
                    print('You\'ve already checked this room.')
                    continue
                elif not valid:
                    print('Please enter a valid room number.')
                    continue
                else:
                    print('No luck in room ' + currentPos + '.')
                    break
            continue
    if currentPos == antidoteLoc:
        print('You consumed the potion and you survived the poison!')
    elif currentPos == madScientistLoc:
        print('\tGAME OVER\t'.center(20,'*'))
    else:
        print('\tGAME OVER\t'.center(20, '*'))
        print('You\'ve run out of time before finding the Antidote.')

    print('\nWould you like to play again? (y or n)')
    loop = input('> ')
