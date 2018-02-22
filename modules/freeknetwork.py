#!/usr/bin/env python

import socket
from modules import freekcolors

def has_internet():
  try:
    host = socket.gethostbyname("www.google.com")
    s = socket.create_connection((host, 80), 2)
    return True
  except:
    pass
  return False

def getnetwork():
  background = freekcolors.text_background
  foreground = freekcolors.foreground
  wifis = [
      '',
      '',
      '',
      ''
      ]
  icon = wifis[3]

  if has_internet():
    background = freekcolors.green
    foreground = freekcolors.background
    icon = wifis[0]


  return_string = (
      '%{+u}'
      '%{+o}'
      '%{F' + foreground + '}'
      '%{B' + background + '}'
      '%{T2}'
      ' ' + icon + '%{T1} wifi '
      '%{B' + freekcolors.background + '}'
      '%{F' + freekcolors.foreground + '}'
      '%{-o}'
      '%{-u}'
      )
  return return_string


if __name__ == '__main__':
  print('Connection : ' + str(has_internet()))
