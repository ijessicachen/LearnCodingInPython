import curses
import random
import math

def initfield(center, size):
  
  board = []

  r, c = 0, 0
  #nested for loops below
  for y in range(center[0] - size[0]//2, center[0] + size[0]//2):
    board.append([[0, 0]] * size[1])
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
      field[r][c][2] = -1
      i = i+1

  #calculate the number of bombs
  for r in range(0, size[0]):
    for c in range(0, size[1]):
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
              board[r][c][2] = board[r][c] + 1


  return board

def paintfield(stdscr, field, size):
  for r in range(0, size[0]):
    for c in range(0, size[1]):
      if board[r][c][2] == -1:
        stdscr.addstr(field[r][c][0], field[r][c][1], chr(9600))
      else:
        #stdscr.addstr(field[r][c][0], field[r][c][1], chr(9608))
        stdscr.addstr(field[r][c][0], field[r][c][1], chr(9608), str(board[r][c][2]))
        


def field(stdscr):
  #get dimensions of the field
  sh, sw = stdscr.getmaxyx()
  #center variable
  center = [sh//2, sw//2]
  #set screen size variables
  size = [sh//2, sw//4]

  #call the field
  board = initfield(center, size)

  paintfield(stdscr, field, size)

  stdscr.getch()

curses.wrapper(field)