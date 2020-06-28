#imports
from pynput.keyboard import Key, Controller
import time
import random
from multiprocessing import Process
import sys
from threading import Thread

keyboard = Controller()#defining keyboard

def enter():#making an enter definition
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def text(n=''):#shortcut for keyboard.type
    keyboard.type(n)

class miner():
    def sell():
        counter=0
        time.sleep(1)
        while True:
            time.sleep(random.choice([40,40.2, 40.25, 40.1 , 40.3, 40.35, 40.32, 40.42, 40.35,41.2]))
            text(';sell')
            enter()
            if counter == 3:
                text(';up p all')
                time.sleep(.2)
                enter()
                counter += 1
            elif counter ==6:
                text(';up bp all')
                time.sleep(.2)
                enter()
                counter = 0
            else:
                counter += 1 
    def hunt():
        time.sleep(1)
        while True:
            text(';hunt')
            enter()
            time.sleep(random.choice([60.21, 60.1, 60.23, 60.24, 60.45, 60.6])*5)
    
    def fish():
        time.sleep(2)
        while True:
            text(';fish')
            enter()
            time.sleep(random.choice([60.21, 60.1, 60.23, 60.24, 60.45, 60.6])*5.25)
    
    def q():
        time.sleep(3)
        while True:
            text(';q')
            enter()
            time.sleep(random.choice([1 , 1.25, 1.5, 1.75 ])-.25)
            text(random.choice(['a','b','c','d']))
            enter()
            time.sleep(random.choice([60.21, 60.1, 60.23, 60.24, 60.45, 60.6])*5.3)
        
if __name__ == "__main__":
    Thread(target = miner.sell).start()
    Thread(target = miner.hunt).start()
    Thread(target=miner.fish).start()
    Thread(target=miner.q).start()