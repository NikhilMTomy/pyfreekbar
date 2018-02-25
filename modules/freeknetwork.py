#!/usr/bin/env python

import socket
import subprocess
import NetworkManager
from modules import freekcolors

def has_internet():
  try:
    host = socket.gethostbyname("www.google.com")
    s = socket.create_connection((host, 80), 2)
    return True
  except:
    pass
  return False

def is_connected():
  nmcli = subprocess.run(['nmcli', 'device', 'show'], stdout=subprocess.PIPE)
  nmcli = [y.split() for z in nmcli.stdout.decode('utf-8').split('\n\n') for y in z.split('\n')]
  found = False
  connected = False
  ssid = ''
  for x in nmcli:
    for y in x:
      if y == 'GENRAL.DEVICE:':
        connected = x[1]
      if y == '(connected)':
        connected = True
        break
    if found == True:
      break

def getnetwork():
  background = freekcolors.text_background
  foreground = freekcolors.red
  icons = [
      '',
      '',
      '',
      '',
      '',
      ]
  icon = icons[3]
  status = ''

  if has_internet():
    background = freekcolors.green
    foreground = freekcolors.background
    icon = icons[0]
    status = ' ' + NetworkManager.const('device_type', 2)
    #if status=='ethernet':
    # icon = icons[4]
    #else:
    # icon = icons[0]


  return_string = (
      '%{+u}'
      '%{+o}'
      '%{F' + foreground + '}'
      '%{B' + background + '}'
      '%{T2}'
      ' ' + icon + '%{T1}'
      '' + status + ''
      ' %{B' + freekcolors.background + '}'
      '%{F' + freekcolors.foreground + '}'
      '%{-o}'
      '%{-u}'
      )
  return return_string


if __name__ == '__main__':
  print('Connection : ' + str(has_internet()))
