#!/usr/bin/env python

import time
import sys
from modules import freektime
from modules import freekcolors
from modules import freekbat
from modules import freeknetwork
from modules import freekdesktops

while True:
  left = (
      '%{l}'
      '' + freekdesktops.getdesktops() + ''
      ' '
      )
  center='%{c}'
  right = (
      '%{r}' 
      ' '
      '' + freeknetwork.getnetwork() + ''
      ' '
      '' + freekbat.getbat() + ''
      ' '
      '' + freektime.gettime() + ''
      ' '
      )

  left = ' ' + left

  final_string = "{0}{1}{2}".format(left, center, right)

  sys.stdout.write(final_string + "\n")
  sys.stdout.flush()

  time.sleep(1)
