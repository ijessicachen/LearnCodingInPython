#move the keyboard stuff from above here
import curses

def window(keyboard):
  sh, sw = 0, 0
  while True:
    hh = sh
    hw = sw
    sh, sw = keyboard.getmaxyx()
    if hh != sh or hw != sw:
      keyboard.clear()
      keyboard.refresh()
    keyboard.addstr(sh-3, 0, str(sh))
    keyboard.addstr(sh-3, sw-3, str(sw))
    userKey = keyboard.getch()
    #to make sure it is centred based on if the width is even or odd
    if sw%2 == 0:
      s = 1.5
    else:
      s = 1
    #to cover the third digit since some are two digits so doing this will make sure it will actually be two digits 
    keyboard.addstr(sh//2, int((sw+1)//2+2+s), " ")
    #Printing the code and the chracter
    keyboard.addstr(sh//2, int((sw+1)//2+s), str(userKey))
    keyboard.addstr(sh//2, int((sw+1)//2-s), chr(userKey))
    if userKey == 27:
      #curses.flash()
      #Not sure if I using this right. Maybe it only wokrs with colour?
      break
curses.wrapper(window)
curses.beep()