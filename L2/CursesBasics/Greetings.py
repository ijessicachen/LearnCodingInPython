#Homework for this, format it properly!

#This include some ASCII stuff

#y is first in curses
import curses

#a literal window
def window(screen):
  #Calculate the centre of the window
  #get the full height and width of the screen
  sh, sw = screen.getmaxyx()

  msg = "Hello Curses!"
  #print out message
  screen.addstr(sh//2, sw//2 - len(msg)//2, msg)

  #ASCII CODE THINGY
  screen.addstr(sh-1, sw-3, str(ord('a')))
  screen.addstr(0, 1, chr(22))

  #beginning keyboard code thingy
  while True:
    # Waiting user's input
    # getch will return teh ascii code, which is an integer
    userKey = screen.getch()
    screen.addstr(str(userKey))
    screen.addstr(chr((userKey)))
    if userKey == 27:
      break

  #collect user information
  screen.getch(sh//2, sw//2)
curses.wrapper(window)