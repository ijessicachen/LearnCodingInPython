#Quick list-ish of what my character choices are:
#ground: 9640 OR 11034, try both
#flag: 9873
#bomb: 10040

import curses
from curses import textpad
import random
import math

def initfield(center, size):
  
  board = []
  r, c = 0, 0

  #nested for loops below
  for y in range(center[0] - size[0]//2, center[0] + size[0]//2):
    board.append([[0, 0, 0]] * size[1])
    #last parameter changes the increment it's at, so it's two now, the default is one
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      board[r][c] = [y, x, 0]
      #stdscr.addstr(y, x, chr(9608))
      c = c+1
    r = r+1
    c= 0

  #generate the bombs!
  i = 0 #track the bomb count
  while i < math.prod(size) // 7:
    index = random.randint(0, math.prod(size)-1)
    #figure out our r c
    r = index // size[1]
    c = index - r * size[1]
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


  return board


def colours():
  #curses setup for colours
  curses.start_color()
  curses.use_default_colors()

  for i in range(0, curses.COLORS):
    #initialize color pair
    curses.init_pair(i + 1, i, -1)
  #return colors in a dictionary type
  return{
    "cover": curses.color_pair(5),
    "-1": curses.color_pair(150),
    "1": curses.color_pair(70),
    "2": curses.color_pair(80),
    "3": curses.color_pair(85),
    "4": curses.color_pair(119),
    "5": curses.color_pair(87),
    "6": curses.color_pair(90),
    "7": curses.color_pair(100),
    "8": curses.color_pair(70)
  }


def paintfield(stdscr, board, size, col):
  #painting the board
  for r in range(0, size[0]):
    for c in range(0, size[1]):
      if board[r][c][2] == -1:
        stdscr.addstr(board[r][c][0], board[r][c][1], chr(10040), col["-1"])
      elif board[r][c][2] == 0:
        stdscr.addstr(board[r][c][0], board[r][c][1], " ")
      else:
        #stdscr.addstr(field[r][c][0], field[r][c][1], chr(9608))
        stdscr.addstr(board[r][c][0], board[r][c][1], str(board[r][c][2]), col[str(board[r][c][2])])



def paintcell(stdscr, cell, col, reverse=False):
  if cell[2] == -1:
    cell_ch = chr(10040)
    stdscr.addstr(cell[0], cell[1], chr(10040), col["-1"])
  elif cell[2] == 0:
    stdscr.addstr(cell[0], cell[1], " ")
  else:
    #stdscr.addstr(field[r][c][0], field[r][c][1], chr(9608))
    stdscr.addstr(cell[0], cell[1], str(cell[2]), col[str(cell[2])])

  if reverse:

  
  stdscr.addstr()
      
        


def field(stdscr):
  #turn off the curser
  curses.curs_set(0)
  r, c = 0, 0

  #get dimensions of the field
  sh, sw = stdscr.getmaxyx()
  #center variable
  center = [sh//2, sw//2]
  #set screen size variables
  size = [20, 20]

  #call the field
  board = initfield(center, size)

  col = colours()
  paintfield(stdscr, board, size, col)
  textpad.rectangle(stdscr, board[r][c][0] - 1, board[r][c][1] - 1, center[0] + size[0]//2, center[1] + size[1]+1)

  #paint cell [r][c] reverse
  stdscr.addstr(board[r][c][0], board[r][c][1], str(board[r][c][2]), curses.A_REVERSE)
  
  stdscr.getch()

curses.wrapper(field)