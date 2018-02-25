#!/usr/bin/env python

from modules import freekcolors

def getbat():
  INTERFACE = 'BAT1'
  BAT_DIR = '/sys/class/power_supply/' + INTERFACE + '/'
  background = freekcolors.text_background
  BAT = [
      '', #0
      '', #1
      '', #2
      '', #3
      '', #4
      '', #5
      '', #6
      '', #7
      '', #8
      '', #9
      '', #10
      ]
  icon = ''
  status = ''
  capacity = 0
  return_string = ''
  foreground = freekcolors.foreground

  with open(BAT_DIR + 'status') as status_file:
    status = status_file.read().strip()

  with open(BAT_DIR + 'capacity') as capacity_file:
    capacity = int(capacity_file.read().strip())

  if status == 'Charging':
    icon = BAT[10]
    if capacity > 95:
      background = freekcolors.green
    else:
      background = freekcolors.yellow
  elif capacity < 10:
    background = freekcolors.red
    icon = BAT[0]
  elif capacity < 20:
    background = freekcolors.red
    icon = BAT[1]
  elif capacity < 30:
    icon = BAT[2]
  elif capacity < 40:
    icon = BAT[3]
  elif capacity < 50:
    icon = BAT[4]
  elif capacity < 60:
    icon = BAT[5]
  elif capacity < 70:
    icon = BAT[6]
  elif capacity < 80:
    icon = BAT[7]
  elif capacity < 90:
    icon = BAT[8]
  elif capacity < 100:
    icon = BAT[9]
  
  if background != freekcolors.text_background:
    foreground = freekcolors.background

  return_string = (
      '%{+u}'
      '%{+o}'
      '%{F' + foreground + '}'
      '%{B' + background + '}'
      '%{T2}'
      ' ' + icon + '%{T1}'
      ' ' + str(capacity) + '% '
      '%{B' + freekcolors.background + '}'
      '%{F' + freekcolors.foreground + '}'
      '%{-o}'
      '%{-u}'
      )
  return return_string

if __name__ == '__main__':
  print(getbat())
