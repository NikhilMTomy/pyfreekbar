#!/usr/bin/env python

import socket
import subprocess
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
  nmcli = [[y.split() for y in z.split('\n')] for z in nmcli.stdout.decode('utf-8').split('\n\n')]
  found = False
  connected = False
  ssid = ''
  device = ''
  for x in nmcli:
    for y in x:
      if len(y) > 1:
        if y[0].strip() == 'GENERAL.TYPE:':
          device = y[1]
        if len(y) == 3 and y[2].strip() == '(connected)':
          connected = True
        if connected and y[0].strip() == 'GENERAL.CONNECTION:':
          ssid = y[1]
          found = True
          return ssid, device, True
  return False

def getnetwork():
  background = freekcolors.text_background
  foreground = freekcolors.red
  icons = [
      '',
      '',
      '',
      '',
      '',
      ]
  icon = icons[3]
  status = ''

  ssid, device, connected = is_connected()
  if connected:
    if has_internet():
      background = freekcolors.green
    else:
      background = freekcolors.text_background
    foreground = freekcolors.background
    if device == 'wifi':
      icon = icons[0]
    else:
      icon = icons[4]
    status = ' ' + device

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
  print('Connection : ' + str(is_connected()))
