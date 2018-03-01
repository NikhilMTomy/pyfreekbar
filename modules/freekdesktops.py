#!/usr/bin/env python

import subprocess
from modules import freekcolors

def getdesktoplist():
  desktops = subprocess.run(['wmctrl', '-d'], stdout=subprocess.PIPE)
  desktops = subprocess.run(['awk', '{print $1$2$11}'], input=desktops.stdout, stdout=subprocess.PIPE)
  desktops = desktops.stdout.decode('utf-8').strip().split('\n')
  desktops = [x for x in [list(y) for y in desktops]]
  return desktops

def getuseddesktoplist():
  used = subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE)
  used = subprocess.run(['awk', '{print $2}'], input=used.stdout, stdout=subprocess.PIPE)
  used = used.stdout.decode('utf-8').strip().split('\n')
  used = [x for x in used]
  return used

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
  used_foreground = freekcolors.foreground
  unused_foreground = freekcolors.foreground

  background = freekcolors.background
  current_background = freekcolors.green
  used_background = freekcolors.text_background
  unused_background = freekcolors.background

  return_string = (
      '%{+u}'
      '%{+o}'
      '%{B' + freekcolors.background + '} '
      )
  used = getuseddesktoplist()
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
      if desktop[0] in getuseddesktoplist():
        return_string += (
            '%{F' + used_foreground + '}'
            '%{B' + used_background + '}'
            '%{A:wmctrl -s ' + desktop[0] + ':}' 
            ' ' + getdesktopname(desktop) + ' %{A}'
            '%{B' + freekcolors.background + '} '
            )
      else:
        return_string += (
            '%{F' + unused_foreground + '}'
            '%{B' + unused_background + '}'
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
