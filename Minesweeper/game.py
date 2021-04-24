#Quick list-ish of what my character choices are:
#ground: 9640 OR 11034, try both
#flag: 9873
#bomb: 10040

import curses
from curses import textpad
import random
import math
import datetime

def initfield(center, size):
  
  board = []
  r, c = 0, 0

  #nested for loops below
  for y in range(center[0] - size[0]//2, center[0] + size[0]//2):
    board.append([])
    #last parameter changes the increment it's at, so it's two now, the default is one
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      board[r].append([y, x, 0, "covered"])
      #stdscr.addstr(y, x, chr(9608))
      c = c+1
    r = r+1
    c= 0

  #generate the bombs!
  #track the bomb count
  i = 0
  while i < 40:
    index = random.randint(0, math.prod(size)-1)
    #figure out our r c
    r = index // size[1]
    c = index - r*size[1]
    if board[r][c][2] == -1:
      continue
    else:
      board[r][c][2] = -1
      i = i+1

  #calculate the number of bombs
  for r in range(0, size[0]):
    for c in range(0, size[1]):
      #CHECK THE BELOW
      if board[r][c][2] == -1:
        #this cell has a bomb
        continue
      
      for sr in [r-1, r, r+1]:
        for sc in [c-1, c, c+1]:
          if sr < 0 or sr >= size[0] or sc < 0 or sc >= size[1]:
            continue #skip
          elif sr == r and sc == c:
            continue
          else:
            if board[sr][sc][2] == -1:
              board[r][c][2] = board[r][c][2] + 1


  return (board, i)


def colours():
  #curses setup for colours
  curses.start_color()
  curses.use_default_colors()

  for i in range(0, curses.COLORS):
    #initialize color pair
    if i == 15:
      curses.init_pair(i + 1, i, 1)
    elif i == 16:
      curses.init_pair(i + 1, i, 196)
    else:
      curses.init_pair(i + 1, i, -1)
  #return colors in a dictionary type
  return{
    "cover": curses.color_pair(1),
    "0": curses.color_pair(1),
    "-1": curses.color_pair(2),
    "1": curses.color_pair(20),
    "2": curses.color_pair(34),
    "3": curses.color_pair(40),
    "4": curses.color_pair(38),
    "5": curses.color_pair(85),
    "6": curses.color_pair(47),
    "7": curses.color_pair(191),
    "8": curses.color_pair(227),
    "flag": curses.color_pair(197),
    "misflag": curses.color_pair(17),
    "blasted": curses.color_pair(16)
  }


def paintfield(stdscr, board, col, center, size, flags, bombs, show = False):
  #painting the board
  for r in range(0, len(board)):
    for c in range(0, len(board[0])):
      paintcell(stdscr, board[r][c], col, False, show)

  #Title
  stdscr.addstr(center[0] - size[0]//2 - 2, center[1] - 5, "Minesweeper")
  #Flag Count
  flagCount(stdscr, flags, bombs, center, size)



def paintcell(stdscr, cell, col, reverse=False, show=False):

  if show:
    if cell[2] == -1:
      if cell[3] == "blasted":
        cell_ch = chr(10040)
        cell_colour = col["blasted"]
        #reverse = False
      else:
        cell_ch = chr(10040)
        cell_colour = col["-1"]
    elif cell[2] == 0:
      cell_ch = " "
      cell_colour = col["-1"]
    else:
      if cell[3] == "flag":
        cell_ch = chr(9873)
        cell_colour = col["misflag"]
      else:
        cell_ch = str(cell[2])
        cell_colour = col[cell_ch]
  else:
    if cell[3] == "covered":
      cell_ch = chr(9608)
      cell_colour = col["cover"]
    elif cell[3] == "flag":
      cell_ch = chr(9873)
      cell_colour = col["flag"]
    elif cell[3] == "dig":
      #so zeroes will just be blank
      if cell[2] == 0:
        cell_ch = str(" ")
        cell_colour = False
      else:
        cell_ch = str(cell[2])
        cell_colour = col[cell_ch]
    elif cell[3] == "blasted":
      cell_ch = chr(10040)
      cell_colour = col["blasted"]
      #reverse = False
  
  if reverse:
      cell_colour = curses.A_REVERSE
  stdscr.addstr(cell[0], cell[1], cell_ch, cell_colour)


def flagcell(cell):
  if cell[3] == "flag":
    cell[3] = "covered"
  elif cell[3] == "covered":
    cell[3] = "flag"
def digcell(cell):
  if cell[3] == "covered":
    if cell[2] == -1:
      cell[3] = "blasted"
    else:
      cell[3] = "dig"

def openaround(stdscr, col, board, r, c):
  flagNum = 0
  if board[r][c][3] == "dig":
    for row in [r-1, r, r+1]:
      for column in [c-1, c, c+1]: 
        if row < 0 or row >= len(board[0]) or column < 0 or column >= len(board[0]):
          continue
        if board[row][column][3] == "flag":
          flagNum += 1
    if board[r][c][2] == flagNum:
      for row in [r-1, r, r+1]:
        for column in [c-1, c, c+1]:
            if row < 0 or row >= len(board[0]) or column < 0 or column >= len(board[0]):
              continue  
            if board[row][column][3] != "flag":
              if board[row][column][3] == "covered":
                if board[row][column][2] == -1:
                  board[row][column][3] = "blasted"
                else:  
                    board[row][column][3] = "dig"
                paintcell(stdscr, board[row][column], col)
                openaround(stdscr, col, board, row, column)
  #return status

def flagCount(stdscr, flags, bombs, center, size):
  fCount = bombs-flags
  stdscr.addstr(center[0] - size[0]//2 - 2, center[1] - size[1]//2 - 6, chr(9873) + " " + str(fCount) + "     ")
def stopwatch(stdscr, center, size, start, elapsed, run = True):
  stopwatch = datetime.timedelta()
  if start == -1:
    stdscr.addstr(center[0] - size[0]//2 - 2, center[1] + size[1]//2 + 3, "0" + "     ")
  elif run == True and start != -1:
    stopwatch = datetime.datetime.now() - start
    msg = '{0}.{1}'.format(stopwatch.seconds, stopwatch.microseconds // 10000)
    stdscr.addstr(center[0] - size[0]//2 - 2, center[1] + size[1]//2 + 3, msg + "     ")





def gameOver(stdscr, board, col, center, size, flags, bombs, start, elapsed): 
  paintfield(stdscr, board, col, center, size, flags, bombs, True)
  stopwatch(stdscr, center, size, start, elapsed, False)
  stdscr.addstr(center[0] + size[0]//2 + 1, center[1] - 4, "game over")
  stdscr.addstr(center[0] + size[0]//2 + 2, center[1] - 16, "Press enter/return to play again")
def youWin(stdscr, center, size, start, elapsed):
  #Okay just as a note I'll make it so they win when they flag all AND they reveal all the board.
  #Both conditions are in the big gamegame loop
  stopwatch(stdscr, center, size, start, elapsed, False)
  stdscr.addstr(center[0] + size[0]//2 + 1, center[1] - 7, "$$$ YOU WIN $$$")
  stdscr.addstr(center[0] + size[0]//2 + 2, center[1] - 16, "Press enter/return to play again")
def coverCheck(stdscr, board, r, c):
  check = 0
  dead = 0
  for r in range(0, len(board)):
      for c in range(0, len(board[0])):
        if board[r][c][3] != "covered":
          check += 1
        if board[r][c][3] == "blasted":
          dead += 1
  return check, dead
          
      
    

def instructions(stdscr):
  stdscr.addstr(20, 20, "Test")





def debugmsg(stdscr, board, cell, show_surrounding = False):
  stdscr.addstr(0, 0, " " * 30)
  stdscr.addstr(0, 0, str(cell))

def printfield(center_yx, size):
  field = initfield(center_yx, size)
  for r in range(0, size[0]):
    print(field[r])
      



def gamegame(stdscr, size, center, r, c):
  while True:
    userKey = stdscr.getch()
    while userKey != ord("r"):
      instructions(stdscr)
    if userKey == ord("u"):
      while userKey != ord("n"):
        instructions(stdscr)
      break
      

  #call the field
  board, bombs = initfield(center, size)
  stdscr.addstr(center[0] + size[0]//3 + 4, center[1] - size[1]//2, " " * size[1]*2)
  stdscr.addstr(center[0] + size[0]//3 + 5, center[1] - size[1], " " * size[1]*2)

  #other variables
  flags = 0
  start = -1
  elapsed = -1
  hold = 0
  live = True

  col = colours()
  textpad.rectangle(stdscr, board[r][c][0] - 1, board[r][c][1] - 2, center[0] + size[0]//2, center[1] + size[1]+1)
  paintfield(stdscr, board, col, center, size, flags, bombs, False)

  #paint cell [r][c] reverse
  paintcell(stdscr, board[r][c], col, True)

  

  #cell[r][c] but reverse
  nr, nc = 0, 0
  #debugmsg(stdscr, board, board[nr][nc])
  while True:
    userKey = stdscr.getch()
    if userKey in [27, 113]:
      break
    if userKey in [curses.KEY_RIGHT, 108]:
        if nc<size[1]-1:
          nc = c+1
    elif userKey in [curses.KEY_LEFT, 104]:
        if nc>0:
          nc = c-1
    elif userKey in [curses.KEY_UP, 107]:
        if nr>0:
          nr = r-1
    elif userKey in [curses.KEY_DOWN, 106]:
        if nr<size[0]-1:
          nr = r+1
    elif userKey == 102:
      flagcell(board[r][c])
      if board[r][c][3] == "flag":
        flags += 1
      if board[r][c][3] == "covered":
        flags -= 1
    elif userKey == 100:
      digcell(board[r][c])
      if hold == 0:
        start = datetime.datetime.now()
        hold += 1
      if board[r][c][2] == 0:
        openaround(stdscr, col, board, r, c)
    elif userKey == 32:
      openaround(stdscr, col, board, r, c)
    
    #debugmsg(stdscr, board, board[nr][nc])
    paintcell(stdscr, board[r][c], col)
    paintcell(stdscr, board[nr][nc], col, True)
    r, c = nr, nc

    flagCount(stdscr, flags, bombs, center, size)
    stopwatch(stdscr, center, size, start, elapsed, True)


    check, dead = coverCheck(stdscr, board, r, c)
    if check == size[0] * size[1]:
      youWin(stdscr, center, size, start, elapsed)
      break
    if dead > 0:
      gameOver(stdscr, board, col, center, size, flags, bombs, start, elapsed)
      break
  
      
    




def field(stdscr):
  #turn off the curser
  curses.curs_set(0)
  r, c = 0, 0

  #make the stopwatch work
  stdscr.nodelay(1)
  stdscr.timeout(50)
  
  #get dimensions of the field
  sh, sw = stdscr.getmaxyx()
  #center variable
  center = [sh//2, sw//2]
  
  
  
  #set screen size variables
  size = [16, 16]

  #Literal game
  gamegame(stdscr, size, center, r, c)

  #OKAY SO HERE IS WHERE I SHOULD PROBABLY MAKE THE LEADERBOARD THING
  while True:
    #hold the screen between games
    userkey = stdscr.getch()
    if userkey == ord('q'):
      break
    elif userkey == 10:
      gamegame(stdscr, size, center, r, c)
    else:
      continue

  
curses.wrapper(field)


printfield([10, 10], [4, 4])