#!/usr/bin/env python
import arrow
from modules import freekcolors

timezone = 'Asia/Kolkata'

def formatter(string):
  return_string = (
      '%{+u}'
      '%{+o}'
      '%{B' + freekcolors.text_background + '}'
      ' ' + string + ' '
      '%{B' + freekcolors.background + '}'
      '%{-u}'
      '%{-o}'
      )
  return return_string

def getdatetime():
  return formatter(arrow.utcnow().to(timezone).format('YYYY-MM-DD HH:mm:ss'))

def gettime():
  return formatter(arrow.utcnow().to(timezone).format('HH:mm:ss'))

def getdate():
  return formatter(arrow.utcnow().to(timezone).format('YYYY-MM-DD'))

if __name__ == '__main__':
  print('datetime : {0}'.format(getdatetime()))
  print('date     : {0}'.format(getdate()))
  print('date     : {0}'.format(gettime()))
