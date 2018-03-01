#!/usr/bin/env python

################### Modules #####################
import atexit
import time
import sys
import threading
from modules import freektime
from modules import freekcolors
from modules import freekbat
from modules import freeknetwork
from modules import freekdesktops
from modules import freekwindow
#################################################
def exit_handler():
  execute = False
atexit.register(exit_handler)
######### Customizble Variables #################
INTERVAL = 1 # time in seconds

desktops = ''
desktops_delay = 0.5

window = ''
window_delay = 1

network = ''
network_delay = 10

battery = ''
battery_delay = 60

currtime = ''
time_delay = 1
#################################################
execute = True
########### Threaded functions ##################
def getdesktops():
  global execute
  global desktops
  while execute:
    desktops = freekdesktops.getdesktops()
    time.sleep(desktops_delay)
def getwindow():
  global execute
  global window
  while execute:
    window = freekwindow.getwindow()
    time.sleep(window_delay)
def getnetwork():
  global execute
  global network
  while execute:
    network = freeknetwork.getnetwork()
    time.sleep(network_delay)
def getbattery():
  global execute
  global battery
  while execute:
    battery = freekbat.getbat()
    time.sleep(battery_delay)
def gettime():
  global execute
  global currtime
  while execute:
    currtime = freektime.gettime()
    time.sleep(time_delay)
#################################################

################## main loop ####################
def main_loop():
  while execute:
    left = (
        '%{l} '
        '' + desktops + ''
        ' '
        )
    center=(
        '%{c}'
        '' + window + ''
        )
    right = (
        '%{r} ' 
        '' + network + ''
        ' '
        '' + battery + ''
        ' '
        '' + currtime + ''
        ' '
        )

    final_string = "{0}{1}{2}".format(left, center, right)
    sys.stdout.write(final_string + "\n")
    sys.stdout.flush()
    time.sleep(INTERVAL)
#################################################

############## program start ####################
if __name__=='__main__':
  execute = True
  t1 = threading.Thread(target=getdesktops)
  t2 = threading.Thread(target=getwindow)
  t3 = threading.Thread(target=getnetwork)
  t4 = threading.Thread(target=getbattery)
  t5 = threading.Thread(target=gettime)
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  main_loop()
#################################################
