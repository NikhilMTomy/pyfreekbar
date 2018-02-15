#!/usr/bin/env python

from modules import freekcolors
#import freekcolors

def getbat():
  INTERFACE = 'BAT1'
  BAT_DIR = '/sys/class/power_supply/' + INTERFACE + '/'
  background = freekcolors.text_background
  BAT_0 = ''
  BAT_1 = ''
  BAT_2 = ''
  BAT_3 = ''
  BAT_4 = ''
  BAT_5 = ''
  icon = ''
  status = ''
  capacity = 0
  return_string = ''

  with open(BAT_DIR + 'status') as status_file:
    status = status_file.read()

  with open(BAT_DIR + 'capacity') as capacity_file:
    capacity = int(capacity_file.read())

  if status != 'Discharging':
    icon = BAT_5
    if capacity > 95:
      background = freekcolors.green
    else:
      background = freekcolors.yellow
  elif capacity < 20:
    background = freekcolors.red
    icon = BAT_0
  elif capacity < 40:
    icon = BAT_1
  elif capacity < 60:
    icon = BAT_2
  elif capacity < 80:
    icon = BAT_3
  elif capacity < 100:
    icon = BAT_4
  
  if background != freekcolors.text_background:
    foreground = freekcolors.background

  return_string = (
      '%{+u}'
      '%{+o}'
      '%{F' + foreground + '}'
      '%{B' + background + '}'
      ' ' + icon + ' ' + str(capacity) + '% '
      '%{B' + freekcolors.background + '}'
      '%{F' + freekcolors.foreground + '}'
      '%{-o}'
      '%{-u}'
      )
  return return_string

if __name__ == '__main__':
  print(getbat())
