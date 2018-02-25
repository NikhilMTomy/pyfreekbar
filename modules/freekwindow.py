#!/usr/bin/env python

import subprocess

def getwindow():
  result = subprocess.run(['xdotool', 'getwindowfocus', 'getwindowname'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
  if len(result) > 50:
    result = result[:50] + '...'
  return_string = (
      '%{+u}'
      '%{+o}'
      ' ' + result + ' '
      '%{-o}'
      '%{-u}'
      )
  return return_string
if __name__ == '__main__':
  print(getwindow())
  
