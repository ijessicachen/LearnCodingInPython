#move the keyboard stuff from above here
import curses

def window(keyboard):
  while True:
    sh, sw = keyboard.getmaxyx()
    keyboard.addstr(sh-3, 0, str(sh))
    keyboard.addstr(sh-3, sw-3, str(sw))
    userKey = keyboard.getch()
    #Get rid of the weird 5 that shows up for 2 digit codes.For this just add a space at taht spot before htis, you'll get it.
    #to make sure it is centred based on if the width is even or odd
    if sw%2 == 0:
      s = 0.5
    else:
      s = 1
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