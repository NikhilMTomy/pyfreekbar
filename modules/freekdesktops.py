#!/usr/bin/env python

import subprocess
from modules import freekcolors
#import freekcolors

def getdesktoplist():
  desktops = subprocess.run(['wmctrl', '-d'], stdout=subprocess.PIPE)
  desktops = subprocess.run(['awk', '{print $1$2$11}'], input=desktops.stdout, stdout=subprocess.PIPE)
  desktops = desktops.stdout.decode('utf-8').strip().split('\n')
  desktops = [x for x in [list(y) for y in desktops]]
  return desktops

def getdesktopname(desktop):
  if desktop[2] == '':
    return desktop[0]
  else:
    return desktop[2]

def getdesktops():
  desktoplist = getdesktoplist()
  current_desktop = desktoplist[0]
  foreground = freekcolors.foreground
  current_foreground = freekcolors.background
  background = freekcolors.text_background
  current_background = freekcolors.green
  icon = '' # Desktop siji icon
  return_string = (
      '%{+u}'
      '%{+o}'
      '%{F' + foreground + '}'
      '%{B' + background + '}'
      '%{T2}'
      ' ' + icon + '%{T1} '
      '%{B' + freekcolors.background + '} '
      )

  for desktop in desktoplist:
    if desktop[1] == '*':
      return_string += (
          '%{F' + current_foreground + '}'
          '%{B' + current_background + '}'
          '%{A:wmctrl -s ' + desktop[0] + ':}' 
          ' ' + getdesktopname(desktop) + ' %{A}'
          '%{B' + freekcolors.background + '} '
          )
    else:
      return_string += (

          '%{F' + foreground + '}'
          '%{B' + background + '}'
          '%{A:wmctrl -s ' + desktop[0] + ':}' 
          ' ' + getdesktopname(desktop) + ' %{A}'
          '%{B' + freekcolors.background + '} '
          )
  return_string += (
      '%{B' + freekcolors.background + '}'
      '%{F' + freekcolors.foreground + '}'
      '%{-o}'
      '%{-u}'
      )
  return return_string

if __name__ == '__main__':
  print(getdesktops())
