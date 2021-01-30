#uhhh there's also stuff I missed here

import curses

def window(colourS):
  #setup
  curses.start_color()
  curses.use_default_colours()

  #initializing
  for i in range(0, curses.COLORS):
    curses.init_pair(i+1, 1, -1)
    colourS.addString(str(1+1), curses.color_pair(i+1))

  colourS.getch()

curses.wrapper(window)