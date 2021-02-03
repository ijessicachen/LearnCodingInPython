#move the keyboard stuff from above here
import curses

def window(keyboard):
  sh, sw = keyboard.getmaxyx()
  while True:
    userKey = keyboard.getch()
    keyboard.addstr(str(userKey))
    keyboard.addstr(chr(userKey))
    if userKey == 27:
      break
curses.wrapper(window)