import turtle
import time
import random
turtle.setup(500, 500)
pen = turtle.Turtle()
pen.ht()
pen.pensize(7)
pen.speed(0)

PC = 'X'
PLAYER = 'O'
gameWon = False

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.value = ''

turns = 0

ps = [
    Position(-150, 100), 
    Position(-50, 100),
    Position(50, 100),
    Position(-150, 0), 
    Position(-50, 0),
    Position(50, 0),
    Position(-150, -100), 
    Position(-50, -100),
    Position(50, -100)
]


rows = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

def drawline(x, y, angle, distance):
    pen.penup()
    pen.goto(x, y)
    pen.left(angle)
    pen.pendown()
    pen.forward(distance)

def drawX(x, y):
    drawline(x+10, y+10, 45, 113)
    drawline(x+10, y+90, -90, 113)
    pen.left(45)

def drawO(x, y):
    pen.penup()
    pen.goto(x+50, y+10)
    pen.pendown()
    pen.circle(40)


def printWinner(ps):
    pen.penup()
    pen.goto(0, 200)
    style = ('Courier', 30, 'bold')
    pen.write(f'{ps.value} is the winner!', font=style, align='center')
    global turns
    turns = 10


def drawWinner(ps, angle, x, y, distance):
    pen.penup()
    pen.right(angle)
    pen.goto(ps.x + x, ps.y + y)
    pen.color('purple')
    pen.pendown()
    pen.forward(distance)
    pen.left(angle)


def checkWinner():
    #horizontal
    checkWinnerType(0, 1, 2, 0, 0, 50, 300)
    checkWinnerType(3, 4, 5, 0, 0, 50, 300)
    checkWinnerType(6, 7, 8, 0, 0, 50, 300)
    #Vertical
    checkWinnerType(0, 3, 6, 90, 50, 100, 300)
    checkWinnerType(1, 4, 7, 90, 50, 100, 300)
    checkWinnerType(2, 5, 8, 90, 50, 100, 300)
    #diagonal
    checkWinnerType(0, 4, 8, 45, 0, 100, 424)
    checkWinnerType(2, 4, 6, 135, 100, 100, 424)
    

def checkWinnerType(a, b, c, angle, x, y, distance):
    global gameWon
    if (gameWon == True):
        return    
    if (ps[a].value != "" and ps[a].value == ps[b].value and ps[b].value == ps[c].value):
        drawWinner(ps[a], angle, x, y, distance)
        printWinner(ps[a])
        addResetButton()
        gameWon = True

def drawlines():
    drawline(-150, 100, 0, 300)
    drawline(-150, 0, 0, 300)
    drawline(-50, 200, 270, 300)
    drawline(50, 200, 0, 300)
    pen.right(270)

def isReset(x, y):

    if (x >= -80 and x < 70 and y > -200 and y < -160):
        pen.color('black')
        pen.clear()
        drawlines()
        global turns
        global gameWon
        turns = 0
        gameWon = False
        for p in ps:
            p.value = ''



def nextTurn(x, y):
    global turns
    global PLAYER
    for p in ps:    
        if x > p.x and x < p.x + 100 and y < p.y + 100 and y > p.y:
            if (p.value == ''):
                p.value = PLAYER
                drawO(p.x, p.y)
                turns = turns + 1
    checkWinner()
    isGameOver(x, y)    

def isGameOver(x, y):
    global turns
    global gameWon
    if (turns == 9 and gameWon == False):
        pen.penup()
        pen.goto(0, 200)
        pen.pendown()
        style = ('Courier', 30, 'bold')
        pen.write('Game Over!', font=style, align='center')
        addResetButton()

def PcTurnRandom(): 
    global PC  
    global turns
    empty = []
    for p in ps:
        if (p.value == ''):
            empty.append(p)
    pos = random.randint(0, len(empty) -1)
    p = empty[pos]
    p.value = PC
    drawX(p.x, p.y)
    turns = turns + 1 
    checkWinner()
    isGameOver(p.x, p.y)    

def addResetButton():
    pen.penup()
    pen.goto(-80, -160)
    pen.pendown()
    pen.forward(150)
    pen.right(90)
    pen.forward(40)
    pen.right(90)
    pen.forward(150)
    pen.right(90)
    pen.forward(40)
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    style = ('Courier', 30, 'bold')
    pen.write('Reset', font=style, align='center') 
    pen.right(90)



def pcTurnBlockPlayer(p):
    global turns
    drawX(p.x, p.y)
    p.value = PC
    drawX(p.x, p.y)
    turns = turns + 1
    checkWinner()
    isGameOver(p.x, p.y)

def pcTurnBlock():
    global turns
    for row in rows:
        a = row[0]
        b = row[1]
        c = row[2]
        if(ps[a].value == PLAYER and ps[b].value == PLAYER and ps[c].value == ''):
            pcTurnBlockPlayer(ps[c])
            return True
        if(ps[a].value == '' and ps[b].value == PLAYER and ps[c].value == PLAYER):
            pcTurnBlockPlayer(ps[a])
            return True
        if(ps[a].value == PLAYER and ps[b].value == '' and ps[c].value == PLAYER):
            pcTurnBlockPlayer(ps[b])
            return True
    return False    
    

def pcTurnWin():
    global turns
    for row in rows:
        a = row[0]
        b = row[1]
        c = row[2]
        if(ps[a].value == PC and ps[b].value == PC and ps[c].value == ''):
            pcTurnBlockPlayer(ps[c])
            return True
        if(ps[a].value == '' and ps[b].value == PC and ps[c].value == PC):
            pcTurnBlockPlayer(ps[a])
            return True
        if(ps[a].value == PC and ps[b].value == '' and ps[c].value == PC):
            pcTurnBlockPlayer(ps[b])
            return True
    return False   



def pcTurn():
    if(turns < 9):
        if(pcTurnWin()):
            return
        if(pcTurnBlock()):
            return
        PcTurnRandom()
        

def onClick(x, y):
    global turns
    global gameWon
    if(turns < 9 and gameWon == False):
        nextTurn(x, y)
        pcTurn()
        return
    isReset(x, y)
    
wn = turtle.Screen()
wn.onclick(onClick)

drawlines()

a =  Position(2,3)


print(f'{a.x}')


wn.mainloop()