#uhhh there's also stuff I missed here

import curses

def window(colourS):
  #setup
  curses.start_color()
  curses.use_default_colors()

  #initializing
  for i in range(0, curses.COLORS):
    curses.init_pair(i+1, i-1, i-1)
    colourS.addstr(str(chr(9608) + " "), curses.color_pair(i+1))
    if i%16 == 0 and i != 0 and i != 17:
      colourS.addstr("\n")

  colourS.getch()
curses.wrapper(window)