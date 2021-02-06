import curses
from curses import textpad

def board(snakeG):
  #hide the cursor
  curses.curs_set(0)
  #move the snake by itself
  snakeG.nodelay(1)
  #set the timeout ot 0.1 second
  snakeG.timeout(100)
  #get the size of the board
  sh, sw = snakeG.getmaxyx()

  #define the game board
  box = [
    [0, 0],
    [sh-2, sw-1]
  ]
  #draw the game board
  textpad.rectangle(snakeG, box[0][0], box[0][1], box[1][0], box[1][1])

  #define the snake body
  snake = [
    [sh//2, sw//2+1],
    [sh//2, sw//2],
    [sh//2, sw//2-1]
  ]
  snake_ch = chr(9608)
  #draw the snake body
  for point in snake:
    snakeG.addstr(point[0], point[1], snake_ch)

  key = 'a'
  hold = 'a'
  direction = curses.KEY_RIGHT
  while True:
    #user input
    #in nodelay model the -1 will return after timeout
    key = snakeG.getch()
    if key == 27:
      break;
    if key == curses.KEY_UP and hold != curses.KEY_DOWN:
      direction = curses.KEY_UP
    elif key == curses.KEY_RIGHT and hold != curses.KEY_LEFT:
      direction = curses.KEY_RIGHT
    elif key == curses.KEY_DOWN and hold != curses.KEY_UP:
      direction = curses.KEY_DOWN
    elif key == curses.KEY_LEFT and hold != curses.KEY_RIGHT and hold != 'a':
      direction = curses.KEY_LEFT
    else:
      continue

    #move the snake right
    #step 1, prep the new head
    head = snake[0]
    #decide the directions based on user input
    if direction == curses.KEY_UP:
      new_head = [head[0]-1, head[1]]
    elif direction == curses.KEY_RIGHT:
      new_head = [head[0], head[1]+1]
    elif direction == curses.KEY_DOWN:
      new_head = [head[0]+1, head[1]]
    elif direction == curses.KEY_LEFT:
      new_head = [head[0], head[1]-1]
    else:
      continue
    hold = key
    #step 2, draw the new head
    snakeG.addstr(new_head[0], new_head[1], snake_ch)
    snake.insert(0, new_head)
    #step 3, remove the tail
    snakeG.addstr(snake[-1][0], snake[-1][1], " ")
    snake.pop()

    #check if the new snake with new head is touching the border
    snake[0][0]
    snake[0][1]
    
   
curses.wrapper(board)